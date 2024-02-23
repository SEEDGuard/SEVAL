# Task: Code Search (AdvTest)

## Problem Definition

### Input
Natural language description of code.

### Output
A list of code that matches the natural language. 

## Input Format
Each line of data file represents one function, and each row is represented as below.
 - url: the url for the example
 - docstring: the top-level comment or docstring, if it exists in the original string
 - function: the code for the example
 - idx: the index of example

Examples:
```
{"url": "url0", "docstring": "doc0","function": "fun0", "idx": 10}
{"url": "url1", "docstring": "doc1","function": "fun1", "idx": 11}
{"url": "url2", "docstring": "doc2","function": "fun2", "idx": 12}
{"url": "url3", "docstring": "doc3","function": "fun3", "idx": 13}
{"url": "url4", "docstring": "doc4","function": "fun4", "idx": 14}
```

THe predictions file contains the expected answers as a list of predicted answers for each URL as their index code.
```
{"url": "url0", "answers": [10,11,12,13,14]}
{"url": "url1", "answers": [10,12,11,13,14]}
{"url": "url2", "answers": [13,11,12,10,14]}
{"url": "url3", "answers": [10,14,12,13,11]}
{"url": "url4", "answers": [10,11,12,13,14]}
```

## How To Test
To evaluate the predictoins for this task and report the MRR score, run the following command.

```
python src/tasks/code_search/eval.py -a src/test/code_search/test.txt -p src/test/code_search/predictions.txt
```

## Evaluation Metrics and Implementation
- MRR score

## Source
[CodeXGLUE - Code Search (AdvTest)](https://github.com/microsoft/CodeXGLUE/tree/main/Text-Code/NL-code-search-Adv)

## Contributor
Kriti (kpatnal@ncsu.edu)
