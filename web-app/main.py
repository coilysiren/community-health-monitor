# external scripts
import flask
import yaml

app = flask.Flask(__name__)
app.config.from_object(__name__)
for key, value in yaml.load(file('CONFIG.yaml','r')).items():
    app.config[key] = value

@app.route('/')
def index():
    page_desc = ''
    page_title = ''
    return flask.render_template('views/index.html', page_title=page_title, page_desc=page_desc)

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()