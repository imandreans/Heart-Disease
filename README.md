# Overview
  ## Data
  This dataset comprises 1025 medical records of heart disease, containing a total of 14 columns, which are 13 features and 1 class variable. Further information about the data can be accessed on the citation.
  ![image](https://github.com/imandreans/Heart-Disease-Prediction/assets/69078720/13f5667e-9301-494d-a07c-bd96e1c7a6ff)


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

![image](https://github.com/imandreans/Heart-Disease-Prediction/assets/69078720/93e9f0e9-9d97-4877-b63b-7ce4234eb740)

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

![image](https://github.com/imandreans/Heart-Disease-Prediction/assets/69078720/78ee8d59-14ea-4dd1-bfbb-37d0e50b266d)

# Citation
Janosi,Andras, Steinbrunn,William, Pfisterer,Matthias, and Detrano,Robert. (1988). Heart Disease. UCI Machine Learning Repository. https://doi.org/10.24432/C52P4X.
