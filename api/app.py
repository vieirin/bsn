#!/usr/bin/env python
from flask import Flask
import rosnode
from dotenv import load_dotenv
from os.path import join, dirname
import ros_manager.manager as ros_manager

dotenv_path = join(dirname(__file__), '.env')  # Path to .env file
load_dotenv(dotenv_path)

app = Flask(__name__)

@app.route('/list_nodes')
def list_nodes():
    nodes = ros_manager.list_nodes()
    return {'nodes': nodes}

@app.route('/get_node_info/<id>')
def node_info(id): 
    return ros_manager.node_info('/'+ id)

if __name__ == "__main__":
    app.run(debug=True)

