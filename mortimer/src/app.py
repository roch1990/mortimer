import asyncio

import aiohttp_jinja2
import jinja2
from aiohttp import web

from config import Config
from src.clients.postgres import Postgres


async def database_client(app):
    app['database'] = await Postgres().connect()
    yield

    await app['database'].wait_close()
    await asyncio.sleep(0.250)


async def make_app(project_root: str) -> web.Application:

    app = web.Application()

    aiohttp_jinja2.setup(
        app=app,
        loader=jinja2.FileSystemLoader('./templates'),
    )

    # Don't use this for production. Use nginx static (for example) instead.
    app.router.add_static(
        prefix=f'/static',
        path=f'{project_root}/static',
    )

    return app