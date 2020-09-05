import numpy as np

class Suffix_Trie():
    class Node():
        def __init__(self, idxs, is_suffix=True):
            self.label = idxs
            self.is_suffix = is_suffix
            self.children = {}

    def __init__(self, text):
        self.text = np.array(text.split())
        self.root = self.Node(None, is_suffix=False)
        self.N = len(self.text)

        for i in range(self.N):
            self.add_child(i)
    
    def add_child(self, idx):
        pass

