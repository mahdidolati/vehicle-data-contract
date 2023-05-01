class MyLogger:
    def __init__(self, rn):
        self.items = {}
        self.runname = rn

    def add_item(self, k, v):
        if k not in self.items:
            self.items[k] = []
        self.items[k].append(v)
    
    def print(self):
        f = open("./reports/{}".format(self.runname), "+w")
        for k in self.items:
            print(k, self.items[k])
            f.write(str(k) + " " + str(self.items[k]) + "\n")
        f.close()