{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dda67103",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "import streamlit as st\n",
    "import requests\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6a5154f",
   "metadata": {},
   "outputs": [],
   "source": [
    "movies = pickle.load(open('model/movie_list.pkl','rb'))\n",
    "similarity = pickle.load(open('model/similarity.pkl','rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df54b735",
   "metadata": {},
   "outputs": [],
   "source": [
    "embeddings=np.load(r\"C:\\Users\\shyam\\Downloads\\arxiv\\arxivtitle_embeddings_10-11-2022.npy\")\n",
    "papers=pickle.load(open(r\"C:\\Users\\shyam\\Downloads\\arxiv\\papers.pkl\",'rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee66b4a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import torch\n",
    "from sentence_transformers import SentenceTransformer, util\n",
    "\n",
    "def recommend(query):\n",
    "    #Compute cosine-similarities with all embeddings \n",
    "    query_embedd = model.encode(query)\n",
    "    cosine_scores = util.pytorch_cos_sim(query_embedd, embeddings)\n",
    "    top5_matches = torch.argsort(cosine_scores, dim=-1, descending=True).tolist()[0][1:6]\n",
    "    return top5_matches\n",
    "\n",
    "id = 'quantum'\n",
    "#query_show_des = papers.loc[netflix_data['show_id'] == id]['description'].to_list()[0]\n",
    "recommendded_results = recommend(id)\n",
    "\n",
    "for index in recommendded_results:\n",
    "    st.text(papers.iloc[index,:])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
