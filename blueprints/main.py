from sanic import Blueprint
from sanic.response import text

bp = Blueprint("main")

@bp.route("/")
async def main(request):
    return await bp.app.ctx.template("index.html")
