# Task: Code Clone Detection

## Problem Definition

### Input

Two snippets of code.

### Output

True if the pieces of code are considered semantically equivalent, false otherwise. 

## Input Format

The dataset used is BigCloneBench, and it is stored in jsonlines format. A row in the file contains a _func_ attribute, which contains the function contents; the other attribute is _idx_, which is used to identify a function in the dataset. An example of a row would be: 
```
{"func": "
      @Override\n    public InitResult init(String name) {\n        this.urlString = name;\n        URL url;\n        URLConnection con;\n
      try {\n            url = new URL(urlString);\n            con = url.openConnection();\n            int size = con.getContentLength();\n
      char[] characters = new char[size];\n            BufferedReader in = new BufferedReader(new InputStreamReader(url.openStream()));\n
      in.read(characters);\n            in.close();\n            return new InitResult(0, size, characters);\n        } catch (Exception e) {\n
      throw new ParserException(e);\n        }\n    }\n",
"idx": "10093209"}

```

Three answer files are provided in a txt format: test.txt, train.txt, and valid.txt. Each of the files follows the format: 
idx1 idx2 label, idx1 and idx2 represent the indices of the two functions being compared, and the label will be a 1 for semantic equivalence and 0 otherwise. An example of a row in an answer file would look like the following: 
```
13988825 8660836 0
```

The predictions file will follow the same format as the answers file: idx1 idx2 label


## Evaluation Metrics and Implementation

- EM (Exact Match)

## Source

- [CodeXGLUE - Code2Code Generation]([https://github.com/microsoft/CodeXGLUE/tree/main/Text-Code/text-to-code/evaluator](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/Clone-detection-BigCloneBench)https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/Clone-detection-BigCloneBench])

## Contributor

Gustavo Zuniga Padron (gzuniga@ncsu.edu)
