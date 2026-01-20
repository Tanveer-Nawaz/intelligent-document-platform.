from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from api.routes import router
import os
from config.settings import UPLOAD_DIR

app = FastAPI(title="Intelligent Document Understanding Platform")

os.makedirs(UPLOAD_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(router)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
