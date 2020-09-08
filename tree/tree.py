import sys

class Node():
    def __init__(self, idxs, is_suffix=False, children=None):
        self.idxs = idxs
        self.is_suffix = is_suffix
        if children is None:
            children = []
        self.children = children

class Suffix_Tree():
    def __init__(self, text):
        self.text = text + '$'
        self.root = Node((0,0), is_suffix=False)
        self.N = len(text)
        
        #Add suffixes *from largest to smaller*
        for i in range(self.N):
            self.add_child(self.root, i)    

    def print_node(self, node, acc):
        for child in node.children:
            if node != self.root:
                print(acc + "'--" + self.text[child.idxs[0]:child.idxs[1]])
            else:
                print(acc + "'--" + self.text[child.idxs[0]:child.idxs[1]])
            self.print_node(child, '  ' + acc)

    def print_tree(self):
        self.print_node(self.root,'')    
    
    def add_child(self, father, idx):
        for node in father.children:
            if self.text[idx] == self.text[node.idxs[0]]:
                #Find the preffix that node and the suffix share
                k = 1
                while (k < self.N - idx and 
                    k < node.idxs[1] - node.idxs[0] and
                    self.text[idx + k] == self.text[node.idxs[0] + k]):
                    k += 1
                    
                suffix_remainder = idx + k
                node_remainder = node.idxs[0] + k
                #If node suffix, simply move on
                if node_remainder == node.idxs[1]:
                    self.add_child(node, suffix_remainder)
                    return
                else:
                    #Change this node to be the commom prefix and update the children
                    node.children = [Node((node_remainder,node.idxs[1]), 
                                        is_suffix = node.is_suffix, 
                                        children=node.children),
                                    Node((suffix_remainder,self.N+1), is_suffix=True)]
                    node.idxs = (node.idxs[0], node_remainder)
                    node.is_suffix = False
                    return
                                
        father.children.append(Node((idx,self.N+1), is_suffix=True))
        return

    def search_longest_in_branch(self, node):         
        node_text = self.text[node.idxs[0]:node.idxs[1]]   
        #if all children are leafs, the longest branch is the node itself
        substr = self.text[node.idxs[0]:node.idxs[1]]  
        end = node.idxs[1]

        for child in node.children:
            if not child.is_suffix:
                child_text = self.text[child.idxs[0]:child.idxs[1]]
                #find the longest local branch that starts at the current child
                local_end, local_substr = self.search_longest_in_branch(child)   
                #update the longest branch among the node's children
                if len(node_text + local_substr) > len(substr):
                    end = local_end
                    substr = node_text + local_substr

        #return the longest branch starting at the current node
        return end, substr

    def longest_repeated_substr(self):
        '''
        Finds the longest repeated substring in the text by finding the "deepest" 
        internal node, i.e., the one whose branch have the larger 
        Since all we have to do is to walk through the tree, the algorithm is O(N)
        '''
        sys.setrecursionlimit(10000)

        end, substr = self.search_longest_in_branch(self.root)

        return substr, end - len(substr)
