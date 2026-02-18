# Import required libraries
import ast
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load API key from .env file
load_dotenv()

# Initialize Groq model
llm = ChatGroq(model="llama-3.1-8b-instant")

# Example user code (you can later replace this with input())
user_code = """
a = 10
b = 20
print(a + b)
"""

try:
    # -------------------------------
    # 1️⃣ Parse code using AST
    # -------------------------------
    tree = ast.parse(user_code)
    print("✅ Code parsed successfully!\n")

    # -------------------------------
    # 2️⃣ Convert AST back to formatted code
    # -------------------------------
    formatted_code = ast.unparse(tree)

    print("📌 Formatted Code:\n")
    print(formatted_code)
    print("\n" + "-" * 50 + "\n")

    # -------------------------------
    # 3️⃣ Send formatted code to Groq model
    # -------------------------------
    response = llm.invoke(
        f"Explain this Python code in simple words:\n{formatted_code}"
    )

    print("🤖 AI Explanation:\n")
    print(response.content)

except SyntaxError as e:
    print("❌ Syntax Error in the provided code:")
    print(e)

except Exception as e:
    print("❌ An unexpected error occurred:")
    print(e)
