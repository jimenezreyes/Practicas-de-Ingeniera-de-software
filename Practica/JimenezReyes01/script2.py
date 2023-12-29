# Obtenemos los valores de la lista desde el usuario
nums_input = input("Ingresa los valores de la lista separados por comas: ")
nums = [int(num.strip()) for num in nums_input.split(',')]

# Obtenemos el valor objetivo (target) desde el usuario
target = int(input("Ingresa el valor objetivo: "))

def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]
    return [-1,-1]
    
indices = two_sum(nums, target)

#Salida
print(two_sum(nums, target))



# Clase para formar un arbol binario
class Arbol:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Inserta un nuevo nodo en el árbol binario de búsqueda
    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    # Función auxiliar para insertar un nuevo nodo de manera recursiva
    def _insert_rec(self, root, key):
        if root is None:
            return Arbol(key)

        if key < root.key:
            root.left = self._insert_rec(root.left, key)
        else:
            root.right = self._insert_rec(root.right, key)

        return root

    # Realiza un recorrido preorden en el árbol
    def preorder(self):
        self._preorder_rec(self.root)
        print("\n")

    # Función auxiliar para realizar un recorrido preorden
    def _preorder_rec(self, root):
        if root:
            print(root.key, end=" ")
            self._preorder_rec(root.left)
            self._preorder_rec(root.right)

    # Realiza un recorrido inorder en el arbol
    def inorder(self):
        self._inorder_rec(self.root)
        print("\n")

    # Funcion auxiliar para realizar un recorrido inorder
    def _inorder_rec(self, root):
        if root:
            self._inorder_rec(root.left)
            print(root.key, end=" ")
            self._inorder_rec(root.right)

    # Realiza un recorrido postorder en el arbol
    def postorder(self):
        self._postorder_rec(self.root)
        print()

    # Funcion auxiliar para realizar un recorrido postorder
    def _postorder_rec(self, root):
        if root:
            self._postorder_rec(root.left)
            self._postorder_rec(root.right)
            print(root.key, end=" ")

# Ejemplo de uso
bst = BinarySearchTree()
bst.insert(10)
bst.insert(30)
bst.insert(20)
bst.insert(50)
bst.insert(110)
bst.insert(60)
bst.insert(90)

print("\nRecorrido en preorden:")
bst.preorder()

print("Recorrido en inorden:")
bst.inorder()

print("Recorrido en postorden:")
bst.postorder()