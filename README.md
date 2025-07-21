# Fake Review Detection (Amazon.in)

A Flask-based web app that detects **fake reviews** from **Amazon product pages** using a **Support Vector Machine (SVM)** model. It scrapes customer reviews using Selenium, analyzes them using NLP techniques, and highlights genuine (`OR`) vs fake (`CG`) reviews.

---

## Demo

> ![Demo Screenshot](demo-screenshot.png)

---

## Features

* **ML-Powered**: Detects fake vs genuine reviews using an SVM model.
* **Web Scraper**: Extracts reviews from Amazon product URLs with Selenium.
* **Text Cleaning**: Uses NLTK and `string` for preprocessing.
* **Clean Interface**: Built with HTML and CSS, integrated with Flask templates.

---

## Requirements

* Python 3.8+
* Google Chrome
* ChromeDriver (automatically managed by `webdriver-manager`)

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
├── app.py                 # Flask application
├── models/
│   └── svm.pkl            # Pre-trained SVM model
├── scraper/
│   └── reviews.py         # Review scraping logic
├── templates/
│   ├── index.html         # Input form
│   └── result.html        # Results display
├── static/
│   └── style.css          # Basic styling
├── requirements.txt
└── README.md
```

---

## Usage

### 1. Set up Virtual Environment (Optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate    # Windows
# OR
source venv/bin/activate # Linux/Mac
```

### 2. Install NLTK Data (only while running the app for the first time)

```bash
python
>>> import nltk
>>> nltk.download('stopwords')
>>> exit()
```

### 3. Run the Flask App

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

---

## Example

Paste this into the form:

```
https://www.amazon.in/dp/B0CHX1W1XY
```

The app will:

* Scrape reviews
* Classify each as **Genuine** (green) or **Fake** (red)
* Show the results with visual indicators

---

## ⚠️ Disclaimer

This tool is a prototype and may not perfectly classify all reviews. It’s trained on a specific dataset provided by @MSTC-DAIICT and doesn’t account for all linguistic tricks used in real-world fake reviews.

---

## Acknowledgments

* [Flask](https://flask.palletsprojects.com/)
* [Selenium](https://selenium.dev/)
* [NLTK](https://www.nltk.org/)
* [scikit-learn](https://scikit-learn.org/)
