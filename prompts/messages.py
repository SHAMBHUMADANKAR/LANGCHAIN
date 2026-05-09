from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
chat = [
    SystemMessage(content='You are an honest AI assistant, you stick to what is correct'),
    HumanMessage(content='Hey, which city is better - Bangalore or Newyork'),
]

result = model.invoke(chat)
chat.append(result)
print(chat)