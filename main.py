from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request

app = FastAPI()

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
controls = {
    "power": (
        ("shutdown", "シャットダウン"),
        ("restart", "再起動"),
        ("sleep", "スリープ"),
        ("lock", "ロック"),
        ("signout", "サインアウト"),
    ),
    "clipboard": (
        ("to_pc", "PCへ送信"),
        ("to_device", "端末へ送信"),
    )
}

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "controls": controls
        }
    )


@app.post("/power/shutdown")
async def power_shutdown(request: Request):
    print(request.url)

@app.post("/power/restart")
async def power_sleep(request: Request):
    print(request.url)

@app.post("/power/sleep")
async def power_sleep(request: Request):
    print(request.url)

@app.post("/power/lock")
async def power_sleep(request: Request):
    print(request.url)

@app.post("/power/signout")
async def power_sleep(request: Request):
    print(request.url)

@app.post("/clipboard/to_pc")
async def clipboard_to_pc(request: Request):
    print(request.url)

@app.post("/clipboard/to_device")
async def clipboard_to_device(request: Request):
    print(request.url)
