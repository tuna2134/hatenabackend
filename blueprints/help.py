from sanic import Blueprint
from sanic.response import json

bp = Blueprint("help")

@bp.route("/api/help", methods = ["POST"])
async def help_setting(request):
    bp.app.ctx.help = request.json
    return json({
        "status": 400,
        "message": "success"
    })
