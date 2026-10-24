# End-to-End Iris Machine Learning Capstone Project

## Project Overview
This repository contains a complete end-to-end Machine Learning pipeline built over 4 weeks using the classic Iris dataset loaded using the url directly without using csv or excel sheet , culminating in a fully deployed prediction API.

## Project Workflow
- **Week 1 (Data Preprocessing):** Loaded data, checked for missing values, normalized features, and performed exploratory data analysis (EDA) in `notebooks/Iris_preprocessingTask.ipynb`.
- **Week 2 (Supervised Models):** Trained and evaluated multiple classification models (Logistic Regression, Random Forest Classifier) in `notebooks/task2.ipynb`.
- **Week 3 (Clustering & Evaluation):** Applied K-Means unsupervised clustering, performed cross-validation, and tuned hyperparameters using GridSearchCV in `notebooks/task3.ipynb`.
- **Week 4 (Deployment):** Serialized the best trained model using Joblib (`iris_model.pkl`) and built a production-ready prediction API using FastAPI (`app.py`).

## How to Run Locally
1. Clone or download this repository.
2. Install Joblib using command : `pip install joblib scikit-learn`
3. Install dependencies : `pip install -r requirememts.txt`
4. Copy & Paste the following packages in the requirements.txt file :
          `fastapi`
          `uvicorn`
          `scikit-learn`
          `numpy`
          `joblib`
          `pydantic`
5. Start/Run your FastAPI development server using Uvicorn:
          type in terminal  : `uvicorn app:app --reload`
6. You'll get a link viewed as `http://127.0.0.1:8000` but dont forget to  add `/docs` at the last making it ..
          Link : `http://127.0.0.1:8000/docs`
7. Add values to the variables and click execute .