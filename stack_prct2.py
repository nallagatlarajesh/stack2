#a stack is used to insert and delete elements in lifo oredr 
#class stack:
    #def __init__(self):
       # self.items=[]
   # def onpush(self,item):
glassstack=list()
def isempty(glassstack):
    if len(glassstack)==0:
        return True
    else:
        return False
def oppush(glassstack,element):
    glassstack.append(element)
    
def size(glassstack):
    return len(glassstack)

def top(glassstack):
    if isempty(glassstack):
        print("stack is empty")
        return None
    else:
        x=len(glassstack)
        element=glassstack[x-1]
        return element
def oppop(glassstack):
    if isempty(glassstack):
        print("underflow")
        return None
    else:
        return(glassstack.pop())
def display(glassstack):
    x=len(glassstack)
    print("current elements in the stackare:")
    for i in range(x-1,-1,-1):
        print(glassstack[i])
        #function ends here
        
#crerating objects
#add elements to a stack
element="glass1" 
print("pussing element ",element)
oppush(glassstack,element)    #function calling

element="glass2"
print("pussing element to ",element)
oppush(glassstack,element)

print("popping element is :",oppop(glassstack))
display(glassstack)

element="glass3"
print("pussing  element ",element)
oppush(glassstack,element)

element="glass4"
print("pusssing element",element)
oppush(glassstack,element)

print("popping element:",oppop(glassstack))

#display the last elemeent  added to the stack
print("top element is ",top(glassstack))


#display the elem,ents of the stack after popping
display(glassstack)


#display all elements to the stack
#while True:
    #item=oppop(glassstack)
    #if item is None:
        #print("stack is emepy now")
        #break
    #else:
        #print("popped element is",item)        
        
