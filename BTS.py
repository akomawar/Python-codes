""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
temp = []

def makeList(root):
    if (root.left is not None) and (root.right is not None):
        if (root.data >= root.left.data) and (root.data <= root.right.data):
            makeList(root.left)
            temp.append(root.data)
            makeList(root.right)
        else:
            temp.append(root.data)
            
    else:
        temp.append(root.data)
        
def checkBST(root):
    makeList(root)
    final = sorted(set(temp))
    
    if(temp == final):
        #print len(temp)
        return True
    else:
        return False

