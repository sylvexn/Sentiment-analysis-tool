from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
from app.model import predict_emotion

app = FastAPI(title="Face Sentiment API")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    emotion = predict_emotion(image)
    return {"emotion": emotion}
