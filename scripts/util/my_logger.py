import numpy as np


class MyLogger:
    def __init__(self, rn):
        self.items = {}
        self.runname = rn

    def add_item(self, c, k, v):
        if c not in self.items:
            self.items[c] = dict()
        if k not in self.items[c]:
            self.items[c][k] = []
        self.items[c][k].append(v)
    
    def print(self):
        f = open("./reports/{}".format(self.runname), "+w")
        for c in self.items:
            for k in self.items[c]:
                print(c, k, np.mean(self.items[c][k]))
                f.write(str(c) + " " + str(k) + " " + str(np.mean(self.items[c][k])) + "\n")
        f.close()