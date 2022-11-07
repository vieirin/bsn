import socket
import rosgraph
import rosnode

ID = rosnode.ID

def topic_type(t, pub_topics):
    matches = [t_type for t_name, t_type in pub_topics if t_name == t]
    if matches:
        return matches[0]
    return 'unknown type'


def list_nodes():
    master = rosgraph.Master(ID)
    nodes = rosnode.get_node_names()
    nodes.sort()

    nodes = [{
        'name': node[1:],
        'uri': rosnode.get_api_uri(master, node)
    } for node in nodes]
    return nodes


def node_info(id):
    master = rosgraph.Master(ID)
    node_name = rosgraph.names.script_resolve_name('rosnode', id)

    # go through the master system state first
    try:
        state = master.getSystemState()
        pub_topics = master.getPublishedTopics('/')
    except socket.error:
        raise rosnode.ROSNodeIOException("Unable to communicate with master!")

    pubs = sorted([t for t, l in state[0] if node_name in l])
    subs = sorted([t for t, l in state[1] if node_name in l])
    srvs = sorted([t for t, l in state[2] if node_name in l])

    return {
        'publication': [{
            'name': pub,
            'type': topic_type(pub, pub_topics)
        } for pub in pubs],
        'subscription': [{
            'name': sub,
            'type': topic_type(sub, pub_topics)
        } for sub in subs],
        'services': [{
            'name': service
        } for service in srvs]
    }
