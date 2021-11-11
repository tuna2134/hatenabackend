from sanic import Sanic
from importlib import import_module
from os import listdir
from jinja2 import Environment, FileSystemLoader
from flask_misaka import Misaka
import aiomysql
from sanic.response import html
from os import getenv

app = Sanic("hatenabot")
app.static('/static', './static')


@app.listener("before_server_start")
async def setup(app, loop):
    app.ctx.env = Environment(loader=FileSystemLoader('./templates/', encoding='utf8'), enable_async=True)
    app.ctx.env.filters.setdefault("markdown", Misaka(autolink=True))
    async def template(tpl, **kwargs):
        template = app.ctx.env.get_template(tpl)
        return html(await template.render_async(kwargs))
    app.ctx.template = template
    app.ctx.pool = await aiomysql.create_pool(host="public-cbsv1.net.rikusutep.xyz", user=getenv("db_user"), password=getenv("db_password"), loop=loop, db="b3vad_rtbot", autocommit=True)
    app.ctx.wslist = []
    
async def gateway_send(data: dict):
    for ws in app.ctx.wslist:
        try:
            await ws.send(dumps(data))
        except:
            app.ctx.wslist.remove(ws)
            
app.ctx.gateway_send = gateway_send

for name in listdir("./blueprints"):
    if not name.startswith("_"):
        module = import_module(f"blueprints.{name[:-3]}")
        if hasattr(module, "bp"):
            module.bp.app = app
            app.blueprint(module.bp)
                                                  
if __name__ == "__main__":
    print("start")
    app.run(host = "0.0.0.0", port = 8000)
