from itertools import combinations
from functools import reduce
import time, datetime

########################################################################################################################
# Problem
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
def job_scheduler(function_name, wait_time):
    print('Entered scheduler function ' + str(datetime.datetime.now()))
    time.sleep(wait_time * 0.001)
    print('Running function ' + str(datetime.datetime.now()))
    function_name()

def echo_name():
    print ('My name is aceme007')

# job_scheduler(echo_name, 5000)

########################################################################################################################
# Problem
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?
def largest_sum(input_list):
    max_sum_temp = 0

    def max_sum(arr, i):
        if i == 0:
            return arr[0]
        if i == 1:
            return max(arr[0], arr[1])
        return max(max_sum(arr, i-1), arr[i] + max_sum(arr, i-2))

    for i in range(len(input_list)):
        max_so_far = max_sum(input_list, i)
        max_sum_temp = max(max_sum_temp, max_so_far)
    return max_sum_temp


assert largest_sum([2, 4, 6, 2, 5]) == 13
assert largest_sum([5, 1, 1, 5]) == 10


########################################################################################################################
# Problem
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1




########################################################################################################################
# Problem
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

def count_message_decoded(message):
    combo = []
    for i in range(1, len(message)+1):
        a = list(set([ex for ex in combinations(message, i)]))
        combo.extend(a)
    return len(set(combo))
assert count_message_decoded('111') == 3

########################################################################################################################
# Problem 5
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    return pair(lambda x, y: x)

def cdr(pair):
    return pair(lambda x, y: y)

assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4

########################################################################################################################
# Problem 4
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def missing_lowest_int(input_list) -> int:
    min_missing_postive_int_so_far = 1
    for i in input_list:
        if i == min_missing_postive_int_so_far:
            min_missing_postive_int_so_far += 1
        elif i > 0:
            min_missing_postive_int_so_far = min(i+1, min_missing_postive_int_so_far)
    return min_missing_postive_int_so_far

input_list = [3, 4, -1, 1]
assert missing_lowest_int(input_list) == 2
input_list = [1, 2, 0]
assert missing_lowest_int(input_list) == 3

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
