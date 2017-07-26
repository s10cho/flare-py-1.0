from flask import Flask
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from flare.Config import Config
from flare.FlareApi import FlareApi
from flare.FlareView import FlareView

"""// Define //"""
app = Flask(__name__, static_folder='view', static_url_path='', template_folder='view/html')
app.debug = True
config = Config()
flareApi = FlareApi()


"""// Router //"""
"""<--- API --->"""
app.add_url_rule('/api/<command>/<option>', '', flareApi.sample)
app.add_url_rule('/api/save/<command>', '', flareApi.sample)
app.add_url_rule('/api/docker/<command>', '', flareApi.sample)
app.add_url_rule('/api/test/<testId>', '', flareApi.sample)
app.add_url_rule('/api/gatling/<command>', '', flareApi.sample)
app.add_url_rule('/api/status/<command>', '', flareApi.sample)
app.add_url_rule('/api/report/<command>', '', flareApi.sample)
"""<--- HTML --->"""
app.add_url_rule('/', view_func=FlareView.as_view('index', template_name='index.html'))


"""// Main //"""
if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(config.get('SERVER', 'PORT'))
    IOLoop.instance().start()