# Project_WoC_7.0_Fake_Review_Detection

## Checkpoint 1

Firstly, I uploaded the dataset to my GitHub repository. The libraries used for this task include NumPy, Pandas, re, NLTK, scikit-learn, and Google Colab. I then used the raw GitHub link of the dataset to read it as a URL with the Pandas library. To get an initial understanding of the data, I used df.sample() to preview a few rows. I checked for missing values using df.isnull().sum() and found that there were no missing values in the dataset.

Next, I explored the data further by examining its shape and the number of unique reviews. I removed all duplicate reviews from the dataset. I then used the re library to eliminate all punctuation, special characters, and numbers. Afterward, I tokenized the reviews into lists of words and removed all stopwords using the NLTK library. Additionally, I lemmatized the reviews using NLTK to reduce words to their base forms.

I then used the TF-IDF Vectorizer from scikit-learn to convert the reviews into a matrix of features. Finally, I saved both the preprocessed dataset and the resulting matrix into CSV files and downloaded them.
