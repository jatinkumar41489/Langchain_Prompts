""""
This shows how a chatbot recieves system messages, human messages and AI messages and responds to them using the Google Generative AI model. and also maintains a conversation history with specify which message is from system, human and AI.
"""
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", temperature=0.7)

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
