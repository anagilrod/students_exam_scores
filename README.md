
# Students Exam Scores README

## Description of the Problem

In this project, the primary objective is to **predict** the math test scores (**MathScore**) of students at a fictional public school based on various personal and socio-economic factors. The dataset used for this project includes scores from three test scores of students (MathScore, ReadingScore, and WritingScore) along with a variety of demographic and background information that may have interaction effects on the MathScore.

### Dataset Overview

The dataset is composed of the following columns:

- **Gender**: Gender of the student (male/female)
- **EthnicGroup**: Ethnic group of the student (group A to E)
- **ParentEduc**: Parent(s) education background (ranging from some_highschool to master's degree)
- **LunchType**: School lunch type (standard or free/reduced)
- **TestPrep**: Test preparation course followed (completed or none)
- **ParentMaritalStatus**: Parent(s) marital status (married/single/widowed/divorced)
- **PracticeSport**: How often the student practices sports (never/sometimes/regularly)
- **IsFirstChild**: Whether the child is the first child in the family or not (yes/no)
- **NrSiblings**: Number of siblings the student has (ranging from 0 to 7)
- **TransportMeans**: Means of transport to school (schoolbus/private)
- **WklyStudyHours**: Weekly self-study hours (less than 5 hours; between 5 and 10 hours; more than 10 hours)
- **MathScore**: The **target column**, representing the math test score (0-100).

https://www.kaggle.com/datasets/desalegngeb/students-exam-scores/

### Data Preprocessing

To tackle the problem of predicting MathScore, we first examined the dataset and identified that **ReadingScore and WritingScore** were highly correlated with MathScore. As a result, we decided to focus our efforts on predicting MathScore exclusively, removing the other two columns from the dataset.

Additionally, data preprocessing steps were performed to handle missing values, encode categorical variables, and scale numerical features.

### Objective

The main goal of this project is to build a predictive model that can accurately **predict a student's MathScore** based on the provided features. By doing so, we aim to identify the key factors that influence a student's math performance and provide valuable insights to improve educational strategies.

In the subsequent sections of this README, we will describe the steps taken to analyze the data, generate the predictive model, and deploy it for real-time predictions. Additionally, we will provide instructions on how to use the API to make predictions.

For a detailed overview of the data analysis, model development, deployment, and results, please refer to the corresponding sections in this README and the project's code and documentation.


## Data Analysis (EDA)
The dataset used for this project includes customer information, subscription plan details, and historical interaction logs. Before building the model, we conducted an exploratory data analysis (EDA) to gain insights into the data. Key findings from the EDA are as follows:
- See notebook 01_exploring_data_and_test_training.ipynb
- See pdf with EDA

## Model Generation
We built a machine learning model to predict MathScore (see more in 02_model_training.ipynb)

## Deployment
The model is deployed using a FASTAPI.

To deploy the model locally, follow these steps:
1. Run the FASTAPI app using the command `uvicorn src.predict:app --host 0.0.0.0 --port 8000`.
2. Access the API at `http://localhost:8000/docs` to make predictions.

## Usage of the API
Send a POST request to the endpoint `/predict`. Include the customer data in the request body in JSON format. Here's an example request:

```json
{
  "Gender": "string",
  "EthnicGroup": "string",
  "ParentEduc": "string",
  "LunchType": "string",
  "TestPrep": "string",
  "ParentMaritalStatus": "string",
  "PracticeSport": "string",
  "IsFirstChild": "string",
  "NrSiblings": 10,
  "TransportMeans": "string",
  "WklyStudyHours": "string"
}