# Level 1: Single File Generation

## Test 1A — Text analysis utility
```
Create a file `utils/text_stats.py` with a function `analyze_text(text: str) -> dict` that returns a dictionary with these keys: word_count, sentence_count, average_word_length, most_common_word, unique_word_count. Then run it with a sample paragraph to verify it works.
```

## Test 1B — Graph class
```
Create a file `utils/graph.py` with a Graph class using an adjacency list. It should support: add_node, add_edge (weighted, directed by default), bfs, dfs, shortest_path (Dijkstra), and has_cycle. Then create a small test graph and demonstrate each method works.
```

## Test 1C — CSV transformer
```
Create a file `utils/csv_transformer.py` that works as a CLI tool. It should read CSV from stdin and write transformed CSV to stdout. Support these flags: --uppercase (uppercase all string values), --round N (round numeric values to N decimal places), --rename OLD:NEW (rename a column). Multiple flags can be combined. Test it by creating a small sample CSV file in data/ and piping it through with a few flags.
```
