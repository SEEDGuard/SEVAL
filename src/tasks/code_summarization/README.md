# Task: Code Generation

## Problem Definition

### Input

Correct natural language comment.

### Output

Generated natural language comment.

## Input Format

References file is a txt file a comment for a particular portion of code, one per line. A legal prediction file is expected to be a txt format file. It should have the same number of lines as the references file. Each line is the model prediction for the corresponding input in the references file. For example, one line in the references file is:
```
0	Outputs the deferred summary information saved via
```

And the corresponding line in your prediction file is:
```
0	Prints a summary message
```

## How To Test
The test script for this evaulation is in the src/test/code_summarization folder. To test, run the test.py script. The output produced should match the expected.txt file.

## Evaluation Metrics and Implementation

- BLEU
- EM (Exact Match)

## Source

- [CodeXGLUE - Text2Code Generation](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Text/code-to-text/evaluator)

## Contributor