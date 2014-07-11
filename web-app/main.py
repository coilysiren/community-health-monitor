import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    page_desc = ''
    page_title = ''
    return flask.render_template('index.html', page_title=page_title, page_desc=page_desc)

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()