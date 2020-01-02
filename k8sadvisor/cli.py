#!/usr/bin/env python3
from k8sadvisor import kubectl

for namespace in kubectl.namespaces():
    pods = kubectl.pods(namespace)
    pod_name_to_node = kubectl.pod_name_to_node(pods)
    owner_to_pod_names = kubectl.owner_to_pod_names(pods)
    for owner, pods in owner_to_pod_names.items():
        nodes = set([pod_name_to_node[p] for p in pods])
        print(f"namespace {namespace}: owner {owner}: has {len(pods)} pods on {len(nodes)} nodes")
        if len(pods) > 1 and len(nodes) == 1:
            print(f"ISSUE DETECTED: namespace {namespace} owner {owner} is not highly available")
