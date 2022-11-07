#!/usr/bin/env python
from flask import Flask
import rosnode

import ros_manager.manager as ros_manager

app = Flask(__name__)

@app.route('/list_nodes')
def list_nodes():
    nodes = ros_manager.list_nodes()
    return {'nodes': nodes}

@app.route('/get_node_info/<id>')
def node_info(id): 
    return ros_manager.node_info('/'+ id)

