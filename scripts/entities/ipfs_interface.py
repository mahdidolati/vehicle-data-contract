import ipfsApi
import pickle
import requests


class IpfsInterface:
    def __init__(self):
        self.api = ipfsApi.Client('127.0.0.1', 5001)

    def save(self, v):
        return self.api.add_pyobj(v)

    def retrieve(self, k):
        url = "http://127.0.0.1:5001/api/v0/cat?stream-channels=true&encoding=json&arg={}".format(k)
        response = requests.post(url)
        return pickle.loads(response.content)
