import ollama

PROMPT = """
Generate an ideal Ansible file in {format_type} format with best practices. Just share the {format_type} without any explanation between two lines to make copying the Ansible file easy.
Include:

- Defining hosts and setting up inventory
- Installing necessary dependencies
- Setting up variables and defaults
- Using roles and tasks for better organization
- Ensuring idempotency in tasks
- Using handlers for service restarts
- Managing secrets securely with Ansible Vault
- Leveraging templates for configuration files
- Implementing error handling and validations
- Using tags for selective task execution
- Testing playbooks before deploying to production
- Optimizing performance with async and batch execution
- Keeping playbooks modular and reusable
"""

def generate_ansible(format_type):
    formatted_prompt = PROMPT.format(format_type=format_type.upper())  # Corrected formatting
    response = ollama.chat(model='llama3.2:latest', messages=[{'role': 'user', 'content': formatted_prompt}])
    return response['message']['content']  # Ensure correct response handling

if __name__ == '__main__':
    format_type = input("Enter the format (YAML or JSON): ").strip().upper()
    ansible = generate_ansible(format_type)
    print("\nGenerated Ansible:\n")
    print(ansible)
