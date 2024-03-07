from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from starlette.websockets import WebSocket

from src.client.configs import RESOURCES

router = APIRouter()

with open(RESOURCES / "html" / "chat.html", encoding="utf-8") as f:
    chat_html = f.read()


@router.get("/")
async def get():
    return HTMLResponse(chat_html)


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message: {data}")
