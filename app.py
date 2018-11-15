from flask import Flask, render_template, request, send_file, redirect
from os import walk, path
import json
import os

app = Flask(__name__)
app.debug = True

ParentDirectory = ["/Users","/Users/"]

def file_node(fpath):
    return {
        'name': path.basename(fpath),
        'type': 'file',
        'path': fpath
    }

def folder_node(fpath):
    return {
        'name': path.basename(fpath),
        'type': 'folder',
        'path': fpath
    }

def path_to_json(rootdir):
    root, folders, files = walk(rootdir).__next__()
    data = [folder_node(path.sep.join([root,folder])) for folder in folders]
    data += [file_node(path.sep.join([root,file])) for file in files]
    data += [{'path': rootdir}]
    js = json.dumps(data)
    return js

@app.route('/index')
def index():
    curdir = request.args['d']
    if not (curdir in ParentDirectory) and (os.path.isdir(curdir)):
        return render_template('index.html',json = path_to_json(curdir))
    else:
        return render_template('404.html')

@app.route("/create")
def create():
    curdir = request.args['d']
    if(not os.path.isdir(curdir)):
        os.makedirs(curdir)
    if not (curdir in ParentDirectory) and (os.path.isdir(curdir)):
        return redirect('/index?d='+os.path.dirname(curdir))
    else:
        return render_template('404.html')

@app.route('/delete')
def delete():
    curdir = request.args['d']
    if(os.path.isdir(curdir)):
        os.removedirs(curdir)
    if not (curdir in ParentDirectory):
        return redirect('/index?d='+os.path.dirname(curdir))
    else:
        return render_template('404.html')

@app.route('/download', methods=['GET'])
def download():
    curdir = request.args['d']
    if not (curdir in ParentDirectory):
        return send_file(curdir, as_attachment=True, attachment_filename=curdir.rsplit('/', 1)[-1])
    else:
        return render_template('404.html')

if __name__ == '__main__':
    app.run()
