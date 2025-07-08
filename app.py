from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model and vectorizer
with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    if request.method == "POST":
        news = request.form["news"]
        if news.strip() != "":
            vect_news = vectorizer.transform([news])
            pred = model.predict(vect_news)[0]
            prediction = "REAL" if pred == 1 else "FAKE"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)