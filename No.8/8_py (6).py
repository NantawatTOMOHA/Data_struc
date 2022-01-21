
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
        self.flag= False
   
    def insert(self,node):
        if self.root is None:
            self.root= node
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
    
    def searchNode(self,Value):
       N=self.root
       def _searchNode(node,data):
        if(node is None ):
            return
        else:
            if(node.data ==data):
                
               if node.right is None and node.left is None:
                  self.flag=True
                  return print("Leaf")
               else:
                   self.flag=True
                   return print("Inner")       
            #recursive
        if(self.root.left!=None):
                      _searchNode(node.left,data)
            
        if(self.root.right!=None):
                       _searchNode(node.right,data)
       _searchNode(N,Value)
       if( self.flag==False):
           return print("Not exist")



  
    def PrintTree(self):
        def _PrintTree(node, level):
            if node != None:
                _PrintTree(node.right, level + 1)
                print('     ' * level, node)
                _PrintTree(node.left, level + 1)
        _PrintTree(self.root, 0)
  
if __name__ == '__main__':

  
  T=Bst()
  inp = [int(i) for i in input('Enter Input : ').split()]
 
  s=inp.pop(0)


for i in inp:
    root = T.insert(Node(i))
T.PrintTree()
if(inp[0]==s):
 print('Root')
else:
 T.searchNode(s)
  




