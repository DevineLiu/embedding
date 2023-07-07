import os
import pickle
import pandas as pd
from langchain.schema import Document
from langchain.document_loaders import UnstructuredFileLoader
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from tqdm import tqdm

with open('embeddings.pkl', "rb") as fIn:
    stored_data = pickle.load(fIn)
    embeddings = stored_data['embeddings']
    
for doc in tqdm(os.listdir(docs_path)):
    if doc.endswith('.md'):
        f=open(f'{docs_path}/{doc}','r',encoding='utf-8')
        docs.append(Document(page_content=''.join(f.read().split()), metadata={"source": f'doc_id_{doc}'}))
        
        
print(embeddings)
vector_store = FAISS.from_documents(docs, embeddings)
vector_store.save_local('cache/redis_info')