import operator

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
            current_tree.setRootVal(int(exp))
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


def evaluate(parse_tree):
    oper_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left_child = parse_tree.getLeftChild()
    right_child = parse_tree.getRightChild()

    if left_child and right_child:
        func = oper_dict[parse_tree.getRootVal()]
        return func(evaluate(left_child), evaluate(right_child))
    else:
        return parse_tree.getRootVal()


def post_order_eval(parse_tree):
    oper_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    if parse_tree:
        result1 = post_order_eval(parse_tree.getLeftChild())
        result2 = post_order_eval(parse_tree.getRightChild())
        if result1 and result2:
            func = oper_dict[parse_tree.getRootVal()]
            return func(result1, result2)
        elif not result1 and not result2:
            return parse_tree.getRootVal()
        else:
            return result1 if result1 else result2


def main():
    args = [
        # '( & % $ )',
        '( 3 )',
        # '( 5 + + )',
        # '( + + 5 )',
        '( ( 10 + 5 ) * 3 )',
    ]
    for arg in args:
        try:
            pt = build_parse_tree(arg)
        except ValueError:
            print('Invalid expression: ', arg)
            continue
        pt.postorder()
        # print('arg: ', arg, '\nevaluate: ', evaluate(pt))
        print('arg: ', arg, '\npost_order_eval: ', post_order_eval(pt))


if __name__ == '__main__':
    main()

