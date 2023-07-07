import os
import pickle
import pandas as pd
from langchain.schema import Document
from langchain.document_loaders import UnstructuredFileLoader
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from tqdm import tqdm


embedding_model_name = 'GanymedeNil/text2vec-large-chinese'
docs_path = 'cache/redis_info'
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)


with open('embeddings.pkl', "wb") as fOut:
    pickle.dump({'embeddings': embeddings}, fOut, protocol=pickle.HIGHEST_PROTOCOL)

