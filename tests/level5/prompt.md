# Level 5: Multi-File Coordination

## Test 5A — Python package
```
Create a Python package `mathlib/` with the following structure:
- `mathlib/__init__.py` that exports everything from the submodules
- `mathlib/stats.py` with functions: mean, median, mode, stdev
- `mathlib/linear.py` with classes: Vector (add, dot_product) and Matrix (add, multiply, transpose)
- `mathlib/demo.py` that imports from the package and demonstrates every function and method

Run demo.py to verify everything works.
```

## Test 5B — Config-driven application
```
Create an `app/` directory with these files:
- `app/config.json` with settings: host (localhost), port (8083), log_level (INFO), max_retries (3)
- `app/config.py` that loads and validates config.json (check required keys exist, port is int, log_level is valid)
- `app/logger.py` that sets up Python logging based on the config's log_level
- `app/server.py` with an HTTP server that has a GET /health endpoint returning {"status": "ok", "config": {"host": "...", "port": ...}}
- `app/main.py` as the entry point that loads config, sets up logging, starts the server, and logs startup info

Run main.py, test the health endpoint with curl, then stop the server.
```
