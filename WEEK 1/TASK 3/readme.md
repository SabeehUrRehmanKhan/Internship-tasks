# 🕵️‍♂️ Task 3: Fraud Detection System

This project implements a **Fraud Detection System** using the Credit Card Fraud Detection dataset. It uses machine learning models (Random Forest and Gradient Boosting) to predict whether a given transaction is fraudulent or legitimate.

---

## 📁 Dataset

- **File Used**: `creditcard.csv`
- **Source**: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- The dataset is highly **imbalanced**, with only ~0.17% of transactions being fraud.

---

## 🔄 Data Preprocessing

1. **Feature Scaling**: No scaling needed — most features are already PCA-transformed.
2. **Handling Imbalance**:
   - Applied **SMOTE (Synthetic Minority Oversampling Technique)** to balance fraud and legitimate classes.
   - This ensures the model doesn't get biased toward predicting only legitimate transactions.

---

## 🤖 Models Implemented

### 1. Random Forest Classifier
- A collection of decision trees trained on bootstrapped samples.
- Provides high accuracy and feature importance.

### 2. Gradient Boosting Classifier
- Builds trees **sequentially**, each learning from the errors of the previous one.
- Generally better at handling complex data.

---

## 📊 Evaluation Metrics

The models are evaluated using:

- **Precision**: Accuracy for predicted frauds
- **Recall**: How many real frauds are detected
- **F1-Score**: Harmonic mean of precision and recall
- **Confusion Matrix**: Visual breakdown of TP, FP, FN, TN

---

## 🧪 Testing Interface

A simple **command-line interface** is available to manually test the model with custom inputs.

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/SabeehUrRehmanKhan/Internship-tasks
cd Internship-tasks
cd "WEEK 1/TASK 3"

## 📁 Download only the `TASK 3` folder

You can browse or download only this folder:
👉 [View Folder on GitHub](https://github.com/SabeehUrRehmanKhan/Internship-tasks/tree/main/WEEK%201/TASK%203)

```

2. **Manage Resources**
- Setup a python virtual environment (optinal).
- Install required libraries.
- Run the task. 