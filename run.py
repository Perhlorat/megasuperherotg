from tornado import ioloop
from tornado import web

from handlers.index_handler import MainHandler


def make_app():
    return web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    ioloop.IOLoop.current().start()
