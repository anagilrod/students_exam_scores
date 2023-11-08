
<span style="color: #60B5FC; font-weight: bold; font-size: 24px;">Students Exam Scores README</span> 

<span style="color: #AC1555; font-weight: bold; font-size: 18px;">Description of the Problem</span> 

In this project, the primary objective is to **predict** the math test scores (**MathScore**) of students at a fictional public school based on various personal and socio-economic factors. The dataset used for this project includes scores from three test scores of students (MathScore, ReadingScore, and WritingScore) along with a variety of demographic and background information that may have interaction effects on the MathScore.

<span style="color: #AC1555; font-weight: bold; font-size: 18px;">Dataset Overview</span> 

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

<span style="color: #AC1555; font-weight: bold; font-size: 18px;">Data Preprocessing</span> 

To tackle the problem of predicting MathScore, we first examined the dataset and identified that **ReadingScore and WritingScore** were highly correlated with MathScore. As a result, we decided to focus our efforts on predicting MathScore exclusively, removing the other two columns from the dataset.

Additionally, data preprocessing steps were performed to handle missing values, encode categorical variables, and scale numerical features.

<span style="color: #AC1555; font-weight: bold; font-size: 18px;">Objective</span> 

The main goal of this project is to build a predictive model that can accurately **predict a student's MathScore** based on the provided features. By doing so, we aim to identify the key factors that influence a student's math performance and provide valuable insights to improve educational strategies.

In the subsequent sections of this README, we will describe the steps taken to analyze the data, generate the predictive model, and deploy it for real-time predictions. Additionally, we will provide instructions on how to use the API to make predictions.

For a detailed overview of the data analysis, model development, deployment, and results, please refer to the corresponding sections in this README and the project's code and documentation.


<span style="color: #AC1555; font-weight: bold; font-size: 18px;">Data Analysis (EDA)</span>

The dataset used for this project includes customer information, subscription plan details, and historical interaction logs. Before building the model, we conducted an exploratory data analysis (EDA) to gain insights into the data. Key findings from the EDA are as follows:
- See notebook 01_exploring_data.ipynb
- See pdf with EDA (/reports/report.html)

<span style="color: #AC1555; font-weight: bold; font-size: 18px;">Model Generation</span> 

We built a machine learning model to predict MathScore (see more in 02_running_different_models and 03_best_model_training)

<span style="color: #AC1555; font-weight: bold; font-size: 18px;">Deployment</span> 

The model is deployed using a FASTAPI.

To deploy the model locally without Docker, follow these steps:
1. Run the FASTAPI app using the command `make app_run`.
2. Access the API at `http://localhost:8000/docs` to make predictions.


To deploy the model locally using Docker, follow these steps:
1. Run the FASTAPI app using the command `make docker_build_run`.
2. Access the API at `http://localhost:8000/docs` to make predictions.


To deploy the model locally using kubernetes, follow these steps:
1. Run the kubernetes cluster using the command `make kubernetes_cluster`.
2. Access the API at `http://localhost:8000/docs` to make predictions.

<span style="color: #AC1555; font-weight: bold; font-size: 18px;">Usage of the API</span> 

Send a POST request to the endpoint `/predict`. Include the customer data in the request body in JSON format. Here's an example request:

```
curl -X 'POST' \
  'http://localhost:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "gender": "female",
  "ethnicgroup": "group A",
  "parenteduc": "some college",
  "lunchtype": "free/reduced",
  "testprep": "none",
  "parentmaritalstatus": "single",
  "practicesport": "never",
  "isfirstchild": "no",
  "nrsiblings": 1.0,
  "transportmeans": "school_bus",
  "wklystudyhours": "> 10"
}'