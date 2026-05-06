from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatLLM= ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature= 1.6)
response = chatLLM.invoke("write a 5 line poem on software engineering")
print(response.content)