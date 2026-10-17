""""
This is an example of how to use the MessagePlaceholder class from the langchain_core.prompts module to create a chat prompt template with dynamic content. The MessagePlaceholder allows for the insertion of variable content into the chat prompt, enabling more flexible and interactive conversations.

You can simply understand that it helps you to maintain a message history of the converssation between the user and the AI model. It allows you to keep track of the previous messages exchanged in the conversation, which can be useful for context and continuity in the dialogue.

example: You are interacting with a customer support chatbot. 
Your Query: Where is my refund?
Chatbot Response: Your refund is being processed and should be credited to your account within 3-5 business days.
-->After 3 days,you ask the chatbot again about your refund status. The chatbot takes the previous conversation from the database where it is stored and responds to your query with the context of the previous conversation. This helps the chatbot provide a more personalized and relevant response based on the history of the conversation.
"""

from langchain_core.prompts import ChatPromptTemplate, MessagePlaceholder

# chat template

chat_template=ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagePlaceholder(variable_name='chat_history'),  
    ('human', '{user_input}')
])

# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
print(chat_history)

# create a prompt

prompt = chat_template.invoke({'chat_history':chat_history, 'user_input':'Where is my refund'}) 

print(prompt)