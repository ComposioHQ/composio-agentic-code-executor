# Composio Code Executor Tool - A Comprehensive Guide


<p align="center"><a href="https://github.com/SamparkAI"><img src="https://avatars.githubusercontent.com/u/128464815?s=200&v=4" alt="Composio Logo" /></a></p>

<p align="center">
<a href="https://github.com/SamparkAI/composio-agentic-code-executor/stargazers"><img src="https://img.shields.io/github/stars/SamparkAI/composio-agentic-code-executor" alt="Stars Badge"/></a>
<a href="https://github.com/SamparkAI/Composio-Function-Calling-Benchmark/blob/master/LICENSE"><img src="https://img.shields.io/github/license/SamparkAI/Composio-Function-Calling-Benchmark?color=2b9348" alt="License Badge"/></a>
<a href="#"><img src="https://visitor-badge.laobi.icu/badge?page_id=SamparkAI.composio-agentic-code-executor" alt="Visitor Badge"/></a></p></p>


Welcome to the Composio Code Executor Tool repository! This repository accompanies our blog post announcing the release of our new Code Executor Tool. It provides a comprehensive guide and practical examples to help you understand and utilize the tool effectively.

## Overview

The Composio Code Executor Tool is a powerful utility designed to execute code across various agentic platforms. 



## Run these Files

### Getting Started

To get started with the Composio Code Executor Tool, clone this repository to your local machine:

```
git clone https://github.com/SamparkAI/composio-agentic-code-executor.git
```

Then, navigate to the cloned directory:

```bash
cd composio-agentic-code-executor
```

Create a `.env` file, and put environmental keys:

```
OPENAI_API_KEY=<openai_api_key>
```
and all other Keys,  corresponding to the framework.

### Autogen
```bash
pip install composio_autogen
python code_itrprtr_autogen.py
```

### CrewAI
```bash
pip install composio_crewai
python code_itrprtr_crewai.py
```

### Julep
```bash
pip install composio_julep
python code_itrprtr_julep.py
```

### Lyzr
```bash
pip install composio_lyzr
python code_itrprtr_lyzr.py
```

### Griptape
```bash
pip install composio_griptape
python code_itrprtr_griptape.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, please feel free to contact us.

Enjoy exploring the Composio Code Executor Tool!
