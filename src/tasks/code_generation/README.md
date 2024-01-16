# Task: Code Generation

## Problem Definition

### Input

Natural language description of code.

### Output

Code.

## Input Format

Answer file is in the same format of the dev set json lines file. A legal prediction file is expected to be a txt format file. It should have the same number of lines as answer file. Each line is the model prediction for the corresponding input in answer file. For example, one line in the answer file is:
```
{
  "nl": "Increment this vector in this place. con_elem_sep double[] vecElement con_elem_sep double[] weights con_func_sep void add(double)",
  "code": "public void inc ( ) { this . add ( 1 ) ; }"
}
```

And the corresponding line in your prediction file is:
```
public void inc ( ) { this . add ( 1 ) ; }
```


## Evaluation Metrics and Implementation

- BLEU
- EM (Exact Match)

## Source

- [CodeXGLUE - Text2Code Generation](https://github.com/microsoft/CodeXGLUE/tree/main/Text-Code/text-to-code/evaluator)

## Contributor

Bowen Xu (bxu22@ncsu.edu)