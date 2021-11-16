from sanic import Blueprint
from ujson import dumps, loads
from os import getenv

bp = Blueprint("gateway")

@bp.websocket("/gateway")
async def gateway(request, ws):
    await ws.send(dumps({
        "t": "hello"
    }))
    while True:
        data = loads(await ws.recv())
        if data["t"] == "LOGIN":
            if data["d"]["token"] == getenv("gateway_password"):
                bp.app.ctx.wslist.append(ws)
                await ws.send(dumps({
                    "t": "LOGIN"
                }))
        else:
            await bp.dispatch(data["t"], data["d"])
