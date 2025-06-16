# plugins/web_server.py

from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def home(request):
    return web.Response(text="Bot is running!", status=200)

@routes.get('/ping')
async def ping(request):
    return web.Response(text="Pong!", status=200)

async def web_server():
    app = web.Application()
    app.add_routes(routes)
    return app
