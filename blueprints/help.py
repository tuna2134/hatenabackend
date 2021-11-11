from sanic import Blueprint
from sanic.response import json
from ujson import loads

bp = Blueprint("help")

@bp.route("/help")
async def help_show(request):
    return await bp.app.ctx.template("help.html", data = data)

@bp.route("/api/help", methods = ["POST"])
async def help_setting(request):
    data = request.json
    return json({
        "status": 400,
        "message": "success"
    })
