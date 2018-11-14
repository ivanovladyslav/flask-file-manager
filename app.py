from flask import Flask, render_template, request, send_file
from os import walk, path
import json
import os

app = Flask(__name__)
app.debug = True

ParentDirectory = "/Users"

def file_node(fpath):
    return {
        'name': path.basename(fpath),
        'type': 'file',
        'path': fpath
    }

def folder_node(fpath):
    fpath = fpath.rsplit(ParentDirectory,10)[1]
    return {
        'name': path.basename(fpath),
        'type': 'folder',
        'path': fpath
    }

def path_to_json(rootdir):
    root, folders, files = walk(rootdir).__next__()
    data = [folder_node(path.sep.join([root,folder])) for folder in folders]
    data += [file_node(path.sep.join([root,file])) for file in files]
    js = json.dumps(data)
    return js

@app.route('/index')
def index():
    curdir = request.args['d']
    return render_template('index.html',json = path_to_json(ParentDirectory+curdir))

@app.route("/create")
def create():
    curdir = request.args['d']
    os.makedirs(ParentDirectory+curdir+'/'+request.args['name'])
    return render_template('index.html',json = path_to_json(ParentDirectory+curdir))

@app.route('/delete')
def delete():
    curdir = request.args['d']
    os.removedirs(ParentDirectory+curdir+'/'+request.args['name'])
    return render_template('index.html',json = path_to_json(ParentDirectory+curdir))

@app.route('/download', methods=['GET'])
def download():
    curdir = request.args['d']
    return send_file(ParentDirectory+curdir, as_attachment=True, attachment_filename=curdir.rsplit('/', 1)[-1])

if __name__ == '__main__':
    app.run()
