from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv


load_dotenv()

chatLLM= ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature= 1.6)
chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]
 
while True:
    userInput = input('You------: ')
    # chat_history.append(userInput)
    chat_history.append(HumanMessage(userInput))
    if userInput == 'Exit' :
        break
    result = chatLLM.invoke(chat_history)
    # chat_history.append(result.content)
    chat_history.append(AIMessage(result.content))
    print('bot---------:', result.content)

print(chat_history)