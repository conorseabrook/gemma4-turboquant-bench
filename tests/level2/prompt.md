# Level 2: Read + Modify

Requires Level 1 files to exist.

## Test 2A — Add a feature
```
Read the file `utils/text_stats.py`. Add a new function `compare_texts(text1: str, text2: str) -> dict` that returns a dictionary with: jaccard_similarity (float, intersection over union of word sets), shared_words (list of words in both texts), length_difference (word count difference, text1 minus text2). Do not break the existing analyze_text function.
```

## Test 2B — Add an algorithm
```
Read the file `utils/graph.py`. Add an optional `algorithm` parameter to the `shortest_path` method that accepts either "dijkstra" (default) or "bellman_ford". Implement the Bellman-Ford algorithm as the alternative. Do not break existing functionality — calling shortest_path without the algorithm parameter should behave exactly as before.
```

## Test 2C — Refactor
```
Read the file `utils/csv_transformer.py`. The transformation logic (uppercase, rounding, renaming) is currently inline in the transform_csv function. Refactor it so each transformation is its own function. The CLI interface and behavior must remain exactly the same — same flags, same input/output format.
```
