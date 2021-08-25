from flask import Flask, request
import sys
app = Flask(__name__)

class Node:
    def __init__(self,data,n=None):
        self.data = data
        self.n = n

class LinkedList:
    def __init__(self,head):
        self.head = head

@app.route('/')
def mainMethod():
    start = 1
    if 'start' in request.args:
        start = int(request.args['start'])
    step = int(request.args['step'])
    
    ll = LinkedList(Node(1))
    curr = ll.head

    for i in range(1,step+1):
        if i<step:
            curr.n = Node(i+1)
        else:
            curr.n = ll.head        
        curr = curr.n

    curr = ll.head
    for i in range(start-1):
        curr = curr.n

    a = []
    while (step - len(a) > 1):
        a.append(curr.n)
        curr.n = curr.n.n
        curr = curr.n
    return (str(curr.data))

if __name__ == '__main__':
    start = 1
    if 'start' in request.args:
        start = int(request.args['start'])
    print(int(request['start']),start)
    mainMethod(int(request['step']),start)

