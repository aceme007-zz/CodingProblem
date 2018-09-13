from itertools import combinations
from functools import reduce

########################################################################################################################
# Problem
#

########################################################################################################################
# Problem
#

########################################################################################################################
# Problem 3
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.
#
# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def insert(self, root, data):
        newNode = Node(data)
        if root == None:
            root = newNode
        elif data < root.val:
            root.left = self.insert(root.left, data)
        elif data > root.val:
            root.right = self.insert(root.right, data)
        return root


def levelOrder(node):
    # BFS
    Q = []
    if node == None:
        return
    else:
        Q.append(node)
        while Q:
            curr = Q[0]
            serialized_array.append (curr.val)
            if curr.left != None:
                Q.append(curr.left)
            if curr.right != None:
                Q.append(curr.right)
            Q.pop(0)

def print_tree(node):
    # DFS
    if node == None:
        return
    print_tree(node.left)
    serialized_array.append(node.val)
    print_tree(node.right)

def serialize(node):
    levelOrder(node)
    return serialized_array

def deserialize(input_list):
    newTree = Node(None)
    root = None
    for each_item in input_list:
        root = newTree.insert(root, each_item)
    return root

serialized_array = []

# newBT = Node(None)
# root = None
# root = newBT.insert(root, 5)
# root = newBT.insert(root, 67)
# root = newBT.insert(root, 1)
# root = newBT.insert(root, 30)
# root = newBT.insert(root, 42)
# root = newBT.insert(root, 92)
# root = newBT.insert(root, 4)

# a = newBT.serialize(root)
# print(a)
# BT2 = Node(None)
# BT2.deserialize(a)
node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

########################################################################################################################
# Problem 2
# Given an array of integers, return a new array such that each element at index i of
# the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

def return_multiplied_array(input_list) -> list:
    product = reduce(lambda x, y : x*y, input_list)
    return [product/each for each in input_list]

def return_multiplied_array_v2(input_list) -> list:
    # without using division
    temp = input_list.copy()
    output_list = []
    for i, val in enumerate(input_list):
        temp[i] = 1
        output_list.append(reduce(lambda x, y: x*y, temp))
        temp[i] = val
    return output_list

input_list = [1, 2, 3, 4, 5]
assert return_multiplied_array(input_list) == [120, 60, 40, 30, 24]
assert return_multiplied_array(input_list) == return_multiplied_array_v2(input_list)
input_list = [3, 2, 1]
assert return_multiplied_array(input_list) == [2, 3, 6]
assert return_multiplied_array(input_list) == return_multiplied_array_v2(input_list)

########################################################################################################################

# Problem 1
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

def return_sum_value(input_list, sum_value) -> bool:
    for var in combinations(input_list, 2):
        if var[0] + var[1] == sum_value:
            return True
        else:
            continue
    return False

input_list = [10, 15, 3, 7]
assert return_sum_value(input_list, 10)
input_list = [1, 5, 5, 10, 15, 3, 7]
assert return_sum_value(input_list, 10)

########################################################################################################################
