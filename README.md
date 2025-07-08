# Fake_News_Prediction
A simple and interactive web application built with Flask, HTML/CSS, and Machine Learning to classify news articles as Fake or Real using Natural Language Processing (NLP) techniques.
# 📰 Fake News Detection Web App

A machine learning-powered web application that allows users to classify whether a news article is **Fake** or **Real**. Built using Python, Flask, HTML/CSS, and scikit-learn.

---

## 🚀 Features

- ✅ Predict whether a news article is fake or real
- 📊 Trained on real-world news datasets from multiple domains (Politics, Film, World News)
- 🔍 Interactive web UI with a modern lavender-themed aesthetic
- 🧠 Uses TF-IDF vectorization and Logistic Regression model
- 📁 Model and vectorizer saved using `pickle` for deployment
- 🛡️ Cleaned and optimized with `.gitignore` and compressed for GitHub-friendly size

---

## 🧠 Technologies Used

- **Python 3.8+**
- **Flask** – Web framework
- **Scikit-learn** – Machine learning (TF-IDF & Logistic Regression)
- **Pandas / NumPy** – Data manipulation
- **HTML / CSS** – Frontend
- **Jinja2** – Templating in Flask

---

## 📂 Project Structure

```
fake_news_web_app/
│
├── static/
│   ├── style.css               # Lavender-themed UI design
│   └── logo.png                # Web app logo
│
├── templates/
│   └── index.html              # Main frontend page
│
├── model/
│   ├── model.pkl               # Trained logistic regression model
│   └── vectorizer.pkl          # TF-IDF vectorizer
│
├── dataset/
│   └── news_dataset.csv        # Combined dataset of real/fake news (200+ rows)
│
├── app.py                      # Flask app entry point
├── train_model.py              # Script to train and save model & vectorizer
├── requirements.txt            # List of dependencies
└── README.md                   # You are here
```

---

## 🛠️ How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/Maha5343/Fake_News_Prediction.git
cd Fake_News_Prediction
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv myenv
myenv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the Model (Optional if model.pkl exists)
```bash
python train_model.py
```

### 5. Run the App
```bash
python app.py
```

Then visit: [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🧪 Sample Data Sources

The dataset includes real-time scraped news from:
- **Kaggle’s Fake & Real News Dataset**
- **BBC News**
- **Reuters**
- **The Guardian**
- **Entertainment & Political blogs**

### Example CSV Structure:

| title                      | text                          | label   |
|---------------------------|-------------------------------|---------|
| Trump says economy is...  | President Trump spoke on...   | FAKE    |
| NASA launches telescope   | NASA announced the launch...  | REAL    |

---

## 📸 UI Preview

![Preview](static/screenshot.png)

---

## ✨ Future Enhancements

- Add support for URL-based news validation
- Mobile-responsive layout
- Use of deep learning models (e.g., LSTM, BERT)
- Deploy on Heroku or Render

---

## 🤝 Contributing

Pull requests are welcome! If you'd like to add improvements, submit a PR or open an issue.

---

## 📄 License

This project is under the **MIT License** – feel free to use and modify.

---

## 👩‍💻 Author

**Maha Lakshmi**  
[GitHub: @Maha5343](https://github.com/Maha5343)

