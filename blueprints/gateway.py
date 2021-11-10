from sanic import Blueprint
from ujson import dumps, loads

bp = Blueprint("gateway")

@bp.websocket("/gateway")
async def gateway(request, ws):
    await ws.send(dumps({
        "t": "hello"
    }))
    while True:
        data = loads(await ws.recv())
        if data["t"] == "LOGIN":
            if data["token"] == "questiongateway":
                bp.app.wslist.append(ws)
                await ws.send(dumps({
                    "t": "LOGIN"
                }))
