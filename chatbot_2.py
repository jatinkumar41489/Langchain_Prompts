""""
This shows how a chatbot recieves system messages, human messages and AI messages and responds to them using the Google Generative AI model. and also maintains a conversation history with specify which message is from system, human and AI.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()  # Load environment variables from .env file

model= ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", temperature=0.7)

chat_history=[
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input("Enter your query (or type 'exit' to quit): ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)