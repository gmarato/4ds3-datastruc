class Stack:
    """LIFO Stack implementation using a Python list as underlying storage"""
    def __init__(self):
        self.__items = []
    
    def isEmpty(self):
        return self.__items == []
    
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        """Returns (no removal) the element at the top of the stack.

        Returns:
            var: top element of the stack 
        """
        try:
            return self.__items[len(self.__items)-1]
        except:
            print("Stack is empty")

    def __len__(self):
        return len(self.__items)

    def __str__(self):
        """Returns all elements in the stack as a string 

        Returns:
            str: all elements in the stack
        """
        str1 = ""

        for item in self.__items:
            str1 += str(item) + " "

        return str1

def string_reverse(mystr):
    """Reverses a string using a stack

    Args:
        mystr (str): string to reverse

    Returns:
        str: reversed string
    """
    s = Stack()

    for char in range(0,len(mystr)):
        s.push(mystr[char])

    mystr_rev = ""

    while not s.isEmpty():
        mystr_rev += s.pop()

    return mystr_rev

def parChecker(symbolString):
    """Checks for single symbol balance"""
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def parChecker(symbolString):
    """Checks for multiple symbol balance"""
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


mystr = "The quick brown fox jumped over Marato"
print(string_reverse(mystr))

print(parChecker('((()))'))
print(parChecker('(()'))

print(parChecker('{({([][])}())}'))
print(parChecker('[{()]'))
