class Node:
    def __init__(self, key, fb) -> None:
        self.key = key
        self.fb = fb
        self.height = 1
        self.left = None
        self.right = None


def printTree(node, level=0):
    if node is not None:
        printTree(node.right, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.key))
        printTree(node.left, level + 1)


def height(node):
    if node is None:
        return 0
    return node.height


def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)


def update_height(node):
    if node:
        node.height = 1 + max(height(node.left), height(node.right))


def left_rotate(x):
    y = x.right
    T2 = y.left
    
    y.left = x
    x.right = T2
    
    update_height(x)
    update_height(y)
    
    return y


def right_rotate(y):
    x = y.left
    T2 = x.right
    
    x.right = y
    y.left = T2
    
    update_height(y)
    update_height(x)
    
    return x


def insert_avl(root, key):
    if not root:
        return Node(key, 0)
    
    if key < root.key:
        root.left = insert_avl(root.left, key)
    else:
        root.right = insert_avl(root.right, key)
    
    update_height(root)
    fb = balance_factor(root)
    

    if fb > 1 and key < root.left.key:
        return right_rotate(root)
    
    if fb < -1 and key > root.right.key:
        return left_rotate(root)

    

    if fb > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    
    if fb < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    
    fb = balance_factor(root)
    root.fb = fb
    
    return root


values = [47, 22, 36, 81, 64, 41, 102, 32, 29]

root = None
for p in values:
    if not root:
        root = Node(p, 0)
        continue

    root = insert_avl(root, p)
 


#printTree(root)
