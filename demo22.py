import pickle
import streamlit as st
import requests
import numpy as np
import torch
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('sentence-transformers/bert-base-nli-mean-tokens')

embeddings = np.load("arxivtitle_embeddings_10-11-2022.npy")
papers = pickle.load(open('papers.pkl', 'rb'))


def recommend(query):
    # Compute cosine-similarities with all embeddings
    query_embedd = model.encode(query)
    cosine_scores = util.pytorch_cos_sim(query_embedd, embeddings)
    top5_matches = torch.argsort(cosine_scores, dim=-1, descending=True).tolist()[0][1:6]
    return top5_matches


st.set_page_config(layout="wide")

st.markdown(
    f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 70%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
    unsafe_allow_html=True,
)
#################

header_container = st.container()

from PIL import Image
arxiv_img = Image.open('arxiv.png')

with header_container:
    # for example a logo or a image that looks like a website header

    # different levels of text you can include in your app
    st.title("Arxiv Research Paper Recommender")
    # st.header("Welcome!")
    #st.image(PIL.Image.open('arxiv.png'))
    # st.subheader("This is a great app")
    st.write(
        "Searching For recommendation of simmilar research Paper ?",
        "Your search ends here !!! \U0001F642")

selected_keyword = st.text_input(
    "Type Keyword for Related Paper .", 'Quantum'
)

recommendded_results = recommend(selected_keyword)
# l=[]
if st.button('Show Recommendation'):

    for index in recommendded_results:
        # st.text(papers.iloc[index,:])
        # st.text(papers.iloc[index].iloc[0])
        # l.append(papers.iloc[index].iloc[0])
        with st.expander(papers.iloc[index].iloc[0]):
            st.write("Published Year :  ",papers.iloc[index].iloc[2])
            st.write("Paper DOI :  ",papers.iloc[index].iloc[3])
            st.write("Abstract :  ",papers.iloc[index].iloc[1])
