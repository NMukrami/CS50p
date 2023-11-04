import sys


def main():
    jar = Jar(7)
    jar.deposit(4)
    jar.withdraw(3)
    print(f"capacity:{jar.capacity} and size:{jar.size}")


class Jar:
    def __init__(self, capacity=12):
        # check capacity if it nagative int or not
        if capacity < 0:
            raise ValueError("Invalid capacity")

        else:
            self._capacity = capacity
            self._size = 0


    def __str__(self):
        return "🍪" * self.size


# check deposit input and size in range of capacity
    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Invalid deposit")

        elif n + self.size > self.capacity:
            raise ValueError("Invalid Amount")

        # size + n
        else:
            self._size += n


# check withdraw cokies input in range of capacity size
    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Invalid withdraw")

        # size - n
        else:
            self._size -= n


# setter for capacity
    @property
    def capacity(self):
        return self._capacity


# setter for size
    @property
    def size(self):
        return self._size


if __name__ == "__main__":
    main()