from sanic import Sanic
from importlib import import_module
from os import listdir
from jinja2 import Environment, FileSystemLoader
from flask_misaka import Misaka
import aiomysql
from sanic.response import html

app = Sanic("hatenabot")
app.static('/static', './static')


@app.listener("before_server_start")
async def setup(app, loop):
    app.ctx.env = Environment(loader=FileSystemLoader('./templates/', encoding='utf8'), enable_async=True)
    app.ctx.env.filters.setdefault("markdown", Misaka(autolink=True))
    async def template(tpl, **kwargs):
        template = env.get_template(tpl)
        return html(await template.render_async(kwargs))
    app.ctx.template = template
    app.ctx.pool = await aiomysql.create_pool(host="public-cbsv1.net.rikusutep.xyz", user="dms", password="dms", loop=loop, db="b3vad_rtbot", autocommit=True)

for name in listdir("./blueprints"):
    if not name.startswith("_"):
        module = import_module(f"blueprints.{name[:-3]}")
        if hasattr(module, "bp"):
            module.bp.app = app
            app.blueprint(module.bp)
                                                  
if __name__ == "__main__":
    print("start")
    app.run(host = "0.0.0.0", port = 8000)
