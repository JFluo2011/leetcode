def binary_tree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])

    return root


def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])

    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, val):
    root[0] = val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


def build_tree():
    r = binary_tree('a')
    insert_left(r, 'b')
    insert_right(get_left_child(r), 'd')
    insert_right(r, 'c')
    insert_left(get_right_child(r), 'e')
    insert_right(get_right_child(r), 'f')
    print(r)


def build_tree2():
    r = binary_tree('a')
    insert_left(r, 'b')
    insert_right(get_left_child(r), 'd')
    insert_right(r, 'f')
    insert_right(r, 'c')
    insert_left(get_right_child(r), 'e')
    print(r)


def test():
    r = binary_tree(3)
    insert_left(r, 4)
    insert_left(r, 5)
    insert_right(r, 6)
    insert_right(r, 7)
    l = get_left_child(r)
    print(l)

    set_root_val(l, 9)
    print(r)
    insert_left(l, 11)
    print(r)
    print(get_right_child(get_right_child(r)))


def main():
    # test()
    build_tree()
    build_tree2()


if __name__ == '__main__':
    main()
