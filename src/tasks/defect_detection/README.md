# Task: Defect Detection

## Problem Definition

### Input

Source code.

### Output

Binary classification of code. 1 means the code is vulnerable, 0 means it is not

## Input Format

Predictions file is a txt file containing the index of the output and the corresponding prediction of the model. A legal prediction file is expected to be a txt format file. It should have the same number of lines as the test file. An example predictions file is:
```
0	0
1	1
2	1
3	0
4	0
```

The test file contains the correct output for each line corresponding to the predictions file. A legal prediction file is expected to be a jsonl file format. An example test file is:
```
{"project": "FFmpeg", "commit_id": "id0", "target": 0, "func": "func0", "idx": 0}
{"project": "FFmpeg", "commit_id": "id1", "target": 1, "func": "func1", "idx": 1}
{"project": "FFmpeg", "commit_id": "id2", "target": 0, "func": "func2", "idx": 2}
{"project": "FFmpeg", "commit_id": "id3", "target": 0, "func": "func3", "idx": 3}
{"project": "FFmpeg", "commit_id": "id4", "target": 1, "func": "func4", "idx": 4}
```


## Evaluation Metrics and Implementation

- EM (Exact Match)

## Source

- [CodeXGLUE -- Defect Detection](https://github.com/microsoft/CodeXGLUE/blob/main/Code-Code/Defect-detection/evaluator/evaluator.py)

## Contributor

Mitchell Huggins (mrhuggin@ncsu.edu)