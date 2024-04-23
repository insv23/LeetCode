'''
Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

Your DynamicArray class should support the following operations:
'''
class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        if i < 0 or i >= self.size:
            raise IndexError('Index out of bounds')
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.size:
            raise IndexError('Index out of bounds')
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size == 0:
            raise IndexError('Pop from empty array')
        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size = self.size - 1
        return val

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity