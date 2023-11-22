class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def cycleDetection(head):

    current = head
    s = set()

    while current:

        if current in s:
            return True
        
        s.add(current)

        current = current.next

    return False

if __name__ == '__main__':

    head = None
    for i in reversed(range(5)):
        head = Node(i+1, head)

    head.next.next.next.next.next = head.next.next

    if cycleDetection(head):
        print("Cycle Found")
    else:
        print("Cycle Not Found")
