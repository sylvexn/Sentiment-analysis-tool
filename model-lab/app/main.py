from fastapi import FastAPI, File, UploadFile, status
from PIL import Image
import io
from app.model import predict_emotion, is_model_ready

app = FastAPI(title="Face Sentiment API")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    emotion = predict_emotion(image)
    return {"emotion": emotion}

@app.get("/health", status_code=status.HTTP_200_OK)
def get_health():
    if is_model_ready():
        return {"status" : "ok"}
    else:
        return {"status" : "unavailable"}
