# Level 4: Debugging

Each test contains intentional bugs. Copy the buggy fixture file into `utils/` before giving the prompt.

## Test 4A — Runtime error (1 bug)
Setup: `cp tests/level4/buggy_sort.py utils/sort.py`
```
Copy `tests/level4/buggy_sort.py` to `utils/sort.py`. The file contains merge sort and quick sort implementations, but there's a bug. Find the bug, fix it, and verify both sorting algorithms work correctly with a test.
```

## Test 4B — Logic errors (2 bugs)
Setup: `cp tests/level4/buggy_calculator.py utils/calculator.py`
```
Copy `tests/level4/buggy_calculator.py` to `utils/calculator.py`. This is an expression evaluator that handles +, -, *, / with proper operator precedence. It has two bugs. Find both bugs, fix them, and verify with these test cases: "2 + 3 * 4" should equal 14, "10 - 2 - 3" should equal 5, "6 / 2 * 3" should equal 9.
```

## Test 4C — Multiple errors (3 bugs)
Setup: `cp tests/level4/buggy_todo.py utils/todo.py`
```
Copy `tests/level4/buggy_todo.py` to `utils/todo.py`. This is a todo manager with save/load, complete, and delete functionality. It has three bugs. Find all three, fix them, and verify by: adding a todo, completing it, adding another, deleting it, and checking that save/load preserves the data correctly.
```
