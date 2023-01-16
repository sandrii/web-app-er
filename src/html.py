from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from src.model import sum_digits_math

app = FastAPI()
app.mount("/static",
          StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
          name="static",
)
templates = Jinja2Templates(directory='templates/')


@app.get('/form')
def form_post(request: Request):
    result = 'Type a number'
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post('/form')
def form_post(request: Request, num: int = Form(...)):
    result = sum_digits_math(num)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result, 'num': num})

