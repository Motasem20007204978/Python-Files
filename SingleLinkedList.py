class Node(object):
    """docstring for Node"""
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleList(object):
    """docstring for linkedList"""
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head 
        while temp is not None:
            print(temp.data,end="-->")
            temp = temp.next
        print("null")


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
            temp = temp.next # to access last node 
        
        temp.next = new_node


    def poll(self):
        if self.isEmpty() :
            print("list is Empty")
            return
            
        returningValue = self.head.data        
        self.head = self.head.next
        return returningValue #to return the value of poped node


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

        else:# there is minimum tow nodes

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
            return returningValue #to return the value of poped node


    def popLast(self):
        
        if self.isEmpty():
            return

        return self.popAt(self.length()-1)


    def push(self,data):
        temp = Node(data)  
        temp.next,self.head = self.head,temp

    def addItemAt(self,data,index):

        if index not in range(self.length()+1):
            #maximum position must be equal length to append node
            #minimum position must be equal 0 to push node
            print("invalid index")

        elif index == 0:
            self.push(data)

        elif index == self.length():
            self.append(data)

        
        else:# there is minimum tow nodes

            new_node = Node(data)
            prev = self.head
            temp = self.head.next # index 1

            counter = 1 # because the list will start with index 1
            while temp.next is not None:
                
                if counter == index:
                    break

                prev = temp # to handle the previous node to link it with new node & push temp node after new node
                counter += 1 
                temp = temp.next
            

            prev.next = new_node
            new_node.next = temp

        
    def reverseList(self):
        length = self.length()

        if self.isEmpty() or length == 1:
            return


        for _ in range(length):
            self.addItemAt(self.poll(),length-_)
    
    

    def getItemAt(self,index):

        temp = self.head; count = 0
        while temp is not None:
            if index == count:#to stop if access to needed node
                break
            count += 1; 
            temp = temp.next

        return temp.data

    def removeItem(self,Item):
        for _ in range(self.length()):
            if Item == self.getItemAt(_):
                self.popAt(_)
                break

    def addList(self,List):
        for _ in List:
            self.append(_)


    def isPalendrome(self):

        if self.isEmpty() or self.length() == 1:
            return

        else:
            temp = self.head
            counter,inverseIndex = 0
            length = self.length()

            while temp is not None:

                inversePosition = length-(inverseIndex+1)#starts with last index

                if inverseIndex == int(length/2) :
                    break  #if check first half of the list does not need to check second half                

                if temp.data == self.getItemAt(inversePosition):
                    #if the data is equal to data from opposite index
                    counter += 1

                inverseIndex += 1#to backward step py step
                temp = temp.next

            return counter == inverseIndex#means that the firs half is identical with second half


    def removeDuplicates(self):
        if self.isEmpty() or self.length() == 1:
            return

        current = second = self.head
        while current is not None:
            while second.next is not None:   # check second.next here rather than second
                if second.next.data == current.data:   # check second.next.data, not second.data
                    second.next = second.next.next   # cut second.next out of the list
                else:
                    second = second.next   # put this line in an else, to avoid skipping items
            current = second = current.next

'''      
if __name__ == '__main__':
        
    leList = SingleList()
    leList.head = Node(2)
    leList.head.next = Node(5)
    leList.head.next.next = Node(7)  
    print("the list before any function is ",end="")
    leList.printList()

    print("the list after push 1 is ",end="")
    #Add a node at the front
    leList.push(1)
    leList.printList()

    print("the list after append 15 is ",end="")
    leList.append(15)
    leList.printList()

    print("the list after pop number ",leList.popAt(4)," is ",end="")
    
    leList.printList()

    print("the list after pop last is ",end="")
    leList.popLast()
    leList.printList()
    
    print("the list after reverse is ",end="")
    leList.reverse() 
    leList.printList()   

    leList.append(2);leList.append(5)
    leList.append(10);leList.append(7)
    leList.append(20);leList.append(9)
    
    leList.printList()

    print("is list nodes palendrome ? ",leList.isPalendrome())

    leList.removeDuplicates()
    print("the list after remove duplicates is ",end="")
    leList.printList()

    leList.reverseList()
    print("the list after reverse is ",end="")
    leList.printList()

    print("the list after add item at index 6 is ",end="")
    leList.addItemAt(8,6)
    leList.printList()

    print("the list after remove item 20 is ",end="")
    leList.removeItem(20)
    leList.printList()

    leList.addList(['My','name','is','motasem'])
    leList.printList()
'''