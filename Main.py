class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.rear = None

  def enqueue(self, data) -> None:
    n = Node(data)
    if self.head==self.rear==None:
        self.head=self.rear=n
    else:
        self.rear.next = n
        self.rear = n

  def dequeue(self) -> None:
    if self.head==self.rear:
        self.head=self.rear=None
    else:
        self.head = self.head.next

  def status(self) -> None:
    t = self.head
    while t!=None:
        print(t.data, end="=>")
        t = t.next
    print(t)


# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
