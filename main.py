import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from fingerprint_postgres import FingerprintDBConnection


class FingerprintData(BaseModel):
    fingerprint: str

templates = Jinja2Templates(directory="templates")
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = FingerprintDBConnection()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    headers = {"Access-Control-Allow-Private-Network": "true"}
    return templates.TemplateResponse("home.html", {"request": request}, headers=headers)


@app.post("/fingerprint")
async def say_hello(data: FingerprintData):
    print(data.fingerprint)
    db.save_raw(data.fingerprint)
    return ""

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8080, log_level="info", reload=False)
