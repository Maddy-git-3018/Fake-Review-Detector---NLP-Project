import string
from nltk.corpus import stopwords

def preprocess_text(text):
    text = text.lower()
    return ''.join(c for c in text if c not in string.punctuation)

def predict_reviews(model, review_list):
    return model.predict(review_list)

def convertmyTxt(rv):
    np = [c for c in rv if c not in string.punctuation]
    np = ''.join(np)
    return [w for w in np.split() if w.lower() not in stopwords.words('english')]
