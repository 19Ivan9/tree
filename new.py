from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.right_hand: Optional['Node'] = None
        self.left_hand: Optional['Node'] = None

    def append(self, value):
        new_node = Node(value)
        self._push(new_node)

    def _push(self, n: 'Node'):
        if n.value > self.value:
            if self.right_hand:
                self.right_hand._push(n)
            else:
                self.right_hand = n
        elif n.value < self.value:
            if self.left_hand:
                self.left_hand._push(n)
            else:
                self.left_hand = n
        else:
            pass

    def is_exist(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left_hand:
                return self.left_hand.is_exist(value)
            else:
                return False
        elif value > self.value:
            if self.right_hand:
                return self.right_hand.is_exist(value)
            else:
                return False

    def show(self):
        if self.left_hand:
            self.left_hand.show()
        print(self.value)
        if self.right_hand:
            self.right_hand.show()

    def generator(self):
        if self.left_hand:
            for i in self.left_hand.generator():
                yield i
        yield self.value
        if self.right_hand:
            for i in self.right_hand.generator():
                yield i

    def __iter__(self):
        self._g = self.generator()
        return self

    def __next__(self):
        return next(self._g)

    def delete(self, value):
        if value == self.value:
            if not self.right_hand and not self.left_hand:
                return None
            if self.right_hand and self.left_hand:
                self.right_hand._push(self.left_hand)
                return self.right_hand
            if self.left_hand and not self.right_hand:
                return self.left_hand

            if self.right_hand and not self.left_hand:
                return self.right_hand

        if value > self.value:
            if self.right_hand:
                self.right_hand = self.right_hand.delete(value, self)
            return self
        elif value < self.value:
            if self.left_hand:
                self.left_hand = self.left_hand.delete(value, self)
            return self

    def replace(self, first_n, new_n):
        if self.left_hand == first_n:
            self.left_hand = new_n
        elif self.right_hand == first_n:
            self.right_hand = new_n


if __name__ == '__main__':
    n = Node(20)
    n.append(10)
    n.append(1)
    n.append(15)
    n.append(35)
    n.append(65)
    n.show()
    n = n.delete(20)

    # n.delete(20)

    for i in n:
        print(i)
    assert n.is_exist(1)
    assert n.is_exist(2) == False
