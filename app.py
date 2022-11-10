import pickle
import streamlit as st
import requests
import numpy as np
import torch
from sentence_transformers import SentenceTransformer, util







embeddings=np.load("arxivtitle_embeddings_10-11-2022.npy")
papers=pickle.load(open('papers.pkl','rb'))















def recommend(query):
    #Compute cosine-similarities with all embeddings
    query_embedd = model.encode(query)
    cosine_scores = util.pytorch_cos_sim(query_embedd, embeddings)
    top5_matches = torch.argsort(cosine_scores, dim=-1, descending=True).tolist()[0][1:6]
    return top5_matches

id = 'quantum'
#query_show_des = papers.loc[netflix_data['show_id'] == id]['description'].to_list()[0]
recommendded_results = recommend(id)

for index in recommendded_results:
    st.text(papers.iloc[index,:])
