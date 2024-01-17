# Task: Code Translation

## Problem Definition
This tool is designed for the the migration of legacy software from one language in a platform to another. The
task is to translate the code such as Java into C#. 

### Input

The input file should be a `.txt` file.

### Output

The output is a `.txt` file with the translated functions in the target language.

## Input Format
The input file is expected to be a .txt file where each line contains a code snippet of the old language. The number of lines in the input file should exactly match the number of lines in the corresponding answer file. 



```
public virtual NGit.Api.SubmoduleAddCommand SetPath(string path){this.path = path;return this;}

```

And the corresponding line in your prediction file is:
```
public virtual NGit.Api.SubmoduleAddCommand SetPath(string path){this.path = path;return this;}

```


## Evaluation Metrics and Implementation

- BLEU : 
- EM (Exact Match)

## Source

- [CodeXGLUE - Code2Code Translation](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-to-code-trans)

## Contributor

Sanjit Verma (skverma@ncsu.edu)
