import json
import subprocess


def namespaces():
    return [i['metadata']['name'] for i in _kubectl("get", "namespaces")['items']]


def pods(namespace):
    return _kubectl("get", "pods", "-n", namespace)['items']


def pod_name_to_node(pods):
    return {pod['metadata']['name']: pod['status']['hostIP'] for pod in pods}


def owner_to_pod_names(pods):
    result = {}
    for pod in pods:
        if 'ownerReferences' not in pod['metadata']:
            continue
        result.setdefault(pod['metadata']['ownerReferences'][0]['name'], []).append(pod['metadata']['name'])
    return result


def _kubectl(*args):
    return json.loads(subprocess.check_output(["kubectl", "-o", "json", *args]).decode())
