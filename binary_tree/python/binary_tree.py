


class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None


def printTree(node, level=0):
    if node is not None:
        printTree(node.right, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.key))
        printTree(node.left, level + 1)
        

def insert(node, value):
    if value <= node.key:
        if node.left:
            insert(node.left, value)
        else:
            node.left = Node(value)
    else:
        if node.right:
            insert(node.right, value)
        else:
            node.right = Node(value)


def preOrder(node):
    print(node.key, end=" ")
    if node.left is not None:
        preOrder(node.left)
    if node.right is not None:
        preOrder(node.right)


def inOrder(node):
    if node.left is not None:
        inOrder(node.left)
    print(node.key, end=" ")
    if node.right is not None:
        inOrder(node.right)

        
def iterative_in_order_traversal(root):
    current = root
    
    while current is not None:
        if current.left is None:
            # Case 1: No left child, visit current node
            print(current.key, end=" ")
            current = current.right
        else:
            # Case 2: Has left child, find predecessor
            predecessor = current.left
            while predecessor.right is not None and predecessor.right != current:
                predecessor = predecessor.right
            
            if predecessor.right is None:
                # Create temporary link to current node
                predecessor.right = current
                current = current.left
            else:
                # Remove temporary link and visit node
                predecessor.right = None
                print(current.key, end=" ")
                current = current.right

        
        
def posOrder(node):
    if node.left is not None:
        posOrder(node.left)
    if node.right is not None:
        posOrder(node.right)
    print(node.key, end=" ")


def search(node, value):
    while node is not None and node.key != value:
        if value < node.key:
            node = node.left
        else:
            node = node.right
    return node


def find_parent(root, child):
    parent = None
    while root is not None and root.key != child:
        parent = root
        if root.key > child:
            root = root.left
        else:
            root = root.right
    return parent
        


root = Node(45)

values = [18, 30, 60, 81, 96, 101, 5, 8, 3]

for q in values:
    insert(root, q)


printTree(root)


print("\npreOrder: ", end="")
preOrder(root)

print("\ninOrder: ", end="")
inOrder(root)

print("\n em ordem: ", end="")
iterative_in_order_traversal(root)

print("\nposOrder: ", end="")
posOrder(root)

response = search(root, 3)
print(f"\nsearch: {response}")

parent = find_parent(root, 45)
print(f"\nparent: {parent.key}")

print("")
