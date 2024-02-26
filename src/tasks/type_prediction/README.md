# Task: Type Prediction

## Problem Definition

### Input

A sequence of source code.

### Output

Type of a particular variable, parameter, or function.

## Input Format

The predictions file is a txt file containing the index of the output and the corresponding type prediction of the model. A legal prediction file is expected to be a txt format file. It should have the same number of lines as the test file. An example of 4 lines of a predictions file is:
```
0	HttpClient
1	Router
2	void
3	number
```

The test file contains the correct output for each line corresponding to the predictions file. A legal test file is expected to be a txt file with the same format as the predictions. An example 4 lines of a test file is:
```
0	HttpClient
1	Router
2	void
3	number
```

## How To Test
The test script for this evaulation is in the src/test/type_prediction folder. To test, run the test.py script. The output produced should match the expected.txt file.

## Evaluation Metrics and Implementation

- EM (Exact Match)

## Source

- [CodeXGLUE -- Type Prediction -- TypeScript](https://github.com/microsoft/CodeXGLUE/blob/main/Code-Code/TypePrediction-TypeScript/evaluator/evaluator.py)

## Contributor

Mitchell Huggins (mrhuggin@ncsu.edu) 
