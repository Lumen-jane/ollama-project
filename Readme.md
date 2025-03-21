# Generate Ansible, dockerfile, k8s File using Ollama

## Overview
This Python script generates an Ansible configuration file in either YAML or JSON format using the Ollama LLM API. It follows best practices for writing modular, efficient, and maintainable Ansible playbooks.

## i tried the hosted llm and also the local-llm

## Features
- Allows users to choose between YAML or JSON format.
- Generates an Ansible playbook with best practices.
- Uses the Ollama LLM model (`llama3.2:latest`) for AI-generated content.

## Prerequisites
Ensure you have the following installed on your system:

- Python 3.x
- A virtual environment (optional but recommended)
- The `ollama` Python package

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Lumen-jane/local-llm.git
   cd local-llm
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the ansible script with:
```sh
python3 generate_ansible.py
```

You will be prompted to enter the format (YAML or JSON):
```
Enter the format (YAML or JSON): yaml
```

The generated Ansible playbook will be displayed in the terminal.

Run the dockerfile with:
```sh
python3 generate_dockerfile.py

```

## DO THE SAME WITH K8s







