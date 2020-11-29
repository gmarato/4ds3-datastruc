class Queue:
    """Queue implementation using python"""

    def __init__(self):
        self.__items = []
    
    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        try:
            return self.__items.pop(0)
        except:
            print("Queue is empty")
    
    def __len__(self):
        return len(self.__items)
    
    def isEmpty(self):
        return self.__items == []

    def __str__(self):
        """Returns all elements in the stack as a string 

        Returns:
            str: all elements in the stack
        """
        str1 = ""

        for item in self.__items:
            str1 += str(item) + " "

        return str1

def hotPotato(namelist, num):
    """Test of the queue with an example from the book"""
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while len(simqueue) > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
