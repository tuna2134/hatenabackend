from sanic import Sanic
from importlib import import_module

app = Sanic("hatenabot")

for name in listdir("./blueprints"):
    if not name.startswith("_"):
        module = import_module(f"blueprints.{name[:-3]}")
        if hasattr(module, "bp"):
            module.bp.app = app
            app.blueprint(module.bp)
                                                  
if __name__ == "__main__":
    print("start")
    app.run(host = "0.0.0.0", port = 8000)
