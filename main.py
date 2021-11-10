from sanic import Sanic
from importlib import import_module
from os import listdir

app = Sanic("hatenabot")

@app.listener("before_server_start")
async def setup(app, loop):
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
