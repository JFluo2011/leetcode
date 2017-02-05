import unittest


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.balanceFactor = 0

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.val = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def find_successor(self):
        return self.right_child.find_min()

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        else:
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def __iter__(self):
        if self.has_left_child():
            for elem in self.left_child():
                yield elem
        yield self.key
        if self.has_right_child():
            for elem in self.right_child():
                yield elem


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if not self.root:
            self.root = TreeNode(key=key, val=val)
        else:
            self._put(key, val, self.root)
        self.size += 1

    def _put(self, key, val, current_node):
        if current_node.key > key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)

    def __setitem__(self, key, value):
        self.put(key=key, val=value)

    def get(self, key):
        if self.root:
            node = self._get(key, self.root)
            if node:
                return node.val
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        if current_node.key == key:
            return current_node
        elif current_node.key > key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        if self._get(item, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        elif self.root.has_any_children():
            remove_node = self._get(key, self.root)
            if remove_node:
                self.remove(remove_node)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, remove_node):
        if remove_node.is_leaf():
            if remove_node == remove_node.parent.left_child:
                remove_node.parent.left_child = None
            else:
                remove_node.parent.right_child = None
        elif remove_node.has_both_children():
            successor = remove_node.find_successor()
            successor.splice_out()
            # remove_node.key = successor.key
            remove_node.val = successor.val
        else:
            if remove_node.has_left_child():
                if remove_node.is_left_child():
                    remove_node.parent.left_child = remove_node.left_child
                    remove_node.left_child.parent = remove_node.parent
                elif remove_node.is_right_child():
                    remove_node.parent.right_child = remove_node.left_child
                    remove_node.left_child.parent = remove_node.parent
                else:
                    remove_node.replace_node_data(remove_node.left_child.key, remove_node.left_child.val,
                                                  remove_node.left_child.left_child,
                                                  remove_node.left_child.right_child)
            else:
                if remove_node.is_left_child():
                    remove_node.parent.left_child = remove_node.right_child
                    remove_node.right_child.parent = remove_node.parent
                elif remove_node.is_right_child():
                    remove_node.parent.right_child = remove_node.right_child
                    remove_node.right_child.parent = remove_node.parent
                else:
                    remove_node.replace_node_data(remove_node.right_child.key, remove_node.right_child.val,
                                                  remove_node.right_child.left_child,
                                                  remove_node.right_child.right_child)

    def __delitem__(self, key):
        self.delete(key)


class AVLTree(BinarySearchTree):
    def _put(self, key, val, current_node):
        if current_node.key > key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
                self.update_balance(current_node.left_child)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)
                self.update_balance(current_node.right_child)

    def update_balance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.re_balance(node)
            return
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balanceFactor += 1
            else:
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self.update_balance(node.parent)

    def re_balance(self, node):
        if node.balanceFactor < 0:
            if node.right_child.balanceFactor > 0:
                self.rotate_right(node.right_child)
            self.rotate_left(node)
        else:
            if node.left_child.balanceFactor < 0:
                self.rotate_left(node.left_child)
            self.rotate_right(node)

    def rotate_left(self, root_node):
        new_root = root_node.right_child
        root_node.right_child = new_root.left_child
        if new_root.has_left_child():
            new_root.left_child.parent = root_node
        new_root.parent = root_node.parent
        if root_node.is_root():
            self.root = new_root
        else:
            if root_node.is_left_child():
                root_node.parent.left_child = new_root
            else:
                root_node.parent.right_child = new_root

        root_node.parent = new_root
        new_root.left_child = root_node
        root_node.balanceFactor = root_node.balanceFactor + 1 - min(new_root.balanceFactor, 0)
        new_root.balanceFactor = new_root.balanceFactor + 1 + max(root_node.balanceFactor, 0)

    def rotate_right(self, root_node):
        new_root = root_node.left_child
        root_node.left_child = new_root.right_child
        if new_root.has_right_child():
            new_root.right_child.parent = root_node
        new_root.parent = root_node.parent
        if root_node.is_root():
            self.root = new_root
        else:
            if root_node.is_left_child():
                root_node.parent.left_child = new_root
            else:
                root_node.parent.right_child = new_root

        root_node.parent = new_root
        new_root.left_child = root_node
        root_node.balanceFactor = root_node.balanceFactor - 1 - max(new_root.balanceFactor, 0)
        new_root.balanceFactor = new_root.balanceFactor - 1 + min(root_node.balanceFactor, 0)


def delete_tree(key):
    mytree = BinarySearchTree()
    mytree[17] = 1
    mytree[18] = 6
    mytree[5] = 2
    mytree[2] = 4
    mytree[11] = 5
    mytree[9] = 8
    mytree[7] = 12
    mytree[25] = 3
    mytree[16] = 9
    mytree[35] = 7
    mytree[29] = 10
    mytree[38] = 11
    print('*************************\n')
    print(key, mytree[key])
    mytree.delete(key)
    print(key, mytree[key])
    print('*************************\n')


def main():
    delete_tree(16)
    delete_tree(35)
    delete_tree(5)
    delete_tree(17)


if __name__ == '__main__':
    main()
