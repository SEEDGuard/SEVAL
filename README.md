# SEVAL
A library for software engineering task evaluation

## Supported Tasks

### Text-to-Code

| Task | Metric | Reference | If Integrated? | 
|------|---------|----------------|----------------|
|   [Code Generation](https://github.com/SEEDGuard/SEVAL/blob/main/src/test/code_generation/test.py)   |   [EM (Exact Match)](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/code_generation/eval.py)      |      [CodeXGLUE - Text2Code Generation](https://github.com/microsoft/CodeXGLUE/tree/main/Text-Code/text-to-code/evaluator)          |       :heavy_check_mark:        |
|      |   [BLEU](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/code_generation/bleu.py)      |      [CodeXGLUE - Text2Code Generation](https://github.com/microsoft/CodeXGLUE/tree/main/Text-Code/text-to-code/evaluator)          |       :heavy_check_mark:        |


### Code-to-Code

| Task | Metric | Reference | If Integrated? |
|------|---------|----------------|----------------|
|  [Code Translation](https://github.com/SEEDGuard/SEVAL/blob/main/src/test/code_translation/test.py)    |    [EM (Exact Match)](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/code_translation/eval.py)     |        [CodeXGLUE -- Code Translator](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-to-code-trans/evaluator)        |               |
|      |   [BLEU](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/code_translation/bleu.py)      |      [CodeXGLUE -- Code Translator](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-to-code-trans/evaluator)          |               |
|  [Code Repair](https://github.com/SEEDGuard/SEVAL/blob/main/src/test/code_repair/test.py)    |    [EM (Exact Match)](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/code_repair/eval.py)     |        [CodeXGLUE -- Code Refinement](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-refinement/evaluator)        |               |
|      |   [BLEU](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/code_repair/bleu.py)      |     [CodeXGLUE -- Code Refinement](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-refinement/evaluator)        |               |
|  [Code Completion](https://github.com/SEEDGuard/SEVAL/blob/main/src/test/code_completion/test.py)    |    [EM (Exact Match)](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/code_completion/eval.py)     |        [CodeXGLUE -- Code Completion (token level)](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/CodeCompletion-token/evaluator)        |       :heavy_check_mark:        |
|  Code Search    |         |                |               |

### Code-to-Text

| Task | Metric | Reference | If Integrated? |
|------|---------|----------------|----------------|
|  [Code Summarization](https://github.com/SEEDGuard/SEVAL/blob/main/src/test/code_summarization/test.py)    |    [EM (Exact Match)](https://github.com/SEEDGuard/SEVAL/blob/main/src/tasks/code_summarization/eval.py)     |        [CodeXGLUE - Code-Text](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Text/code-to-text/evaluator)        |       :heavy_check_mark:        |


### Code Clasification

| Task | Metric | Reference | If Integrated? |
|------|---------|----------------|----------------|
|  Clone Detection    |         |    [CodeXGLUE - Clone Detection](https://github.com/microsoft/CodeXGLUE/blob/main/Code-Code/Clone-detection-BigCloneBench/README.md)            |               |
|  Bug/Defect/ Prediction    |         |    [Paper]()            |               |
|  Bug/Vulnerability Type Prediction    |         |      [Paper]()          |               |


### Others

| Task | Metric | Reference | If Integrated? |
|------|---------|----------------|----------------|
|  Fault/Bug Localization    |         |                |               |


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
</p>

## Dependancy
- python 3.6 or 3.7
