# Task: Clone Detection - BigCloneBench

## Problem Definition

### Input
Pairs of code snippets.

### Output
Determine whether each pair is a code clone or not. A binary classification (0/1) is conducted, where 1 stands for semantic equivalence and 0 for others.

## File Formats
The input file is stores in a JSON lines file. Each row contains the following:
1. func: the code to assess
2. index: the index number assigned to this piece of code 

```
{
  "func": "public Object run() {
               try {
                   MessageDigest digest = MessageDigest.getInstance(\"SHA\");
                   digest.update(buf.toString().getBytes());
                   byte[] data = digest.digest();
                   serialNum = new BASE64Encoder().encode(data);
                   return serialNum;
               } catch (NoSuchAlgorithmException exp) {
                   BootSecurityManager.securityLogger.log(Level.SEVERE, exp.getMessage(), exp);
                   return buf.toString();
               }
           }",
  "idx": "10005624"
}
```

The prediction file is a text file where each row gives the following three pieces of information
1. The index of one of the pairs of code checked
2. The index of the another pair
3. The binary classification (1 for equivalence)

## How To Test
The test script for this evaluation is located in the src/test/clone_detection folder. To test run the following test.py script. The output produced should match the answers.txt file.

```
python src/task/clone_detection/eval.py -a src/test/clone_detection/answers.txt -p src/test/clone_detection/predictions.txt
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
