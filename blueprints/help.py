from sanic import Blueprint

bp = Blueprint("help")

@bp.route("/api/help", methods = ["POST"])
async def help_setting(request):
    bp.app.ctx.help = request.json
