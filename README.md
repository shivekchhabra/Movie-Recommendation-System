## What does this repository contain?
This repository contains a code of a movie recommendation system deployed in the form of a web application using streamlit.

## How to use this repository?
Clone
Install requirements by doing pip install -r requirements.txt
Run:
	streamlit run runme.py

## Notes:
Here we have built a content-based recommendation system using tf-idf and cosine similarities.

Recommendation System

Recommending movies, books, other products to the users. This can be done by a variety of techniques.

1- Average Weighted Values:

Dataset-  
https://www.kaggle.com/tmdb/tmdb-movie-metadata

 

After this, you can take popularity into account too and give it 50% importance (after normalizing the data)
This will give u better results.


There are 4 types of recommendation systems:
1.	Content Based Filtering – On movie type
2.	Collaborative Filtering- On similar people purchase
3.	Hybrid (mix of 1,2)
4.	Demographic Filtering- They offer generalized recommendations to every user, based on movie popularity and/or genre. The System recommends the same movies to users with similar demographic features. Since each user is different , this approach is considered to be too simple. The basic idea behind this system is that movies that are more popular and critically acclaimed will have a higher probability of being liked by the average audience.

•	Content Based Filtering- They suggest similar items based on a particular item. This system uses item metadata, such as genre, director, description, actors, etc. for movies, to make these recommendations. The general idea behind these recommender systems is that if a person liked a particular item, he or she will also like an item that is similar to it.
•	Collaborative Filtering- This system matches persons with similar interests and provides recommendations based on this matching. Collaborative filters do not require item metadata like its content-based counterparts.



Content Based:
Based on genres

Collaborative:
Based on viewer rating and viewer profiles



For content based filtering, its important to vectorize words in a sentence. For this we use  TF-IDF

Term Frequency-Inverse Document Frequency (TF-IDF)

term frequency is the relative frequency of a word in a document and is given as (term instances/total instances). Inverse Document Frequency is the relative count of documents containing the term is given as log(number of documents/documents with term) The overall importance of each word to the documents in which they appear is equal to TF * IDF

 



After converting the words into vectors, we need to find the cosine similarity between them.

Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.
When plotted on a multi-dimensional space, where each dimension corresponds to a word in the document, the cosine similarity captures the orientation (the angle) of the documents and not the magnitude.


 
#### A big thanks to Krish Naik and Kaggle for helping me learn this.
