import pickle
import streamlit as st
import requests
import numpy as np
import torch
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('sentence-transformers/bert-base-nli-mean-tokens')

embeddings=np.load("arxivtitle_embeddings_10-11-2022.npy")
papers=pickle.load(open('papers.pkl','rb'))

def recommend(query):
    #Compute cosine-similarities with all embeddings
    query_embedd = model.encode(query)
    cosine_scores = util.pytorch_cos_sim(query_embedd, embeddings)
    top5_matches = torch.argsort(cosine_scores, dim=-1, descending=True).tolist()[0][1:6]
    return top5_matches

st.markdown("""
        <h1 style='text-align: center; margin-bottom: -35px;'>
        Arxiv Research Paper Recommender
        </h1>
    """, unsafe_allow_html=True
    )

    

st.write(
        "Searching For recommendation of simmilar research Paper ?",
        "Your search ends here !!! \U0001F642")

selected_keyword = st.text_input(
    "Type Keyword for Related Paper .",'Quantum'
)

if st.button('Show Recommendation'):
    
    for index in recommendded_results:
        
        #st.text(papers.iloc[index,:])
        st.text(papers.iloc[index].iloc[0])
    

    recommendded_results = recommend(selected_keyword)

for index in recommendded_results:
    st.text(papers.iloc[index,:])
