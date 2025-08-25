from langchain_core.messages import HumanMessage            # import HumanMessage class, which represents a message from the user in a conversation 
from langchain_google_genai import ChatGoogleGenerativeAI   # import the Google Gemini LLM wrapper. So, we can use Google's Gemini models
from langchain.tools import tool                            # defines custom functions as tools that the AI agent can call when needed
from langgraph.prebuilt import create_react_agent           # allowing the model to think about whether it needs to use a tool or respond directly
from dotenv import load_dotenv                              
from typing import Literal                                  # specifically to restrict a string to specific valeus (eg: 'add', 'subtract', etc.)

load_dotenv()       # loads enviroment variable from ".env" file

@tool
def calculator(a: float, b: float, operation: Literal['add', 'subtract', 'multiply', 'divide']) -> str:
    """ 
    Useful for performing basic arithmatic calculation with numbers.
    The 'operation' parameter must be one of 'add', 'subtract', 'multiply', or 'divide'.
    """
    if operation == 'add':
        print("Tool has been called.")
        return f"The sum of {a} and {b} is {a + b}"
    elif operation == 'subtract':
        print("Tool has been called.")
        return f"The difference of {a} and {b} is {a - b}"
    elif operation == 'multiply':
        print("Tool has been called.")
        return f"The product of {a} and {b} is {a * b}"
    elif operation == 'divide':
        print("Tool has been called.")
        if b == 0:
            return "Error: Division by zero is not allowed."
        return f"The quotient of {a} and {b} is {a / b}"
    else:
        print("Tool has been called.")
        return "Error: Invalid operation specified."

def main():
    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", temperature=0)        # Initializes the Google gemini LLM. Output is deterministic

    tools = [calculator]
    agent_executor = create_react_agent(model, tools)

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform basic calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        print("\nAssistant: ", end="") 
        for chunk in agent_executor.stream(                     # chunks are essentially parts of a response coming from our agent
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")              # allows us to stream larger response from the agent, it won't look like a whole response at once, but typing word by word.
        print()

if __name__ == "__main__":
    main()                      # ensures the "main()" function runs only when the script is executed directly