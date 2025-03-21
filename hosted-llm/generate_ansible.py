import google.generativeai as genai
import os

# Load the API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-pro')

PROMPT = """
Generate an ideal Ansible for {format_type} with best practices. Just share the YAML without any explanation between two lines to make copying the Ansible file easy.
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
    response = model.generate_content(PROMPT.format(format_type=format_type))
    return response.text

if __name__ == '__main__':
    format_type = input("Enter the format (YAML or JSON): ").strip().lower()
    ansible = generate_ansible(format_type)
    print("\nGenerated Ansible:\n")
    print(ansible)
