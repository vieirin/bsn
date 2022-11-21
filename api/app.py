#!/usr/bin/env python
from flask import Flask
import rosnode
from dotenv import load_dotenv
from os.path import join, dirname
from flask_cors import CORS
import ros_manager.manager as ros_manager

dotenv_path = join(dirname(__file__), '.env')  # Path to .env file
load_dotenv(dotenv_path)

app = Flask(__name__)
CORS(app)

@app.route('/list_nodes')
def list_nodes():
    nodes = ros_manager.list_nodes()
    return {'nodes': nodes}

@app.route('/get_node_info/<id>')
def node_info(id): 
    return ros_manager.node_info('/'+ id)

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)

