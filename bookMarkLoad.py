
'''
this script loads chrome bookmarks into excel file.
format: link=link,status=y/n: y if link already explored, n if to be explored
'''
import pandas
import openpyxl
import json
import os
## import bookmarks, store in bookmarklist. read from excel. store in excellist. if ele in bookmarklist not in excellist, append ele in excellist. excellist to excel sheet with status='n'

class list:
    link=None
    status=None

    def push(self,link,status):
        self.list=link
        self.status=status

def importBookmarks():
    bookmarkList=[]
    file=open(r"C:\Users\<username>>\AppData\Local\Google\Chrome\User Data\Default\Bookmarks",encoding="utf8")

    filej=json.load(file)
    for ele in filej['roots']['bookmark_bar']['children']:
        temp=list()
        temp.link=ele["url"]
        temp.status='n'
        bookmarkList.append(temp)

    for ele in filej['roots']['other']['children']:
        temp = list()
        temp.link = ele["url"]
        temp.status = 'n'
        bookmarkList.append(temp)

    for ele in filej['roots']['synced']['children']:
        temp = list()
        temp.link = ele["url"]
        temp.status = 'n'
        bookmarkList.append(temp)

    file.close()
    return bookmarkList

def changeName(name):
    os.remove(name)
    os.rename('temp'+name,name)

def readExcel():
    excel_file='bookmarkExcel.xlsx'
    tempList=pandas.read_excel(excel_file)
    excelList=[]
    link=tempList['link']
    status=tempList['status']
    for i in range(len(link)):
        temp=list()
        temp.link=link[i]
        temp.status=status[i]
        excelList.append(temp)

    return excelList

def writeToExcel(excelList):
    excelIndex=2
    excel_file='bookmarkExcel.xlsx'
    file=openpyxl.load_workbook(excel_file)
    sheet=file.worksheets[0]

    for i in range(len(excelList)):
        if 'www.youtube.com' in excelList[i].link:
            sheet['A'+str((excelIndex))]=excelList[i].link
            sheet['B' + str((excelIndex))]=excelList[i].status
            excelIndex+=1
    file.save('temp'+excel_file)

    #change name to bookmarkExcel.xlsx
    changeName('bookmarkExcel.xlsx')

def transfer(bookmarkList,excelList):
    link_list_in_excelList=[]
    #store links in link_list
    for ele in excelList:
        link_list_in_excelList.append(ele.link)

    #check if link in bookmarklist present in link_list
    for ele in bookmarkList:
        if ele.link not in link_list_in_excelList:
            temp=list()
            temp.link=ele.link
            temp.status='n'
            excelList.append(temp)
    return excelList

def getList():
    global excelList
    return excelList

bookmarkList=importBookmarks()
excelList=readExcel()
print(excelList)
excelList=transfer(bookmarkList,excelList)
print(excelList)
writeToExcel(excelList)
