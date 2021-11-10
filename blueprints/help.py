from sanic import Blueprint

bp = Blueprint

@bp.post("/api/help")
async def help_setting(request):
    bp.app.ctx.help = request.json
