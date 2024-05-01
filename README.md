# SEEDEVAL
A library for software engineering task evaluation

## Supported Tasks



### Text-to-Code

#### Task Definition

| Task | Input | Output | Task Definition |
|---------|----------------|----------------| -------------- |
|  Code Generation   |  A natural language description/comment on implmenting certain specification.  |  Code  | Generate code for a given specification written in natural language.  |
|  Code Search   |  A natural language description of code. |  The code that matches the description. | Given a natural language, search for source code that matches the natural language.  |


#### Metrics

| Task | Metric | Reference | If Integrated? | 
|------|---------|----------------|----------------|
|   [Code Generation](https://github.com/SEEDGuard/SEVAL/blob/main/src/test/code_generation/test.py)   |   [EM (Exact Match)](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/code_generation/eval.py)      |      [CodeXGLUE - Text2Code Generation](https://github.com/microsoft/CodeXGLUE/tree/main/Text-Code/text-to-code/evaluator)          |       :heavy_check_mark:        |
|      |   [BLEU](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/code_generation/bleu.py)      |      [CodeXGLUE - Text2Code Generation](https://github.com/microsoft/CodeXGLUE/tree/main/Text-Code/text-to-code/evaluator)          |       :heavy_check_mark:        |
|  [Code Search](https://github.com/SEEDGuard/SEVAL/blob/main/src/test/code_search/test.py)    |    [MRR](https://github.com/SEEDGuard/SEVAL/blob/main/src/task/code_search/eval.py)     |         [CodeXGLUE -- Code Search (AdvTest)](https://github.com/microsoft/CodeXGLUE/blob/main/Text-Code/NL-code-search-Adv/evaluator/evaluator.py) |       :heavy_check_mark:         |


### Code-to-Code

#### Task Definition

| Task | Input | Output | Task Definition |
|---------|----------------|----------------| -------------- |
|  Code Translation   |  A function of code in either C# or Java.  |  The function translated from Java to C# or vice-versa.  | Translate the code from one programming language to another programming language.  |
|  Code Repair   |  A Java function with bugs.  |  The refined function with no bugs.  | Automatically refine code by fixing bugs.  |
|  Code Completion   | A chunk of Java or Python context code.  |  The predicted next token.  | Predict subsequent tokens given the context of code.  |


#### Metrics

| Task | Metric | Reference | If Integrated? |
|------|---------|----------------|----------------|
|  [Code Translation](https://github.com/SEEDGuard/SEVAL/blob/main/src/test/code_translation/test.py)    |    [EM (Exact Match)](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/code_translation/eval.py)     |        [CodeXGLUE -- Code Translator](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-to-code-trans/evaluator)        |         :heavy_check_mark:       |
|      |   [BLEU](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/code_translation/bleu.py)      |      [CodeXGLUE -- Code Translator](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-to-code-trans/evaluator)          |          :heavy_check_mark:      |
|  [Code Repair](https://github.com/SEEDGuard/SEVAL/blob/main/src/test/code_repair/test.py)    |    [EM (Exact Match)](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/code_repair/eval.py)     |        [CodeXGLUE -- Code Refinement](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-refinement/evaluator)        |         :heavy_check_mark:       |
|      |   [BLEU](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/code_repair/bleu.py)      |     [CodeXGLUE -- Code Refinement](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-refinement/evaluator)        |        :heavy_check_mark:        |
|  [Code Completion](https://github.com/SEEDGuard/SEVAL/blob/main/src/test/code_completion/test.py)    |    [EM (Exact Match)](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/code_completion/eval.py)     |        [CodeXGLUE -- Code Completion (token level)](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/CodeCompletion-token/evaluator)        |       :heavy_check_mark:        |


### Code-to-Text

#### Task Definition


| Task | Input | Output | Task Definition |
|---------|----------------|----------------| -------------- |
|  Code Summarization   | Code  |  A natural language description of the code.  | Generate natural language comments for code.  |


#### Metrics

| Task | Metric | Reference | If Integrated? |
|------|---------|----------------|----------------|
|  [Code Summarization](https://github.com/SEEDGuard/SEVAL/blob/main/src/test/code_summarization/test.py)    |    [EM (Exact Match)](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/code_summarization/eval.py)     |        [CodeXGLUE - Code-Text](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Text/code-to-text/evaluator)        |       :heavy_check_mark:        |


### Code Clasification

#### Task Definition


| Task | Input | Output | Task Definition |
|---------|----------------|----------------| -------------- |
|  Clone Detection   | Two examples of code.  |  A binary classification of similar or not.  | Measure the semantic similarity between codes.  |
|  Bug/Defect Prediction - Binary   | Code  | A binary classification of defective or not. | Classify whether code contains defects that may be used to attack software systems.  |
|  Bug/Vulnerability Type Prediction - Multi-class   | Code  |  The type of a variable, parameter, or function.  | Predict the correct type for a particular variable, parameter, or function.  |


#### Metrics

| Task | Metric | Reference | If Integrated? |
|------|---------|----------------|----------------|
|  [Clone Detection](https://github.com/SEEDGuard/SEVAL/blob/main/src/test/clone_detection/test.py)    |    [MAP@R score](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/clone_detection/eval.py)     |    [CodeXGLUE - Clone Detection](https://github.com/microsoft/CodeXGLUE/blob/main/Code-Code/Clone-detection-BigCloneBench/README.md)            |       :heavy_check_mark:        |
|  [Bug/Defect Prediction - Binary](https://github.com/SEEDGuard/SEVAL/blob/main/src/test/defect_detection/test.py)    |    [EM (Exact Match)](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/defect_detection/eval.py)     |    [CodeXGLUE - Defect Detection](https://github.com/microsoft/CodeXGLUE/blob/main/Code-Code/Defect-detection/evaluator/evaluator.py)            |        :heavy_check_mark:       |
|  [Bug/Vulnerability Type Prediction - Multi-class](https://github.com/SEEDGuard/SEVAL/blob/main/src/test/type_prediction/test.py)    |     [EM (Exact Match)](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/type_prediction/eval.py)    |      [CodeXGLUE -- Type Prediction -- TypeScript](https://github.com/microsoft/CodeXGLUE/blob/main/Code-Code/TypePrediction-TypeScript/evaluator/evaluator.py)          |       :heavy_check_mark:        |


### Others

#### Task Definition


| Task | Input | Output | Task Definition |
|---------|----------------|----------------| -------------- |
|         |         |         |         |


#### Metrics

| Task | Metric | Reference | If Integrated? |
|------|---------|----------------|----------------|
|  Fault/Bug Localization    |         |  [Paper with Replication Package]()             |               |


## How to Contribute

Thank you for your interest in contributing! This document outlines the process for contributing to our project. Your contributions can make a real difference, and we appreciate every effort you make to help improve this project.

## Getting Started

1. **Identify your target software engineering task** (Unfamiliar with SE tasks? Find them [here](https://github.com/gai4se/LLM4SE?tab=readme-ov-file#paper-list)!)

You can either choose to integrate an existing evaluation technique or add a new evaluation technique. 

Note, there could be evaluation tasks that are currently being worked on. Check the pull requests tab to see if a task is already in the works

3. **Integrate the evaluation method**

Ensure that you have a detailed readme that describes how to use the evaluation method.

An example of an evaluation method and appropriate readme can be found [here](https://github.com/SEEDGuard/SEVAL/tree/main/src/tasks/code_generation).

3. **Add a test script for you evaluation**

In order to ensure the validity of the evaluation method, we require that you provide a test script as well. 

There is a separate test folder that you must add your tests to. We also ask that you provide a 'how-to-test' section in your readme, detailing how to test the evaluation method.

An example test script can be found [here](https://github.com/SEEDGuard/SEVAL/blob/main/src/test/code_generation/test.py).

## Coordinator

Mitchell Huggins, please contact [mrhuggin@ncsu.edu](mrhuggin@ncsu.edu) if any questions about SEVAL.

## Contributors

<p align="left"><a href="https://github.com/mrhuggins03"><img src="https://avatars.githubusercontent.com/mrhuggins03?v=4" width="50px" alt="mrhuggins03" /></a>
<a href="https://github.com/chaseltb"><img src="https://avatars.githubusercontent.com/chaseltb?v=4" width="50px" alt="chaseltb" /></a>
<a href="https://github.com/ArsalaanK7"><img src="https://avatars.githubusercontent.com/ArsalaanK7?v=4" width="50px" alt="ArsalaanK7" /></a>
<a href="https://github.com/BrennenFa"><img src="https://avatars.githubusercontent.com/BrennenFa?v=4" width="50px" alt="BrennenFa" /></a>
<a href="https://github.com/EZ7051"><img src="https://avatars.githubusercontent.com/EZ7051?v=4" width="50px" alt="EZ7051" /></a>
<a href="https://github.com/ywang146"><img src="https://avatars.githubusercontent.com/ywang146?v=4" width="50px" alt="ywang146" /></a>
<a href="https://github.com/kritipat"><img src="https://avatars.githubusercontent.com/kritipat?v=4" width="50px" alt="kritipat" /></a>
<a href="https://github.com/gsharma3"><img src="https://avatars.githubusercontent.com/gsharma3?v=4" width="50px" alt="gsharma3" /></a>
</p>

## Dependancy
- python 3.6 or 3.7
- numpy
