import string
from nltk.corpus import stopwords
from flask import Flask, render_template, request
import joblib
from scraper.reviews import get_reviews
from utils import preprocess_text, predict_reviews
from utils import convertmyTxt  # Required so joblib can find it

app = Flask(__name__)

models = {
    'Logistic Regression': joblib.load('models/logreg.pkl'),
    'Random Forest': joblib.load('models/randomforest.pkl'),
    'SVM': joblib.load('models/svm.pkl')
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['product_url']
        model = models['SVM']

        try:
            raw_reviews = get_reviews(url)
            clean_reviews = [preprocess_text(r) for r in raw_reviews]
            predictions = predict_reviews(model, clean_reviews)
            results = list(zip(raw_reviews, predictions))
            return render_template('results.html', results=results)
        except Exception as e:
            return render_template('index.html', models=models.keys(), error=str(e))

    return render_template('index.html', models=models.keys())
    
if __name__ == '__main__':
    app.run(debug=True)
