"""
This is a simple chatbot that uses the Google Generative AI model to respond to user queries.
The chatbot maintains a conversation history and allows the user to exit the chat by typing 'exit'.
But it does not maintain the conversation history with specify which message is from system, human and AI.
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

model= ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", temperature=0.7)

chat_history=[]

while True:
    user_input = input("Enter your query (or type 'exit' to quit): ")
    chat_history.append(user_input)
    if user_input.lower() == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI:", result.content)