import chromadb
from config import settings
import google.generativeai as genai
from chromadb.utils import embedding_functions


class ChromadbManager:
    def __init__(self, persist_directory):
        self.client = chromadb.PersistentClient(path=persist_directory)
    
    def init_collection(self, collection_name="documents_collection"):
        google_api_key = None
        
        if not settings.GOOGLE_API_KEY:
            gapikey = input("Please enter your Google API Key: ")
            genai.configure(api_key=gapikey)
            google_api_key = gapikey
        else:
            google_api_key = settings.GOOGLE_API_KEY
        
        # create embedding function
        embedding_function = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
            api_key=google_api_key,
            task_type="RETRIEVAL_QUERY",
            model_name="gemini-embedding-001"
        )
        # Get or Create the collection.
        collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=embedding_function
        )
        
        return collection
