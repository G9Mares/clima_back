from fastapi import FastAPI
from features.clima import routes as clima_router
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from mangum import Mangum

load_dotenv()

VERSION = os.getenv("VERSION")

app = FastAPI()
app.include_router(router=clima_router.router)

handler = Mangum(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes usar ["*"] para permitir todos en desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def check_healt():
    return {"service_status":"ok", "version_api":VERSION}