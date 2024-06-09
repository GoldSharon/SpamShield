from flask import render_template, Flask, request
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import load
import numpy as np

app = Flask(__name__)

# Load the model and vectorizer
model = load(r"D:\projects\Spam_Ham\models\Spam_Model.joblib")
vectorizer = load(r"D:\projects\Spam_Ham\models\Vectorizer.joblib")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/result/<flag>")
def result(flag):
    flag = flag.lower() == 'true'
    return render_template('predict.html', flag=flag)

@app.route("/submit", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        input_value = request.form.get('Check', '')
        if not input_value:
            return render_template('index.html', error="Input cannot be empty")
        else:
            transformed_input = vectorizer.transform([input_value])
            predicted = model.predict(transformed_input)
            flag = np.array(predicted) == np.array([1])
            return render_template('predict.html', flag=flag)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
