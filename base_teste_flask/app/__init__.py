from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/api')
    def hello_world():
        return {'message': 'Hello, World!'}

    return app
