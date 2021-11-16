from sanic import Blueprint
from sanic.response import redirect

bp = Blueprint("main")

@bp.route("/")
async def main(request):
    return await bp.app.ctx.template("index.html")

@bp.route("/favicon.ico")
async def favicon(request):
    return redirect("/static/image/favicon.ico")
