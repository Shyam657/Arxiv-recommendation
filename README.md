



<!-- ABOUT THE PROJECT -->
## About The Project
![alt text](https://github.com/Shyam657/Arxiv-recommendation/blob/main/Files/Screenshot.png?raw=true)


This is a Project about a Research Paper Recommender on Arxiv. It recommendes Simmilar Research Paper on Arxiv along with their Pubishing Year, DOI and abstract . 

Motivation:
*  one-day, I was reading a Research-Paper about Quantum-Copmutation on Arxiv, Then I thought of reading simmilar Research paper. 
*  So, I thoght why not make my own recommendation engine about it. Here it is !!

Unfortunately for the space limit on Streamlit and Heroku I can't host my Project there. All the steps are there to reproduce the project.




<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With



* Hugging Face sentence transformer
* pytorch

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Install The Requirements 

 pip install -r requirements.txt


### Running

Run the app.py file


streamlit run app.py

<p align="right">(<a href="#readme-top">back to top</a>)</p>

###Quick Demo



https://user-images.githubusercontent.com/103296209/204440550-d14d2a67-9e93-47f0-b1d5-4320326f09d2.mp4




<p align="right">(<a href="#readme-top">back to top</a>)</p>

###Description

*From Kaggle datasets I downloaded the arxiv Research_paper Dataset from following [link](https://www.kaggle.com/datasets/Cornell-University/arxiv/code)
You can Downloadload the dataset using the following kaggle api command
!kaggle datasets download -d Cornell-University/arxiv


I preprocessed the data and extraced title, DOI,Year,abstract from it.


Using the Hugging Face transformers I encoded the extracted Data with hugging face sentence Transformers.


Used cosine simmilarity with encoded  Search keyword (encoded with the same model of transformers) and original Data.
 
Extracted and Printed the desired information with resulting cosine simmilarity.

