# Task: Code Completion

## Problem Definition
Predict the next code token based on the context of previous tokens, with the aim of enhancing software development efficiency. 
Evaluation is conducted at the token level.

### Input
Context of previous code tokens.

### Output
Prediction of the next code token.

## Input Format
Each line in the prediction file must correspond to a line in the answer file, containing the same number of tokens. 
Example: 

Line from input file
```
<s> import json <EOL> json . load ( f ) </s>
```

Corresponding line from predictions file
```
. import numpy <EOL> json . dump ( open ) <EOL>
```

## How To Test
The test script for this evaluation is in the src/test/code_completion folder. To test, run the test.py script. The output produced should match the expected.txt file.

## Evaluation Metrics and Implementation
Measured by comparing the predicted tokens against the actual tokens, and provides a percentage value indicating the accuracy of predictions.

## Source

- [CodeXGLUE -- Code Completion (token level)](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/CodeCompletion-token/evaluator)

## Contributor
Arsalaan Shah Khan (askhan6@ncsu.edu)
