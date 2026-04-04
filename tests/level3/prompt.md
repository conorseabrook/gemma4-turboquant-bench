# Level 3: Multi-Step with Verification

## Test 3A — Write + run + verify
```
Create `utils/prime_sieve.py` implementing the Sieve of Eratosthenes. It should accept N as a command-line argument and print all primes up to N, one per line. Then run it with N=1000 and verify the output contains exactly 168 primes.
```

## Test 3B — Generate + process
```
Write `utils/generate_data.py` that creates `data/sample.csv` with 100 rows containing columns: name, age (18-80), email, salary (30000-150000). Use random but realistic data. Then write `utils/summarize_data.py` that reads `data/sample.csv` and prints: average age, average salary, age distribution (count per decade: 18-29, 30-39, etc.), and salary percentiles (25th, 50th, 75th). Run both scripts and show the output.
```

## Test 3C — HTTP endpoint
```
Create `utils/word_api.py` using Python's built-in http.server module. It should have two endpoints: POST /analyze (accepts JSON with a "text" field, returns word count and character count as JSON), and GET /health (returns {"status": "ok"}). Start the server on port 8082, test both endpoints with curl, then stop the server.
```
