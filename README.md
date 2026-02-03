# GenAI Documentation Generator
This project is a GenAI-powered web application that automatically generates technical or business documentation for ETL pipelines and data workflows.
Users paste ETL code or configuration into a web UI, and a backend microservice uses a LLM (Large Language Model) to give standard and concise documentation.
The goal is to demonstrate practical usage of ReactJS, Python microservices, and GenAI in a real-world scenario.

## Tech Stack

**Frontend**
- ReactJS
- JavaScript
- HTML / CSS

**Backend**
- Python
- FastAPI

**GenAI**
- Ollama (Phi-3 model)

## Flow
1. The user enters ETL or pipeline code in the React UI and selects the documentation type.
2. React sends a POST request with the input data to the FastAPI backend, and it validates the request.
3. The backend constructs a prompt and sends it to a locally hosted LLM via Ollama.
4. The LLM generates documentation based on the prompt rules.
5. FastAPI returns the generated documentation in the form of JSON, and React UI displays the formatted output back to the user.
