# Overview
  ## Data
  This dataset comprises 1025 medical records of heart disease, containing 14 columns, which are 13 features and 1 class variable.

  ## Objective
  - to develop a machine learning model to predict heart disease
  - to identify the most influential features that cause heart disease.
# Exploratory Data Analysis
Exploratory data analysis (EDA) is done by looking for missing values, duplicates, outliers, and other anomalies in the dataset. In the EDA process, features with the highest correlation toward the class variable are chosen in the modeling process. Run `eda.ipynb` to perform exploratory analysis.

# Modeling
The four models are trained, as follows:
- Logistic Regression
- Random Forest
- Decision Tree
- Multi-Layer Perceptron

These models are tuned using GridSearchCV to find the best accuracy score and determine their optimal parameters. The models are then evaluated based on their ROC-AUC scores to assess their ability to distinguish between classes. The model with the highest ROC-AUC score is selected for deployment in Streamlit.

# Result
## Most influential features
The most influential features in the dataset that cause heart disease are age,' 'sex,' 'cp,' 'thalach,' 'exang,' 'oldpeak,' 'slope,' 'ca,' and 'thal'.

![corr_target](https://github.com/imandreans/Heart-Disease-Prediction/assets/69078720/d00ac2b8-3581-460a-bf48-73be93fb0843)


Description of correlation:
1. age: -0.23 (Moderate)
2. sex: -0.28 (Moderate)
3. cp: 0.43 (Strong)
4. trestbps: -0.14 (Weak)
5. chol: -0.1 (weak)
6. fbs: -0.041 (weak)
7. restecg: 0.13 (weak)
8. thalach: 0.42 (Strong)
9. exang: -0.44 (Strong)
10. oldpeak: -0.44 (Strong)
11. slope: 0.35 (Strong)
12. ca: -0.38 (Strong)
13. thal: -0.34 (Strong)


## Chosen model
Random Forest has the highest ROC-AUC score, with its parameters are 'criterion': 'entropy', 'max_depth': 10, 'n_estimators': 200.

![ROC-AUC](https://github.com/imandreans/Heart-Disease-Prediction/assets/69078720/3d96ef6c-7fa8-4046-8eee-26181d6c807f)
