from flask import Flask, render_template, request, send_file
from os import walk, path
import json
import os

app = Flask(__name__)
app.debug = True

def file_node(fpath):
    return {
        'name': path.basename(fpath),
        'type': 'file',
    }

def folder_node(fpath):
    return {
        'name': path.basename(fpath),
        'type': 'folder',
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
    return render_template('index.html',json = path_to_json("/Users"+curdir))

@app.route("/create")
def create():
    curdir = request.args['d']
    os.makedirs(curdir+'/'+request.args['name'])
    return render_template('index.html',json = path_to_json("/Users"+curdir))

@app.route('/delete')
def delete():
    curdir = request.args['d']
    os.removedirs(curdir+'/'+request.args['name'])
    return render_template('index.html',json = path_to_json("/Users"+curdir))

@app.route('/download', methods=['GET'])
def download():
    curdir = request.args['d']
    return send_file("/Users"+curdir, as_attachment=True, attachment_filename=curdir.rsplit('/', 1)[-1])

if __name__ == '__main__':
    app.run()
