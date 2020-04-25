'''this script gets list of non explored links and stores them on stack'''

import stack
import bookMarkLoad

def initStack():
    Stacklist = stack.Stack()
    toExploreList = bookMarkLoad.getList()

    for ele in toExploreList:
        if ele.status=='n':
            Stacklist.push(ele)
    return Stacklist

Stacklist=initStack()
