# backend/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import random
import time

app = FastAPI()

# React에서 요청을 허용하기 위해 CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발 중에는 * 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    time.sleep(3)
    # 여기서 나중에 ML 모델로 추론 가능
    danger_score = round(random.uniform(0.3, 0.9), 2)
    return {"danger_score": danger_score}
