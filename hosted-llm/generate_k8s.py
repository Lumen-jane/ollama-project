import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro')

PROMPT = """
Generate an ideal Kubernetes {format_type} file with best practices. Just share the YAML without any explanation between two lines to make copying easy.
Include:

- Defining Deployments, Services, and ConfigMaps
- Setting up Namespace and RBAC for security
- Using Secrets for sensitive data
- Implementing Health Checks (Liveness & Readiness Probes)
- Ensuring Resource Limits and Requests
- Using Horizontal Pod Autoscaling
- Configuring Persistent Volumes and Persistent Volume Claims
- Using ConfigMaps for environment variables
- Implementing rolling updates and rollback strategies
- Setting up Ingress for external access
- Optimizing Networking with Network Policies
"""

def generate_kubernetes(format_type):
    response = model.generate_content(PROMPT.format(format_type=format_type))
    return response.text

if __name__ == '__main__':
    format_type = input("Enter the format (YAML or JSON): ").strip().lower()
    kubernetes_yaml = generate_kubernetes(format_type)
    print("\nGenerated Kubernetes Configuration:\n")
    print(kubernetes_yaml)
