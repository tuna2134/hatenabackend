from sanic import Blueprint

bp = Blueprint

@bp.route("/api/help", methods = ["POST"])
async def help_setting(request):
    bp.app.ctx.help = request.json
