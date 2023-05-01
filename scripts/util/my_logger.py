class MyLogger:
    def __init__(self):
        self.items = {}

    def add_item(self, k, v):
        if k not in self.items:
            self.items[k] = []
        self.items[k].append(v)
    
    def print(self):
        for k in self.items:
            print(k, self.items[k])