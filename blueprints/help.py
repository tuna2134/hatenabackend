from sanic import Blueprint
from sanic.response import json

bp = Blueprint("help")

@bp.route("/help")
async def help_show(request):
    data = bp.app.ctx.help
    return await bp.app.ctx.template("help.html", data = data)

@bp.route("/api/help", methods = ["POST"])
async def help_setting(request):
    bp.app.ctx.help = request.json
    return json({
        "status": 400,
        "message": "success"
    })
