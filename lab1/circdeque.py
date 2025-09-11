# Для python

class CircularDeque:
    def __init__(self, n: int, push_force: bool):
        if not isinstance(push_force, bool):
            raise ValueError
        if not isinstance(n, int):
            raise ValueError
        if n <= 0:
            raise ValueError
        self.__data = [0] * n
        self.__push_force = push_force
        self.__max_size = n
        self.__front = 0
        self.__back = n - 1
        self.__size = 0
    

    def __inc_front(self):
        self.__front += 1
        self.__front %= self.__max_size

    def __dec_front(self):
        self.__front -= 1
        self.__front %= self.__max_size

    def __inc_back(self):
        self.__back += 1
        self.__back %= self.__max_size
    
    def __dec_back(self):
        self.__back -= 1
        self.__back %= self.__max_size

    def push_front(self, x: int):
        if self.full():
            if not self.__push_force:
                raise IndexError
            
            self.__dec_front()
            self.__dec_back()
        
        else:
            self.__dec_front()
            self.__size += 1

        self.__data[self.__front] = x

    def push_back(self, x: int):
        if self.full():
            if not self.__push_force:
                raise IndexError
            self.__inc_front()
            self.__inc_back()
        else:
            self.__inc_back()
            self.__size += 1
        self.__data[self.__back] = x

    def pop_front(self) -> int:
        if self.empty():
            raise IndexError

        value = self.front()
        self.__inc_front()
        self.__size -= 1
        return value
    
    def pop_back(self) -> int:
        if self.empty():
            raise IndexError

        value = self.back()
        self.__dec_back()
        self.__size -= 1
        return value

    def front(self) -> int:
        if self.empty():
            raise IndexError

        return self.__data[self.__front]

    def back(self) -> int:
        if self.empty():
            raise IndexError

        return self.__data[self.__back]

    def size(self) -> int:
        return self.__size

    def empty(self) -> bool:
        return self.size() == 0

    def full(self):
        return self.size() == self.__max_size

    def resize(self, new_cap: int):
        if not isinstance(new_cap, int):
            raise ValueError
        if new_cap <= 0:
            raise ValueError
        new_data = [0] * new_cap
        i = self.__front
        j = 0
        copy_size = min(self.__size, new_cap)
    
        for _ in range(copy_size):
            new_data[j] = self.__data[i]
            j += 1
            i = (i + 1) % self.__max_size

        self.__data = new_data
        self.__max_size = new_cap
        self.__size = copy_size
        self.__front = 0
        self.__back = self.__size - 1 if self.__size > 0 else 0

    def __str__(self) -> str:
        return f"size: {self.size()}, front: {self.__front}, back: {self.__back}, {str(self.__data)}"

def main():
    dq = CircularDeque(3, True)
    dq.push_back(1)
    dq.push_back(2)
    dq.push_back(3)
    print(dq)
    dq.push_back(4)
    print(dq)

    dq = CircularDeque(3, False)
    assert dq.size() == 0
    dq.push_front(1)
    print(dq.front()) 
    print(dq)
    assert dq.back() == 1
    assert dq.size() == 1
    assert dq.pop_back() == 1
    dq.push_back(2)
    print(dq)
    assert dq.front() == 2
    assert dq.back() == 2
    assert dq.size() == 1
    dq.push_front(1)
    print(dq.back())
    assert dq.front() == 1
    print(dq)
    dq.push_front(52)
    print(dq)
    print(dq.full())
    print(dq.back())
    print(dq.front())
    print('\n')
    dq = CircularDeque(3, True)
    dq.push_back(1)
    print(dq)
    dq.push_back(2)
    print(dq)
    dq.push_back(3)
    print(dq)
    dq.pop_back()
    dq.push_back(52)
    print(dq)
    print(dq.back())
    dq.push_back(11)
    print(dq)
    print(dq.back())
    dq.push_front(1)
    print(dq)
    dq.push_front(2)
    print(dq)
    dq.push_back(2)
    print(dq)
    dq.resize(2)
    print(dq)
    dq.resize(13)
    print(dq)

if __name__ == "__main__":
    main()

