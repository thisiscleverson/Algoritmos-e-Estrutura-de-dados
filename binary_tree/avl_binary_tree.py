import os
import time


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
    return height(node.left) - height(node.right)  # Corrigido: esquerda - direita


def update_height(node):
    """Atualiza a altura do nó baseado nas alturas dos filhos"""
    if node:
        node.height = 1 + max(height(node.left), height(node.right))


def left_rotate(x):
    """
    Rotação simples à esquerda
    x é o nó desbalanceado
    """
    y = x.right
    T2 = y.left
    
    # Realiza a rotação
    y.left = x
    x.right = T2
    
    # Atualiza alturas (x primeiro, depois y)
    update_height(x)
    update_height(y)
    
    return y


def right_rotate(y):
    """
    Rotação simples à direita
    y é o nó desbalanceado
    """
    x = y.left
    T2 = x.right
    
    # Realiza a rotação
    x.right = y
    y.left = T2
    
    # Atualiza alturas (y primeiro, depois x)
    update_height(y)
    update_height(x)
    
    return x


def insert_avl(root, key):
    # Caso base: cria novo nó
    if not root:
        return Node(key, 0)
    
    # Inserção recursiva
    if key < root.key:
        root.left = insert_avl(root.left, key)
    else:
        root.right = insert_avl(root.right, key)
    
    # Atualiza altura do nó atual
    update_height(root)
    
    # Calcula fator de balanceamento
    fb = balance_factor(root)
    
    # Casos de desbalanceamento
    # Caso Left Left
    if fb > 1 and key < root.left.key:
        return right_rotate(root)
    
    # Caso Right Right
    if fb < -1 and key > root.right.key:
        return left_rotate(root)
    
    # Caso Left Right
    if fb > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    
    # Caso Right Left
    if fb < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    fb = balance_factor(root)
    root.fb = fb
    
    return root


# Teste
root = Node(47, 0)
values = [22, 36, 81, 64, 41, 102, 32, 29]

for p in values:
    root = insert_avl(root, p)  # Importante: reassign the root
    print(f"Após inserir {p}:")
    printTree(root)
    
    #time.sleep(2)
    breakpoint()
    os.system("clear")

print("Árvore AVL final:")
printTree(root)
