class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
    
   
class Bst:
    def __init__(self):
        self.root = None
        self.check=0
        self.NodeCh=None
        self.flag= False
   
    def insert(self,node):
        if self.root is None:
            self.root= node
            self.NodeCh=node
        else:
            Rootnode=self.root
            while True:
                if node.data >= Rootnode.data:
                   
                    if Rootnode.right is None :
                       
                        Rootnode.right = node        
                        break
                    Rootnode = Rootnode.right
                    
                else: 

                    if Rootnode.left is None:
                        Rootnode.left = node 
                        break
                    Rootnode = Rootnode.left   
                            
    def Root(self):
            return self.root.data
    
    def searchNodePrev(self,Value):
       N=self.root
       Node1=self.NodeCh
       def _searchNode(node,data,node1):
        if(node is None ):
            return
        else:
            if(node.data ==data):
              
                  self.flag=True
                  return print(str(node1.data))
             
        
            #recursive
        if(self.root.left!=None):
                      _searchNode(node.left,data,node)
            
        if(self.root.right!=None):
                       _searchNode(node.right,data,node)
       _searchNode(N,Value,None)
       if(self.flag== False):
           return print('Not Found Data')


  
    def PrintTree(self):
        def _PrintTree(node, level):
            if node != None:
                    _PrintTree(node.right, level + 1)
                    print('     ' * level, node)
                    _PrintTree(node.left, level + 1)
        _PrintTree(self.root, 0)
  
if __name__ == '__main__':

  
  T=Bst()
  inp = [str(i) for i in input('Enter Input : ').split('/')]
  s=int(inp[1])
  Inp=[int(i) for i in inp[0].split()]

for i in Inp:
    root = T.insert(Node(i))
T.PrintTree()
if(Inp[0]==s):
 print('None Because '+str(s)+' is Root')
else:
 T.searchNodePrev(s)
  


