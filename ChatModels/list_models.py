from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    print("API key not found")
    exit(1)

genai.configure(api_key=api_key)

models = genai.list_models()
embedding_models = [
    m.name for m in genai.list_models() 
    if 'embedContent' in m.supported_generation_methods
]

print("Available Embedding Models:")
for model in embedding_models:
    print(f" - {model}")

# with open('available_models.txt', 'w') as f:
#     f.write("Available Gemini models for your subscription:\n\n")
#     for model in models:
#         f.write(f"{model.name}\n")
#         f.write(f"  Description: {model.description}\n")
#         f.write(f"  Supported generation methods: {model.supported_generation_methods}\n")
#         f.write("\n")

# print("Available models written to available_models.txt")