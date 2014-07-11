# external scripts
import flask
import yaml
import flask.ext.scss

app = flask.Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object(__name__)
for key, value in yaml.load(file('CONFIG.yaml','r')).items():
    app.config[key] = value

@app.route('/')
@app.route('/index')
def index():
    page_desc = ''
    page_title = ''
    return flask.render_template('views/index.html', page_title=page_title, page_desc=page_desc)

@app.route('/about')
def about():
    page_desc = ''
    page_title = ''
    return flask.render_template('views/index.html', page_title=page_title, page_desc=page_desc)

@app.route('/contact')
def contact():
    page_desc = ''
    page_title = ''
    return flask.render_template('views/index.html', page_title=page_title, page_desc=page_desc)

@app.route('/profile')
def profile():
    page_desc = ''
    page_title = ''
    return flask.render_template('views/index.html', page_title=page_title, page_desc=page_desc)

@app.route('/static/<path:filename>') 
def base_static(filename): 
    return flask.send_from_directory(app.root_path + '/static/', filename)

if __name__ == '__main__':
    app.config['DEBUG'] = True
    flask.ext.scss.Scss(app)
    app.run()