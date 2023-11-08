import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

model = joblib.load("src/ml_models/best_model.pkl")


# Define a Pydantic model for the input features
class InputData(BaseModel):
    gender: str
    ethnicgroup: str
    parenteduc: str
    lunchtype: str
    testprep: str
    parentmaritalstatus: str
    practicesport: str
    isfirstchild: str
    nrsiblings: float
    transportmeans: str
    wklystudyhours: str

class Response(BaseModel):
    prediction: float

app = FastAPI()


# Define a route for making predictions
@app.post("/predict/")
def predict(data: InputData):
    # Convert the input data into a DataFrame with named columns
    # Convert the input data into a DataFrame with lowercase column names
    features = pd.DataFrame(
        {
            "gender": [data.gender],
            "ethnicgroup": [data.ethnicgroup],
            "parenteduc": [data.parenteduc],
            "lunchtype": [data.lunchtype],
            "testprep": [data.testprep],
            "parentmaritalstatus": [data.parentmaritalstatus],
            "practicesport": [data.practicesport],
            "isfirstchild": [data.isfirstchild],
            "nrsiblings": [data.nrsiblings],
            "transportmeans": [data.transportmeans],
            "wklystudyhours": [data.wklystudyhours],
        }
    )

    # Perform the prediction using the loaded model
    prediction = model.predict(features)

    # Return the prediction as a result
    return Response(prediction=prediction[0])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
