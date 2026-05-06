from langchain_huggingface import HuggingFaceEmbeddings

embeds = HuggingFaceEmbeddings(model_name = 'your model path')

text = "I am superman"

embeds.embed_query(text)

print(str(embeds))