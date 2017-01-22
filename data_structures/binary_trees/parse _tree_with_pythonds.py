from pythonds.basic import Stack
from pythonds.trees.binaryTree import BinaryTree


def build_parse_tree(expression):
    expression_list = expression.split()
    stack = Stack()
    e_tree = BinaryTree('')
    stack.push(e_tree)
    current_tree = e_tree

    for exp in expression_list:
        if exp == '(':
            current_tree.insertLeft('')
            stack.push(current_tree)
            current_tree = current_tree.getLeftChild()
        elif exp not in ['+', '-', '*', '/', ')']:
            current_tree.setRootVal(exp)
            parent = stack.pop()
            current_tree = parent
        elif exp in ['+', '-', '*', '/']:
            current_tree.setRootVal(exp)
            current_tree.insertRight('')
            stack.push(current_tree)
            current_tree = current_tree.getRightChild()
        elif exp == ')':
            current_tree = stack.pop()
        else:
            raise ValueError

    return e_tree


def main():
    pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
    pt.postorder()  # defined and explained in the next section


if __name__ == '__main__':
    main()

