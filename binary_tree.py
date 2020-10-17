class BinarySearchTree(object):
    """
        Класс описывает 'Бинарное Дерево Поиска'
    """
    def __init__(self, data):
        """
            Конструктор класса
            value - корень
            right - правая ветвь
            left - левая ветвь
            :param data: входное значение для установки корневого элемента
        """

        super(BinarySearchTree, self).__init__()
        self.value = data
        self.right = None
        self.left = None

    def insert(self, data):
        """
            Функция вставки элемента в дерево.
            :param data: значение для вставки в дерево
        """

        # Если элемент для вставки уже есть в дереве
        if self.value == data:
            print(f"Внимание, дерево не поддерживает дубликаты. Элемент {data} уже был в дереве, "
                  f"пожалуйста, введите другой.".format(data=data))
            return
        # Если элемент для вставки больше корневого элемента
        elif self.value < data:
            # Если правая ветвь пуста, вставляем элемент туда
            if self.right is None:
                self.right = BinarySearchTree(data)
                return
            # Если правая ветвь не пуста, то рекурсивно вызываем для нее функцию вставки
            self.right.insert(data)
        # Если элемент для вставки меньше корневого элемента
        else:
            # Если левая ветвь пуста, вставляем элемент туда
            if self.left is None:
                self.left = BinarySearchTree(data)
                return
                # Если левая ветвь не пуста, то рекурсивно вызываем для нее функцию вставки
            self.left.insert(data)

    def display(self):
        """
            Оболочка для вывода списка строк в файл
        """
        lines, *_ = self.__display()
        with open('output.txt', 'w') as f:
            for line in lines:
                f.write(line + '\n')

    def __display(self):
        """
            Защищенный метод реализующий формирование списка строк для вывода в файл
            :return: список строк для вывода, ширину, высоту и центр
        """

        # Если нет потомков (дочерних элементов)
        if self.right is None and self.left is None:
            line = '{value}'.format(value=self.value)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Если есть только левый потомок
        if self.right is None:
            lines, n, p, x = self.left.__display()
            s = '{value}'.format(value=self.value)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Если есть только правый потомок
        if self.left is None:
            lines, n, p, x = self.right.__display()
            s = '{value}'.format(value=self.value)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Если есть оба потомка
        left, n, p, x = self.left.__display()
        right, m, q, y = self.right.__display()
        s = '{value}'.format(value=self.value)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + _ for a, _ in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
