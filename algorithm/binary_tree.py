class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.number_elements = 0

    def insert(self, value):
        self.number_elements +=1

        if self.value:
            if value > self.value:
                if self.right is None:
                    self.right = BinaryTreeNode(value)
                else:
                    self.right.insert(value)
            else:
                if self.left is None:
                    self.left = BinaryTreeNode(value)
                else:
                    self.left.insert(value)
        else:
            self.value = value

    
def print_tree(node: BinaryTreeNode, level=0):
    if node != None:
        print_tree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.value)
        print_tree(node.right, level + 1)

def sort_tree(tree: BinaryTreeNode):
    if tree.left is not None:
        print(sort_tree(tree.left))
    if tree.value is not None:
        print(tree.value)
    if tree.right is not None:
        print(sort_tree(tree.right))

if __name__ == "__main__":
    array_to_sort = [8,21,11,23,1,3,2,8,52,45,53,9]
    root = BinaryTreeNode(12)

    for value in array_to_sort:
        root.insert(value)
    print_tree(root)
    sort_tree(root)



