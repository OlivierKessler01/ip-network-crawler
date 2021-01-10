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

def generate_sorted_array(tree : BinaryTreeNode, array : list) -> list:
    if tree.left is not None:
        array.append(generate_sorted_array(tree.left, array))
    if tree.value is not None:
        array.append(tree.value)
    if tree.right is not None:
        array.append(generate_sorted_array(tree.right, array))
    return array

def build_bst_balanced(bst : BinaryTreeNode, array):
    left_array = array[0:round(len(array)/2):1]
    right_array = array[round(len(array)/2)+1:len(array)-1:1]
    if len(left_array) > 0:
        bst.left = build_bst_balanced(BinaryTreeNode(round(len(left_array)/2)), left_array)
    bst.value = array[round(len(array)/2)]
    if len(right_array) > 0:
        bst.right = build_bst_balanced(BinaryTreeNode(round(len(right_array)/2)), right_array)
    
    return bst
    
def print_tree(node: BinaryTreeNode, level=0):
    if node != None:
        print_tree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.value)
        print_tree(node.right, level + 1)

if __name__ == "__main__":
    unsorted_array = [1,2,3,4,5,6,7,8,9,18,11,23]
    bst = BinaryTreeNode(12)
    bst_balanced = BinaryTreeNode(12)
    for value in unsorted_array:
        bst.insert(value)

    sorted_array = []
    generate_sorted_array(bst, sorted_array)
    build_bst_balanced(bst_balanced, sorted_array)
    print_tree(bst_balanced)
    

