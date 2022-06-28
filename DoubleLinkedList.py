
class Node(object):
    """docstring for Node"""
    def __init__(self, data):
        
        self.data = data
        self.prev = None
        self.next = None

class DoubleList(object):
    """docstring for DoubleLinkedList"""
    def __init__(self):
        self.head = None
        

    def printList(self):
        temp = self.head 
        print('None',end="<--")
        while temp.next is not None:
            print(temp.data,end="<-->")
            temp = temp.next

        print(temp.data,end="-->")
        print("None")


    def length(self):
        temp = self.head ;count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count


    def isEmpty(self):
        return self.head is None

    
    def append(self,data):

        new_node = Node(data)

        if self.isEmpty(): 
            self.head = new_node 
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next# to access last node 
        
        temp.next = new_node
        new_node.prev = temp


    def poll(self):
        if self.isEmpty() :
            print("list is Empty")
            return
            
        returningValue = self.head.data

        self.head = self.head.next

        if not self.isEmpty():
            # if there is only one node & poped ,list becomes null & has no previous

            self.head.prev = None

        return returningValue#to return the value of poped node


    def popAt(self,index):

        if self.isEmpty() :
            print("list is Empty")
            return

        elif index not in range (self.length()):
            #maximum position must be equal last index to pop node
            #minimum position must be equal 0 to pop node
            print("invalid index")
            return

        elif index == 0:
            return self.poll()

        else: # there is minimum tow nodes
            temp = self.head.next
            count = 1 # because the list will start with index 1
            while temp is not None:

                if index == count:
                    break
                
                prev = temp # to handle the previous node to link it with new node & push temp node after new node
                count += 1
                temp = temp.next
                returningValue = temp.data

            prev.next = temp.next

            if temp.next is not None: #if need last node to pop which has no previous for its next
                temp.next.prev = prev
            return returningValue #to return the value of poped node


    def popLast(self):
        
        if self.isEmpty():
            return

        return self.popAt(self.length()-1)


    def getNodeAt(self,index):
        temp = self.head
        count = 0
        while temp is not None:
            if index == count:
                break
            temp = temp.next ;count += 1
        
        return temp


    def addList(self,List):
        for _ in List:
            self.append(_)


    def reverseList(self):
        List = list(self.popLast() for _ in range(self.length()))

        self.addList(List)


    def push(self,data):
        temp = Node(data)  
        temp.next = self.head
        self.head = temp

        temp.next.prev = temp


    def addItemAt(self,data,index):

        if index not in range(self.length()+1):
            #maximum position must be equal length to append node
            #minimum position must be equal 0 to push node
            print("invalid index")

        elif index == 0:
            self.push(data)

        elif index == self.length():
            self.append(data)

        
        else:

            new_node = Node(data)
            prev = self.head
            temp = self.head.next

            counter = 1 # because the list will start with index 1
            while temp.next is not None:
                
                if counter == index:
                    break
                prev = temp
                counter += 1
                temp = temp.next
            

            prev.next, new_node.prev = new_node, prev
            

            new_node.next, temp.prev = temp, new_node
            
'''
if __name__ == '__main__':
    
    doubleList = DoubleList()
    doubleList.append(1)
    doubleList.append(2)
    doubleList.append(3)
    doubleList.append(4)
    doubleList.append(41)

    #doubleList.popAt(2)
    doubleList.push(0)
    #doubleList.reverseList()
    doubleList.addItemAt(5,3)
    doubleList.printList()

    getNode = doubleList.getNodeAt(3)
    print(getNode.prev.data,getNode.data,getNode.next.data)
'''