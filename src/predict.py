import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

model = joblib.load("src/ml_models/best_model.pkl")


# Define a Pydantic model for the input features
class InputData(BaseModel):
    Gender: str
    EthnicGroup: str
    ParentEduc: str
    LunchType: str
    TestPrep: str
    ParentMaritalStatus: str
    PracticeSport: str
    IsFirstChild: str
    NrSiblings: float
    TransportMeans: str
    WklyStudyHours: str


app = FastAPI()


# Define a route for making predictions
@app.post("/predict/")
def predict(data: InputData):
    # Convert the input data into a DataFrame with named columns
    # Convert the input data into a DataFrame with lowercase column names
    features = pd.DataFrame(
        {
            "gender": [data.Gender],
            "ethnicgroup": [data.EthnicGroup],
            "parenteduc": [data.ParentEduc],
            "lunchtype": [data.LunchType],
            "testprep": [data.TestPrep],
            "parentmaritalstatus": [data.ParentMaritalStatus],
            "practicesport": [data.PracticeSport],
            "isfirstchild": [data.IsFirstChild],
            "nrsiblings": [data.NrSiblings],
            "transportmeans": [data.TransportMeans],
            "wklystudyhours": [data.WklyStudyHours],
        }
    )

    # Perform the prediction using the loaded model
    prediction = model.predict(features)

    # Return the prediction as a result
    return {"prediction": prediction[0]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
