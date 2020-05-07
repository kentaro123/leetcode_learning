def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummyHead = ListNode(0);
    curNode = dummyHead

    if not l1 and not l2: return None
    elif not l1:          return l2
    elif not l2:          return l1

    co = 0 # carry over from the previous node
    while l1 or l2:
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        sum += co
        co  = sum / 10
        sum = sum % 10

        curNode.next = ListNode(sum)
        curNode = curNode.next

    if co == 1:
        curNode.next = ListNode(1)

    return dummyHead.next
