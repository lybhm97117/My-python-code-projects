"""
File: add2.py
Name: Teresa Tien
------------------------
This program adds two numbers which are stored as
the type of linked-list. Notice that the numbers
are stored reversely, and the length of two linked-list
might be different. After the plus of two numbers, the
result also has to be stored as linked-list reversely.

If you execute this program in terminal, you will the
result like below,
----------test1----------
l1: 2->4->3
l2: 5->6->4
ans: 7->0->8
----------test2----------
l1: 9->9->9->9->9->9->9
l2: 9->9->9->9
ans: 8->9->9->9->0->0->0->1
----------test3----------
l1: 0
l2: 0
ans: 0
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    dummy = ListNode(0)  # 做一個空的節點當作粽子頭
    cur = dummy  # 用來遍歷每一個ＬistNode的指針
    carry = 0  # 儲存進位值
    while l1 or l2 or carry:  # 在l1,l2, or 進位值時持續執行迴圈
        sum_val = carry  # 等等要計算加總後要進位多少次
        if l1:
            sum_val += l1.val  # 將l1節點數值加入到sum中
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next
        carry = sum_val // 10  # 計算進位幾次
        sum_val %= 10  # 取餘數看剩下的個位數字是多少
        cur.next = ListNode(sum_val)  # 現在這個cur節點連向ListsNode(sum)的節點
        cur = cur.next
    return dummy.next
    #######################


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type "python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2)
            l1.next = ListNode(4)
            l1.next.next = ListNode(3)
            l2 = ListNode(5)
            l2.next = ListNode(6)
            l2.next.next = ListNode(4)
            ans = add_2_numbers(l1, l2)
            print('------test1------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------')
        elif args[0] == 'test2':
            l1 = ListNode(9)
            l1.next = ListNode(9)
            l1.next.next = ListNode(9)
            l1.next.next.next = ListNode(9)
            l1.next.next.next.next = ListNode(9)
            l1.next.next.next.next.next = ListNode(9)
            l1.next.next.next.next.next.next = ListNode(9)
            l2 = ListNode(9)
            l2.next = ListNode(9)
            l2.next.next = ListNode(9)
            l2.next.next.next = ListNode(9)
            ans = add_2_numbers(l1, l2)
            print('------test2------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------')
        elif args[0] == 'test3':
            l1 = ListNode(0)
            l2 = ListNode(0)
            ans = add_2_numbers(l1, l2)
            print('------test3------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------')
        else:
            print('Error: Please type "python3 add2.py test1"')


if __name__ == '__main__':
    main()
