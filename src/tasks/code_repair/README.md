# Task: Code Repair

## Problem Definition

### Input

Java function with bugs.

### Output

Repaired code.

## Input Format

References file is a txt file containing Java function to be repaired, one per line. A legal prediction file is expected to be a txt format file. It should have the same number of lines as the references file. Each line is the model prediction for the corresponding input in the references file. For example, one line in the references file is:
```
private TYPE_1 getType ( TYPE_2 VAR_1 ) { TYPE_3 VAR_2 = new TYPE_3 ( STRING_1 ) ; return new TYPE_1 ( VAR_2 , VAR_2 , this , VAR_1 ) ; }
```

And the corresponding line in your prediction file is:
```
private TYPE_1 getType ( TYPE_2 VAR_1 ) { return new TYPE_1 ( VAR_2 , VAR_1 ) ; }
```

## How To Test
The test script for this evaulation is in the src/test/code_generation folder. To test, run the test.py script. The output produced should match the expected.txt file.

## Evaluation Metrics and Implementation

- BLEU
- EM (Exact Match)

## Source

- [CodeXGLUE -- Code Refinement](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-refinement/evaluator)

## Contributor

Mitchell Huggins (mrhuggin@ncsu.edu)