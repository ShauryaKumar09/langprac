from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

def main():
    print("Hello from langchain-practice!")
    print(os.getenv("GROQ_API_KEY"))


if __name__ == "__main__":
    main()
