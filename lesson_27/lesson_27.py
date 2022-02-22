from typing import Optional, Any
from node import Node
if __name__ == '__main__':
    # Task 1

    # Extend UnorderedList
    # Implement append, index, pop, insert methods for UnorderedList.Also implement a slice method,
    # which will take two parameters `start` and `stop`, and return a copy of the list starting at the
    # position and going up to but not including the stop position.


    # Незаметил что к задания приложены листинги, по этому я написал все с нуля.
    class Package:
        def __init__(self, data: Any):
            self.__data = data
            self.next: Optional[Package] = None

        def __repr__(self):
            return f'object - {self.__data}'

        def __str__(self):
            return f'object - {self.__data}'

        def get_data(self) -> Any:
            return self.__data


    class Order_list:
        def __init__(self):
            self.root = None
            self.counter = -1

        def append(self, data: Any):
            package: Package = Package(data)
            self.counter += 1
            if not self.root:
                self.root = package
            else:
                package.next = self.root
                self.root = package

        def pop(self, x: Optional[int] = None) -> Any:
            if not self.root:
                raise IndexError('Package is empty')
            elif x == self.counter or x is None:
                present_elem = self.root
                self.root = self.root.next
                self.counter -= 1
                return present_elem.get_data()

            present_elem = self.root
            index_elem = self.counter
            while True:
                index_elem -= 1
                if x == index_elem:
                    pop_elem = present_elem.next
                    present_elem.next = present_elem.next.next
                    self.counter -= 1
                    return pop_elem.get_data()
                present_elem = present_elem.next

        def index(self, x: Any) -> int:
            present_item = self.root
            index_elem = self.counter
            while self.root:
                if present_item.get_data() == x:
                    return index_elem
                if present_item.next:
                    present_item = present_item.next
                    index_elem -= 1
                else:
                    raise ValueError(f'{x} is not in Order_list')

        def insert(self, i: int, x: Any):
            package: Package = Package(x)

            if not self.root:
                self.counter += 1
                self.root = package
            elif i > self.counter:
                self.counter += 1
                package.next = self.root
                self.root = package
            else:
                index_elem = self.counter
                present_elem = self.root
                while True:

                    if index_elem == i:
                        package.next = present_elem.next
                        present_elem.next = package
                        self.counter += 1
                        break

                    present_elem = present_elem.next
                    index_elem -= 1

    # q = Order_list()
    #
    # victor = 'Victor'
    # sergey = 'Sergey'
    # alex = 'Alex'
    # ivan = 'Ivan'
    # robert = 'Robert'
    # q.append(victor)
    # q.append(sergey)
    # q.append(alex)
    # q.append(ivan)
    # q.append(robert)

    # Task 2
    # Implement a stack using a singly linked list.

    class Stack:
        def __init__(self):
            self._root = None

        def is_empty(self) -> bool:
            if self._root:
                return False
            return True

        def pop(self):
            if self.is_empty():
                raise IndexError('Package is empty')
            elif self._root and self._root.get_next():
                self._root = self._root.get_next()
            else:
                self._root = None

        def push(self, data: Any):
            item: Node = Node(data)
            if not self._root:
                self._root = item
            else:
                item.set_next(self._root)
                self._root = item

        def peek(self) -> Any:
            return self._root.get_data()

        def size(self):
            present_elem = self._root
            size = 0
            while True:
                if present_elem:
                    size += 1
                    present_elem = present_elem.get_next()
                else:
                    return size

    # q = Stack()
    # q.push('one')
    # q.push('two')
    # q.push('three')
    # q.pop()
    # print(q.size())



