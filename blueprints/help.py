from sanic import Blueprint
from sanic.response import json
from ujson import loads

bp = Blueprint("help")

@bp.route("/help")
async def help_show(request):
    return await bp.app.ctx.template("help.html", data = data)

@bp.route("/help/<category>")
async def help_category(request, category):
    return await bp.app.ctx.template("help_category.html", category=category, data=data[category])

@bp.route("/api/help", methods = ["POST"])
async def help_setting(request):
    global data
    data = request.json
    return json({
        "status": 400,
        "message": "success"
    })
