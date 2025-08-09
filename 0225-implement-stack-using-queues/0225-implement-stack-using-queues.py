class MyStack:

    def __init__(self):
        self.q = deque()
        self.topelm = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.topelm = x

    def pop(self) -> int:
        size = len(self.q)
        while size > 2:
            self.q.append(self.q.popleft())
            size -= 1
        self.topelm = self.q[0]
        self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.topelm

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()