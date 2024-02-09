# Task: Defect detection
### Problem Definition
Detect if the given code is insecure.\
\
**Input** The source code\
\
**Output** The binary classification of the security of the code. 0 represents secure, and 1 represents insecure
### Input Format
##### Download and Preprocess

1.Download dataset from [website](https://drive.google.com/file/d/1x6hoF7G-tSYxg8AFybggypLZgMGDNHfF/view?usp=sharing) to "dataset" folder or run the following command:

```shell
cd dataset
pip install gdown
gdown https://drive.google.com/uc?id=1x6hoF7G-tSYxg8AFybggypLZgMGDNHfF
cd ..
```

2.Preprocess dataset

```shell
cd dataset
python preprocess.py
cd ..
```
There will be at lease 3 fileds in each json object:

- **func**: the source code
- **target**: 0 or 1 (vulnerability or not)
- **idx**: the index of example

The prediction file will be in TXT format, and each line will represent one function. It will have the same number of lines as the jsonl file.\
\
There will be two rows in the prediction file, the first one is the id of the function, and the second one is the fulnerability of the function.


# Evaluation of Defect Detection
### Files needed
besides the evaluator, you will need 2 additional files: The preprocessed jsonl file(test.jsonl), and the predition(preditions.txt)\
\
The jsonl file will contain several json objects, and each one represent one function. For example:
```
{"project": "FFmpeg", "commit_id": "id0", "target": 0, "func": "func0", "idx": 0}
{"project": "FFmpeg", "commit_id": "id1", "target": 1, "func": "func1", "idx": 1}
{"project": "FFmpeg", "commit_id": "id2", "target": 0, "func": "func2", "idx": 2}
{"project": "FFmpeg", "commit_id": "id3", "target": 0, "func": "func3", "idx": 3}
{"project": "FFmpeg", "commit_id": "id4", "target": 1, "func": "func4", "idx": 4}
```
\
A prediction file that has predictions in TXT format, such as evaluator/predictions.txt. For example:
```
0	0
1	1
2	1
3	0
4	0
```
### How to run 
To run the evaluation, navigate to the evaluator's folder and run the following command:
```shell
python3 evaluator/evaluator.py -a evaluator/test.jsonl -p evaluator/predictions.txt

```
And it wiil print the accuracy of the prediction. for example:
```
{'Acc': 0.6}
```
### Evaluation Metrics and Implementation
The evaluator will ready the two given files, and find each json object's prediction by using its id and compare its "target" field with its prediction, and print the mean of accuracy score of all the preditions.

### Source

- [CodeXGLUE - Code2Code Defect Detection](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/Defect-detection/evaluator)

### Contributor

David Wang(ywang146@ncsu.edu)
