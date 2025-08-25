# AI Calculator Agent

## Overview
This project is a beginner-level AI application that creates an interactive AI assistant capable of performing basic arithmetic calculations (addition, subtraction, multiplication, and division) using a conversational interface. The assistant is powered by Google's Gemini model through LangChain and LangGraph, allowing it to process user input and decide whether to use a calculator tool or respond directly. The project demonstrates the integration of a large language model (LLM) with custom tools to handle specific tasks, making it a great starting point for learning about AI agents and tool usage.

## Project Steps
Here’s a step-by-step guide to setting up and running the project:

1. **Initialize a New UV Project**  
   Inside your project directory, initialize a new UV project to set up a virtual environment and project structure:  
   ```bash
   uv init .
   ```

2. **Install Dependencies**  
   Install the required Python packages using UV, a faster alternative to pip for package installation and dependency resolution:  
   ```bash
   uv add langgraph langchain python-dotenv langchain-google-genai
   ```

3. **Create an Environment File**  
   Create a `.env` file in the project root to store environment variables, such as the API key for the LLM provider:  
   ```bash
   touch .env
   ```  
   Add your API key to the `.env` file in the format:  
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```  
   Replace `your_api_key_here` with the actual API key.

4. **Obtain an API Key**  
   This project uses the Google Gemini API, but you can use an API key from any compatible LLM provider (e.g., OpenAI, Anthropic, etc.). To get a Google Gemini API key:  
   - Visit the Google Cloud Console or the Gemini API provider’s website.  
   - Create a new project and enable the Gemini API.  
   - Generate an API key and copy it to the `.env` file.

5. **Write the Code**  
   Create a `main.py` file and implement the code for the AI calculator agent. The code:  
   - Imports necessary libraries (`langchain`, `langgraph`, `python-dotenv`, etc.).  
   - Defines a `calculator` tool for basic arithmetic operations.  
   - Initializes the Google Gemini model and creates a ReAct agent.  
   - Runs an interactive loop to process user input and stream responses.  
   See the `main.py` file in this repository for the complete implementation.

6. **Run the Application**  
   Activate the UV virtual environment and run the script:  
   ```bash
   uv run python main.py
   ```  
   Interact with the assistant by typing commands (e.g., "Add 5 and 3") or general queries. Type `quit` to exit.

## Python Packages Used
The following Python packages are required for this project:
- **langchain**: Provides tools for building applications with LLMs, including message handling and tool integration.
- **langchain-google-genai**: A wrapper for Google’s Gemini models, enabling their use within LangChain.
- **langgraph**: A library for creating conversational agents with reasoning capabilities (e.g., ReAct agents).
- **python-dotenv**: Loads environment variables from a `.env` file for secure API key management.
- **uv**: A fast Python package installer and resolver used instead of pip for dependency management.

## Additional Information
- **How to Use the Assistant**:  
  After running `main.py`, the assistant will prompt you for input. You can:  
  - Ask for calculations (e.g., "What is 10 divided by 2?" or "Multiply 4 by 5").  
  - Engage in general conversation (e.g., "Tell me about AI").  
  - Type `quit` to exit the program.  
  The assistant uses the ReAct framework to decide whether to use the calculator tool or respond conversationally.

- **Why UV?**  
  UV is a modern, high-performance alternative to pip, offering faster dependency resolution and installation. It simplifies project setup and ensures a clean virtual environment. Learn more at [UV’s official documentation](https://docs.astral.sh/uv/).

- **Extending the Project**:  
  - Add more tools to handle additional tasks (e.g., a weather API tool or a unit converter).  
  - Experiment with different LLM providers by modifying the `ChatGoogleGenerativeAI` model to use another API (e.g., OpenAI’s GPT models).  
  - Enhance the user interface by integrating a web frontend using frameworks like Flask or FastAPI.
