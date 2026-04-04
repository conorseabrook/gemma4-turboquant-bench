# Building llama.cpp with TurboQuant + CUDA Flash Attention

Instructions for compiling the TurboQuant fork of llama.cpp on Windows with CUDA and Flash Attention support. Tested on an RTX 4090 with CUDA 13.2.

## Requirements

| Tool | Version | Purpose |
|------|---------|---------|
| CMake | 4.3+ | Build system |
| CUDA Toolkit | 13.2+ | GPU compute |
| VS 2022 Build Tools | MSVC 19.44+ | C/C++ compiler |
| Ninja | 1.13+ | Build backend |

## 1. Install Build Tools

```powershell
winget install Kitware.CMake --accept-package-agreements --accept-source-agreements
winget install Nvidia.CUDA --accept-package-agreements --accept-source-agreements
winget install Microsoft.VisualStudio.2022.BuildTools --accept-package-agreements --accept-source-agreements
winget install Ninja-build.Ninja --accept-package-agreements --accept-source-agreements
```

After installing VS Build Tools, open the Visual Studio Installer, select "Visual Studio Build Tools 2022", click Modify, and verify that **"Desktop development with C++"** is checked. The winget install alone may not pull the full C++ toolchain — you may need to toggle the workload off and on, then click Modify to force the download (~5 GB).

Reboot after installation.

### Verify

```powershell
cmake --version
nvcc --version
Test-Path "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\*\bin\Hostx64\x64\cl.exe"
```

## 2. Clone the TurboQuant Fork

```bash
git clone https://github.com/TheTom/llama-cpp-turboquant.git
cd llama-cpp-turboquant
git checkout feature/turboquant-kv-cache
```

We used TheTom's fork because it is based on recent llama.cpp with Gemma 4 architecture support (via mainline PR #21309). The older `spiritbuun/llama-cpp-turboquant-cuda` fork does not recognize the `gemma4` architecture.

## 3. Build

Create `build.bat` in the repo root:

```bat
@echo off
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
cd /d %~dp0
if exist build rmdir /s /q build
mkdir build
cd build
cmake -G Ninja ^
  -DGGML_CUDA=ON ^
  -DGGML_CUDA_FA=ON ^
  -DGGML_CUDA_FA_ALL_QUANTS=ON ^
  -DCMAKE_CUDA_ARCHITECTURES=89 ^
  -DCMAKE_BUILD_TYPE=Release ..
if %errorlevel% neq 0 (
    echo CMAKE CONFIGURE FAILED
    exit /b 1
)
cmake --build . --config Release -j%NUMBER_OF_PROCESSORS%
if %errorlevel% neq 0 (
    echo BUILD FAILED
    exit /b 1
)
echo BUILD SUCCEEDED
```

Run:

```powershell
cmd /c build.bat
```

### CMake Flags

| Flag | Purpose |
|------|---------|
| `-DGGML_CUDA=ON` | Enable CUDA backend |
| `-DGGML_CUDA_FA=ON` | Enable Flash Attention (required for TurboQuant) |
| `-DGGML_CUDA_FA_ALL_QUANTS=ON` | Enable FA for turbo3/turbo4 quant types |
| `-DCMAKE_CUDA_ARCHITECTURES=89` | Target Ada Lovelace (RTX 4090). Use `86` for Ampere (RTX 3090), `75` for Turing |

Build time: ~5-10 minutes (596-623 compilation units, mostly CUDA kernels).

### Known Build Issues

**M_PI undefined (MSVC):** If using the `spiritbuun` fork, MSVC will fail with `error C2065: 'M_PI': undeclared identifier` in `ggml-turbo-quant.c`. Fix:

```c
// Before #include <math.h>
#define _USE_MATH_DEFINES

// After includes
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif
```

TheTom's fork does not have this issue.

## 4. Download the Model

```bash
# Q5_K_M (higher quality, ~19.3 GB)
curl -L -o gemma-4-26B-A4B-it-Q5_K_M.gguf \
  "https://huggingface.co/bartowski/google_gemma-4-26B-A4B-it-GGUF/resolve/main/gemma-4-26B-A4B-it-Q5_K_M.gguf"

# Q4_K_M (smaller, ~17 GB, fallback option)
curl -L -o gemma-4-26B-A4B-it-Q4_K_M.gguf \
  "https://huggingface.co/ggml-org/gemma-4-26B-A4B-it-GGUF/resolve/main/gemma-4-26B-A4B-it-Q4_K_M.gguf"
```

Do **not** use Ollama's cached GGUF blob. Ollama's format has 1014 tensors; the TurboQuant fork expects 658 and will fail with a tensor count mismatch.

## 5. Run

```bash
./build/bin/llama-server \
  -m /path/to/gemma-4-26B-A4B-it-Q5_K_M.gguf \
  --cache-type-k turbo3 \
  --cache-type-v turbo3 \
  -c 262144 \
  -ngl 99 \
  -fa on \
  --port 8081 \
  --host 0.0.0.0
```

| Flag | Purpose |
|------|---------|
| `--cache-type-k turbo3 --cache-type-v turbo3` | TurboQuant 3-bit KV cache |
| `-c 262144` | Full 262K native context window |
| `-ngl 99` | Offload all layers to GPU |
| `-fa on` | Required for TurboQuant KV types |
| `--host 0.0.0.0` | Accept connections from other machines on the network |

Do **not** pass `--chat-template gemma`. The GGUF file contains the correct template. Overriding it causes garbled output.

## 6. Verify

```bash
# Health check
curl http://localhost:8081/health

# Test inference
curl http://localhost:8081/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"gemma4","messages":[{"role":"user","content":"What is 2+2?"}],"max_tokens":50}'
```

A web UI is available at `http://localhost:8081`.

## 7. Network Access

To serve to other machines on the local network, create a firewall rule:

```powershell
# Run as Administrator
New-NetFirewallRule -DisplayName "llama-server" -Direction Inbound -Protocol TCP -LocalPort 8081 -Action Allow
```

Then connect from the client machine using the server's LAN IP.

## Fallback Configuration

If VRAM is tight, use Q4_K_M with reduced context:

```bash
./build/bin/llama-server \
  -m /path/to/gemma-4-26B-A4B-it-Q4_K_M.gguf \
  --cache-type-k turbo3 \
  --cache-type-v turbo3 \
  -c 131072 \
  -ngl 99 \
  -fa on \
  --port 8081 \
  --host 0.0.0.0
```

This uses ~19.1 GB VRAM at 139 tok/s with 131K context.

## Common Pitfalls

- **`--chat-template gemma`** — causes garbled output ("gemma____..." garbage, only 2 prompt tokens parsed instead of the full input). The GGUF file contains the correct chat template baked in. Do not override it.
- **Ollama GGUF blobs** — Ollama stores models in its own format with a different tensor count (1014 vs 658). Download directly from [ggml-org](https://huggingface.co/ggml-org/gemma-4-26B-A4B-it-GGUF) or [bartowski](https://huggingface.co/bartowski/google_gemma-4-26B-A4B-it-GGUF).
- **`-fa on` omitted** — Flash Attention must be explicitly enabled. Without it, the server falls back to non-FA attention, which is slower and may not correctly handle turbo-quantized KV cache types.
- **Ollama TurboQuant support** — Ollama does not support TurboQuant as of April 2026. Expected Q3 2026.
- **`spiritbuun` fork** — the `spiritbuun/llama-cpp-turboquant-cuda` fork is based on older llama.cpp that does not recognize the `gemma4` architecture (added post-Gemma 4 release on April 2, 2026). Use TheTom's fork.
