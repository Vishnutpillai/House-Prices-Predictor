# 🏠 House Price Prediction Using Machine Learning

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Regressor-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📌 Project Overview

This project is an end-to-end Machine Learning solution for predicting residential house prices based on property characteristics such as area, number of bedrooms, bathrooms, parking availability, furnishing status, and location preferences.

The project includes:

* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Machine Learning Model Development
* Hyperparameter Tuning using GridSearchCV
* Model Evaluation and Comparison
* Streamlit Web Application Deployment
* Model Serialization using Joblib

---

## 🎯 Business Problem

Accurately estimating house prices is a critical challenge in the real estate industry.

This project helps:

* Home Buyers estimate property values
* Real Estate Agencies assess pricing trends
* Property Investors evaluate investments
* Housing Market Analysts generate insights

---

## 📊 Dataset Information

### Features Used

| Feature          | Description                    |
| ---------------- | ------------------------------ |
| area             | Area of house in square feet   |
| bedrooms         | Number of bedrooms             |
| bathrooms        | Number of bathrooms            |
| mainroad         | Main road access               |
| guestroom        | Guest room availability        |
| basement         | Basement availability          |
| hotwaterheating  | Hot water heating availability |
| airconditioning  | Air conditioning availability  |
| parking          | Number of parking spaces       |

### Target Variable

| Target |
| ------ |
| price  |

---

## 🔍 Exploratory Data Analysis

The following analyses were performed:

* Dataset Overview
* Missing Value Analysis
* Correlation Analysis
* House Price Distribution
* Feature Relationship Analysis
* Outlier Detection
* Feature Importance Investigation

### Visualizations

* Correlation Heatmap
* Histograms
* Scatter Plots
* Box Plots
* Distribution Plots

---

## 🤖 Machine Learning Models

Three regression algorithms were trained and evaluated.

### 1. Linear Regression

Used as a baseline model.

### 2. Random Forest Regressor

Ensemble learning algorithm based on multiple decision trees.

### 3. XGBoost Regressor

Gradient boosting framework optimized for performance and predictive accuracy.

---

## ⚙️ Hyperparameter Tuning

GridSearchCV was used for hyperparameter optimization.

### Random Forest Parameters

* n_estimators
* max_depth
* min_samples_split
* min_samples_leaf
* max_features

### XGBoost Parameters

* n_estimators
* learning_rate
* max_depth
* subsample
* colsample_bytree

---

## 🏆 Model Evaluation Metrics

The following metrics were used:

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score

Model comparison was performed to select the best-performing model.

---

## 🧠 Machine Learning Pipeline

The project uses a production-ready Scikit-Learn Pipeline.

### Components

* OneHotEncoder
* ColumnTransformer
* Random Forest Regressor
* XGBoost Regressor

Benefits:

* Prevents data leakage
* Consistent preprocessing
* Easier deployment
* Industry-standard workflow

---

## 🚀 Streamlit Web Application

A user-friendly Streamlit application was developed for real-time house price prediction.

### Features

✅ Interactive User Interface

✅ Real-Time Predictions

✅ Categorical Feature Handling

✅ Responsive Layout

✅ Production-Ready Deployment

---

## 📂 Project Structure

```text
House-Price-Prediction/
│
│── House_price_prediction.ipynb
│
├── models/
│   ├── house_price_pipeline.pkl
│   └── feature_columns.pkl
│
├── app.py
├── requirements.txt
├── README.md
├── Housing.csv
│
└── images/
```

## 💾 Model Serialization

The trained model is saved using Joblib.

```python
joblib.dump(model, "Models/house_price_model.pkl")
```

Load model:

```python
model = joblib.load("Models/house_price_model.pkl")
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/House-Price-Prediction.git
```

Move into project directory:

```bash
cd House-Price-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

* Cross Validation Reporting
* SHAP Explainability
* Feature Importance Dashboard
* Docker Deployment
* CI/CD Integration
* Cloud Deployment (AWS/Azure/GCP)

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* Joblib
* Streamlit

---

## 👨‍💻 Author

### Vishnu T Pillai

Aspiring Data Scientist | Machine Learning Enthusiast

### LinkedIn

linkedin.com/in/vishnu-t-pillai

### GitHub

https://github.com/Vishnutpillai

###App Link

https://house-prices-predictor-2026.streamlit.app/

---

## ⭐ If you found this project useful

Please consider giving this repository a star.

It helps others discover the project and supports future development.

⭐ Star the repository if you found it helpful.
