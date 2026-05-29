from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

def main():
    print("Hello from langchain-practice!")
    print("shaurya")


if __name__ == "__main__":
    main()
