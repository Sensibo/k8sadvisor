FROM python:3.7-buster

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get upgrade -yq && \
    apt-get install -yq --no-install-recommends \
        apt-transport-https \
        curl \
        ca-certificates \
        gnupg-agent \
        software-properties-common \
        && \
    apt-get autoremove -y && \
    apt-get clean && \
    bash -c 'rm -rf /var/lib/apt/lists /tmp/* /var/tmp/*'
RUN (curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -) && \
    (echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list) && \
    apt-get update && \
    apt-get install -yq kubectl && \
    apt-get clean && \
    bash -c 'rm -rf /var/lib/apt/lists /tmp/* /var/tmp/*'
RUN pip3 install boto3 slackclient==1.3.2 

WORKDIR /opt/k8sadvisor
ENV PYTHONPATH=/opt/k8sadvisor
COPY k8sadvisor k8sadvisor
CMD python k8sadvisor/cli.py
