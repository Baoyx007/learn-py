# -*- coding: utf-8 -*-
__author__ = 'PCPC'


# #
# class Flip:
#     def flipChess(self, A, f):
#         # write code here
#         markPo = {}
#         for it in f:
#             if checkBound(it[0] + 1, it[1]):
#                 markPo[]
def Find(self, array, target):
    # write code here
    row_index = (len(array) // 2) - 1
    col_index = 0
    col_length = len(array)
    while row_index >= 0 and col_index <= col_length - 1:
        if target == array[row_index][col_index]:
            return True
        elif target < array[row_index][col_index]:
            row_index -= 1
        else:
            col_index += 1
    return False
