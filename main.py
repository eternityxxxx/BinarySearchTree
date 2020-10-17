import binary_tree
import random

if __name__ == '__main__':

    # Экземпляр класса BinarySearchTree
    bst = binary_tree.BinarySearchTree(50)
    # Для регулировки кол-ва элементов дерева, менять n
    n = 25

    # Тут просто рандомно заполняем дерево
    for _ in range(n):
        bst.insert(random.randint(1, 100))

    # И выводи в файл
    bst.display()
