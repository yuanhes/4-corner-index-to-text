from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from translate_4CI import translate_number_to_chinese

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/translate_4CI", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/translate_4CI", response_class=HTMLResponse)
async def post_form(request: Request, number_input: str = Form(None)):
    if not number_input:
        number_input = ""  # or you can set a default message
    translated_text = translate_number_to_chinese(number_input)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "translated_text": translated_text,
        "number_input": number_input  # Pass the input number back
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

