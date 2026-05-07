from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatLLM= ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature= 1.6)
chat_history = []
 
while True:
    userInput = input('You------: ')
    chat_history.append(userInput)
    if userInput == 'Exit' :
        break
    result = chatLLM.invoke(chat_history)
    chat_history.append(result.content)
    print('bot---------:', result.content)

print(chat_history)