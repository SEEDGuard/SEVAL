# Task: Defect Detection

## Problem Definition

Given a source code, the task is to identify whether it is an insecure code that may attack software systems, such as resource leaks, use-after-free vulnerabilities and DoS attack. We treat the task as binary classification (0/1), where 1 stands for insecure code and 0 for secure code.

### Dataset

The dataset we use comes from the paper Devign: Effective Vulnerability Identification by Learning Comprehensive Program Semantics via Graph Neural Networks. We combine all projects and split 80%/10%/10% for training/dev/test.

### Download and Preprocess

1.Download dataset from website to "dataset" folder or run the following command:

cd dataset
pip install gdown
gdown https://drive.google.com/uc?id=1x6hoF7G-tSYxg8AFybggypLZgMGDNHfF
cd ..

2.Preprocess dataset

cd dataset
python preprocess.py
cd ..
Data Format
After preprocessing dataset, you can obtain three .jsonl files, i.e. train.jsonl, valid.jsonl, test.jsonl

For each file, each line in the uncompressed file represents one function. One row is illustrated below.

func: the source code
target: 0 or 1 (vulnerability or not)
idx: the index of example
Data Statistics
Data statistics of the dataset are shown in the below table:

#Examples
Train	21,854
Dev	2,732
Test	2,732

### Evaluator
We provide a script to evaluate predictions for this task, and report accuracy score.

Example
python tasks/eval.py -a test/defect_detection/test.jsonl -p test/defect_detection/predictions.txt
{'Acc': 0.6}

### Predicted Input

A predications file that has predictions in TXT format, such as evaluator/predictions.txt. For example:

0	0
1	1
2	1
3	0
4	0
Pipeline-CodeBERT
We also provide a pipeline that fine-tunes CodeBERT on this task.

Fine-tune
cd code
python run.py \
    --output_dir=./saved_models \
    --model_type=roberta \
    --tokenizer_name=microsoft/codebert-base \
    --model_name_or_path=microsoft/codebert-base \
    --do_train \
    --train_data_file=../dataset/train.jsonl \
    --eval_data_file=../dataset/valid.jsonl \
    --test_data_file=../dataset/test.jsonl \
    --epoch 5 \
    --block_size 400 \
    --train_batch_size 32 \
    --eval_batch_size 64 \
    --learning_rate 2e-5 \
    --max_grad_norm 1.0 \
    --evaluate_during_training \
    --seed 123456  2>&1 | tee train.log
Inference
cd code
python run.py \
    --output_dir=./saved_models \
    --model_type=roberta \
    --tokenizer_name=microsoft/codebert-base \
    --model_name_or_path=microsoft/codebert-base \
    --do_eval \
    --do_test \
    --train_data_file=../dataset/train.jsonl \
    --eval_data_file=../dataset/valid.jsonl \
    --test_data_file=../dataset/test.jsonl \
    --epoch 5 \
    --block_size 400 \
    --train_batch_size 32 \
    --eval_batch_size 64 \
    --learning_rate 2e-5 \
    --max_grad_norm 1.0 \
    --evaluate_during_training \
    --seed 123456 2>&1 | tee test.log

### Expectations
python ../evaluator/evaluator.py -a ../dataset/test.jsonl -p saved_models/predictions.txt
{'Acc': 0.6207906295754027}

### Results

The results on the test set are shown as below:

Methods	ACC
BiLSTM	59.37
TextCNN	60.69
RoBERTa	61.05
CodeBERT	62.08
Reference
@inproceedings{zhou2019devign,
  title={Devign: Effective vulnerability identification by learning comprehensive program semantics via graph neural networks},
  author={Zhou, Yaqin and Liu, Shangqing and Siow, Jingkai and Du, Xiaoning and Liu, Yang},
  booktitle={Advances in Neural Information Processing Systems},
  pages={10197--10207},
  year={2019}
}

## Source

- [CodeXGLUE -- Code to Code -- Defect Detection](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/Defect-detection)

## Contributor

Rohan Nandula (rnandul@ncsu.edu)


