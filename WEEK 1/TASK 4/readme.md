# Boston Housing Price Prediction from Scratch

## Project Description
This project focuses on predicting house prices using the Boston Housing Dataset. We have implemented three machine learning algorithms **from scratch** without relying on any ML libraries:

- Linear Regression
- Random Forest
- XGBoost

The goal is to deeply understand how these algorithms work internally by building them manually.

## Dataset
- The dataset contains 506 samples with 13 features describing different attributes of houses.
- The target variable is the median house price (`MEDV`).
- The dataset was obtained from Kaggle or can be loaded via scikit-learn.

## Algorithms Implemented

### 1. Linear Regression
- Implemented using both Gradient Descent and Normal Equation methods.
- The loss function used is Mean Squared Error (MSE).

### 2. Random Forest
- Built multiple decision trees using feature bagging.
- Each tree performs recursive binary splits on randomly selected features.
- Final prediction is the average of all trees’ predictions.

### 3. XGBoost
- Implemented gradient boosting from scratch.
- Each iteration fits a new tree to the residual errors from previous predictions.
- Parameters like learning rate and tree depth are manually tuned.

## Evaluation Metrics
- **RMSE (Root Mean Squared Error):** Measures the average prediction error magnitude.
- **R² Score:** Indicates the proportion of variance explained by the model.

## How to Run

1. Setup a Python environment
2. Install required packages:

###  Clone the repository
```bash
git clone https://github.com/SabeehUrRehmanKhan/Internship-tasks
cd Internship-tasks
cd "WEEK 1/TASK 3"

## 📁 Download only the `TASK 4` folder

You can browse or download only this folder:
👉 [View Folder on GitHub](https://github.com/SabeehUrRehmanKhan/Internship-tasks/tree/main/WEEK%201/TASK%204)

```


