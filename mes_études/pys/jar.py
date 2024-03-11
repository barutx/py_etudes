import emoji

class Jar:

    def __init__(self,capacity=12):
        self.capacity = capacity    
        size = 0
        self.size = size

    def __str__(self):
        return emoji.emojize(":cookie:") * self.size

        
    @property # Getter for capacity
    def capacity(self):
        return self._capacity
    @capacity.setter ## Setter for capacity
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("CCapacity cannot be a negative integer")
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,size):
        if size > 12:
            raise ValueError("Jar is Full")
        elif size < 0:
            raise ValueError("Jar is Empty")
        self._size = size

    def deposit(self,n):
        self.size += n
        return n
    def withdraw(self,n):
        self.size -= n       
        return n

def main():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(3)
    print(jar)

    

if __name__ == '__main__':
    main()