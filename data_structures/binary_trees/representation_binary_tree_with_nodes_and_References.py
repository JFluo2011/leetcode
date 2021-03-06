class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left = self.left_child
            self.left_child = t

    def insert_right(self, new_code):
        if self.right_child:
            self.right_child = BinaryTree(new_code)
        else:
            t = BinaryTree(new_code)
            t.right_child = self.right_child
            self.right_child = t

    def get_root_val(self):
        return self.key

    def set_root_val(self, obj):
        self.key = obj

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def pre_order(self):
        """
        实现为一个外部函数更好
        :return:
        """
        print(self.key)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.key)

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.key)
        if self.right_child:
            self.right_child.in_order()


def test():
    r = BinaryTree('a')
    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left('b')
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
    r.insert_right('c')
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val('hello')
    print(r.get_right_child().get_root_val())


def main():
    test()


if __name__ == '__main__':
    main()
