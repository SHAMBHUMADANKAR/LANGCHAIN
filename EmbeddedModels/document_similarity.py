from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2", dimensions = 300)

documents = [
    "Virat is kohli is an Indian cricketer and known for his aggressive batting style.",
    "Sachin Tendulkar is a former Indian cricketer and one of the greatest batsmen in the history of cricket.",
    "M.S. Dhoni is a former Indian cricketer and captain of the Indian national team, known for his calm demeanor and finishing abilities.",
    "Rohit Sharma is an Indian cricketer and known for his ability to score big centuries in limited-overs cricket."
]

query = "Who is Sharma?"
documents_embeddings = embeddings.embed_documents(documents)
query_embeddings = embeddings.embed_query(query)

# Always send the query in 2d and docs is always 2d
similarity = cosine_similarity([query_embeddings], documents_embeddings )[0]
print(similarity)