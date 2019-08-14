import os
from flask import Flask, escape, render_template, request, flash, redirect, url_for

# os.mkdir('./uploader')

UPLOAD_FOLDER = '/uploader'
ALLOWED_EXTENSIONS = set(['txt', 'png', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.config['UPLOADER_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def main():
    return("<h1>Hello Flask</h1>")

@app.route('/api/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/api/mytemplate/')
@app.route('/api/mytemplate/<name>')
def template_html(name=None):
    return render_template('index.html', name=name)

def allowed_filename(filename):
    return  '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/api/upload', methods=['GET','POST'])
# def upload_file():
#     if request.method == 'POST':


if __name__ == '__main__':

    if os.path.isdir('./uploader'):
        pass
    else:
        os.mkdir('./uploader')
    app.run(debug=True)