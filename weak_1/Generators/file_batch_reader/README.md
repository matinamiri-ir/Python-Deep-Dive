# Challenge 003 – File Batch Reader

## Overview

This challenge focuses on building a memory-efficient, lazy file reader that streams data from multiple text files and yields lines in configurable batches.

The implementation avoids loading entire files into memory and demonstrates how Python iterators and generators can be combined to build production-style data pipelines.

---

## Objectives

- Implement a custom iterable class.
- Read multiple files lazily.
- Process data using generators.
- Yield fixed-size batches.
- Support reusable iteration.
- Handle file-related errors gracefully.
- Practice clean API design.

---

## Features

- Reads from multiple files.
- Lazy line-by-line streaming.
- Configurable batch size.
- Optional skipping of empty lines.
- UTF-8 encoding support.
- Reusable iterable object.
- Memory-efficient implementation.

---

## Project Structure

```
FileBatchReader
│
├── __iter__()
│
├── _iter_batch()
│
├── _paths_iter()
│
└── _file_get()
```

---

## Python Concepts Covered

- Iterable
- Iterator
- Generator
- `yield`
- `yield from`
- Lazy Evaluation
- Iterator Protocol
- Generator Composition
- Type Hints
- Resource Management
- API Design

---

## Example

```python
reader = FileBatchReader(
    paths=[
        Path("a.txt"),
        Path("b.txt")
    ],
    batch_size=3
)

for batch in reader:
    print(batch)
```

---

## Design Decisions

- Store file paths as a reusable collection.
- Stream file contents lazily.
- Separate responsibilities across helper methods.
- Keep memory usage constant regardless of file size.

---


## Lessons Learned

This challenge demonstrates that building efficient data pipelines is not only about writing working code, but also about designing reusable APIs, understanding Python's iterator protocol, and processing data lazily.