# SEVAL
A library for software engineering task evaluation

## Supported Tasks

- [x] [Code Generation](src/tasks/code_generation/README.md)
- [ ] [Code Summarization](src/tasks/code_summarization/README.md)
- [x] [Code Translation](src/tasks/code_translation/README.md)
- [ ] [Clone Detection](src/tasks/clone_detection/README.md)
- [x] [Code Repair](src/tasks/code_repair/README.md)
- [x] [Code Completion](src/tasks/code_completion/README.md)
- [ ] [Code Search](src/tasks/code_search/README.md)
- [ ] Code Classification
  - [ ] Bug/Defect/ Prediction
  - [ ] Bug/Vulnerability Type Prediction
- [ ] Fault/Bug Localization
- [ ] ...

## How to Contribute

Thank you for your interest in contributing! This document outlines the process for contributing to our project. Your contributions can make a real difference, and we appreciate every effort you make to help improve this project.

## Getting Started

1. **Identify your target software engineering task** (Unfamiliar with SE tasks? Find them [here](https://github.com/gai4se/LLM4SE?tab=readme-ov-file#paper-list)!)

You can either choose to integrate an existing evaluation technique or add a new evaluation technique.

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
</p>

