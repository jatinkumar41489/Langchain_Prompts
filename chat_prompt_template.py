"""
This is an example of how to use the ChatPromptTemplate class from the langchain_core.prompts module to create a chat prompt template. The template defines a system message and a human message, and allows for dynamic content to be inserted into the messages using placeholders.
"""

from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)