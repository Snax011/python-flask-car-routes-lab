from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route('/')
def index():
    '''Welcome message for the car company homepage'''
    return 'Welcome to Flatiron Cars'


@app.route('/<model>')
def model_route(model):
    '''Confirms whether the requested car model is in our fleet'''
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    return f'No models called {model} exists in our catalog'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
