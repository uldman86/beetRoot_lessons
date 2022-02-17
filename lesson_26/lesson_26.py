if __name__ == '__main__':
    # Task 1
    # Write a program that reads in a sequence of characters and prints them in reverse order,
    # using your implementation of Stack.

    class MyStack_1:
        def __init__(self):
            self.__result = []

        def append_char(self, input_char):
            if not input_char:
                raise ValueError('Str empty')
            self.__result.insert(0, input_char)

        def __repr__(self):
            representation = "<Queue>\n"
            for ind, item in enumerate(self.__result, 1):
                representation += f"{ind}: {str(item)}\n"
            return representation

        def __str__(self):
            return self.__repr__()


    q = MyStack_1()
    while True:
        user_input = input('Typing char  \n Enter "quit" for Exit\n')
        if user_input.lower() == 'quit':
            print('Exit')
            break
        q.append_char(user_input)
        print(f'Char "{user_input}" append to collection')
    print(q)

    # Task 2
    # Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces,
    # and curly brackets are "balanced."

    class Stack2:

        def __init__(self):
            self.__stack = []
            self.braces = {')': '(', '}': '{'}
            self.balance = None

        def pop(self):
            if self.__stack:
                self.__stack.pop()

        def push(self, input_str):
            self.balance = True
            for item in input_str:
                if item in '{(':
                    self.__stack.append(item)
                elif item in '})':
                    if self.__stack and self.braces[item] == self.__stack[-1]:
                        self.pop()
                    else:
                        self.balance = False
            if self.__stack:
                self.__stack.clear()
                self.balance = False
            return self.balance

        def get_data(self):
            return self.__stack


    q = Stack2()
    assert q.push('}}})((((') == False
    assert q.push('(asd{1}  awd ({}))') == True

    # Task 3
    # Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
    # Any other element must remain on the stack respecting their order.
    # Consider the case in which the element is not found - raise ValueError with proper info Message

    from typing import Optional, Any


    class Package:
        def __init__(self, data: Any):
            self.__data = data
            self.link: Optional[Package] = None

        def __repr__(self):
            return f'object - {self.__data}'

        def __str__(self):
            return f'object - {self.__data}'

        def get_data(self) -> Any:
            return self.__data


    class Stack:
        def __init__(self):
            self.root = None

        def push(self, data: Any):
            package: Package = Package(data)
            if not self.root:
                self.root = package
            else:
                package.link = self.root
                self.root = package

        def pop(self) -> Any:
            elem: Optional[Package] = self.root
            if not elem:
                raise IndexError('Package is empty')
            self.root = elem.link
            return elem

        def get_from_stack(self, elem):
            previous_elem: Optional[Package] = self.root.link
            present_elem: Package = self.root
            next_elem: Optional[Package] = None
            while True:
                if present_elem.get_data() is elem:
                    next_elem.link = previous_elem
                    return present_elem.get_data()
                if not previous_elem:
                    print('Elem not found')
                    return None
                next_elem = present_elem
                present_elem = previous_elem
                previous_elem = present_elem.link


    q = Stack()

    victor = 'Victor'
    sergey = 'Sergey'
    alex = 'Alex'
    ivan = 'Ivan'
    robert = 'Robert'
    q.push(victor)
    q.push(sergey)
    q.push(alex)
    q.push(ivan)
    q.push(robert)
    print(q.pop())
    print(q.get_from_stack(sergey))
    print(q.get_from_stack(sergey))
    print(q.get_from_stack(123))
