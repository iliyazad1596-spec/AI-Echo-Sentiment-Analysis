# AI Echo - Sentiment Analysis Dashboard

## Project Overview

AI Echo is a Natural Language Processing (NLP) project that analyzes ChatGPT user reviews and classifies them into Positive, Neutral, and Negative sentiments. The project helps understand customer satisfaction, identify common concerns, and provide insights for improving user experience.

---

## Problem Statement

Sentiment analysis is an NLP technique used to determine the sentiment expressed in text. This project analyzes ChatGPT user reviews and predicts sentiment based on the review content.

---

## Business Use Cases

* Customer Feedback Analysis
* Brand Reputation Management
* Feature Enhancement
* Automated Customer Support
* Marketing Strategy Optimization

---

## Technologies Used

* Python
* Pandas
* NumPy
* NLTK
* TextBlob
* Scikit-learn
* Matplotlib
* Streamlit
* Joblib

---

## Project Workflow

### 1. Data Collection

* Loaded ChatGPT reviews dataset from Excel.

### 2. Data Preprocessing

* Removed special characters
* Converted text to lowercase
* Removed stopwords
* Cleaned review text

### 3. Exploratory Data Analysis

* Sentiment Distribution
* Rating Distribution
* Platform Analysis
* Verified vs Non-Verified User Analysis

### 4. NLP Feature Engineering

* Text Cleaning
* TF-IDF Vectorization

### 5. Machine Learning Model

* Logistic Regression

### 6. Model Evaluation

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix

### 7. Deployment

* Streamlit Dashboard

---

## Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 100%  |
| Precision | 100%  |
| Recall    | 100%  |
| F1 Score  | 100%  |

---

## Project Structure

AI_Echo_Sentiment_Analysis

├── app/

│ └── app.py

├── data/

│ ├── raw/

│ └── processed/

├── models/

│ ├── sentiment_model.pkl

│ ├── vectorizer.pkl

│ └── label_encoder.pkl

├── sentiment_analysis.py

├── nlp_preprocessing.py

├── train_model.py

├── save_model.py

├── requirements.txt

└── README.md

---

## Streamlit Dashboard Features

* Review Sentiment Prediction
* Sentiment Distribution Visualization
* Rating Distribution Analysis
* Platform-wise Rating Comparison
* Verified vs Non-Verified User Analysis

---

## Results

The dashboard successfully classifies user reviews and provides visual insights into customer sentiment trends and satisfaction levels.

---

## Future Enhancements

* Word Cloud Visualization
* Topic Modeling
* Deep Learning Models (LSTM/BERT)
* Real-time Sentiment Monitoring
* Cloud Deployment

---

## Author

Iliyaz Ahamed

Data Science Project - GUVI
