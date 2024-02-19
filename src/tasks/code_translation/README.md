# Task: Code Translation

## Problem Definition

### Input

Code written in Java.

### Output

Code in another programming language.

## Input Format

The prediction and references files must be txt format files. They should have the same number of lines. The code is translated line by line. For example, one line in the references file is:
```
public override void Serialize(ILittleEndianOutput out1){out1.WriteShort(field_1_vcenter);}
```

And the corresponding line in your prediction file is:
```
public override void Serialize(ILittleEndianOutput out1){out1.WriteShort(field_1_vcenter);}
```


## Evaluation Metrics and Implementation

- BLEU
- EM (Exact Match)

## Source

- [CodeXGLUE -- Code Translator](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-to-code-trans/evaluator)

## Contributor

Chase Thompson (cbthomp3@ncsu.edu)