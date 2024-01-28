# Task: Clone Detection - BigCloneBench

## Problem Definition

### Input

Pairs of code snippets.

### Output

Determine whether each pair is a code clone or not.

## Input Format

The answer file is in the same format as the dev set JSON lines file. A legal prediction file is expected to be a JSON lines file. Each line in the prediction file represents the model's prediction for the corresponding input in the answer file. For example, one line in the answer file is:
```
{
  "label": "Clone",
  "code1": "public void inc ( ) { this . add ( 1 ) ; }",
  "code2": "public void inc ( ) { this . add ( 1 ) ; }"
}
```

And the corresponding line in your prediction file is:
```
{
  "label": "Clone",
  "code1": "public void inc ( ) { this . add ( 1 ) ; }",
  "code2": "public void inc ( ) { this . add ( 1 ) ; }"
}
```

## How To Test
The test script for this evaluation is located in the src/test/code_clone_detection folder. To test, run the test.py script. The output produced should match the predicted_results.txt file.

```
python src/test/code_clone_detection/test.py --answers labels.txt --predictions predicted_results.txt
```

## Evaluation Metrics and Implementation
The performance is evaluated by F1 score where a binary classification is conducted. 1 stands for semantic equivalence and 0 for others.

$F1 \text{ Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$

Accuracy measures the overall correctness of the model's predictions.

$Accuracy = \frac{\text{True Positives} + \text{True Negatives}}{\text{Total Instances}}$

## Source

- [CodeXGLUE - Clone Detection (BigCloneBench)](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/Clone-detection-BigCloneBench/evaluator)

## Contributor

Kriti Patnala (kpatnal@ncsu.edu)
