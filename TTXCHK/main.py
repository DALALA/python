#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 2013/12/10

@author: Robert
'''
import win32com.client
import sys
gini = 0x9a
ginc = 0xbc
gopd = 0x5a
glen = int(sys.argv[1])
gdn  = 0x00
temp = 0x00
def OutputToXls(sheet,row,data):
    for col in range(len(data)):
        cell = sheet.Cells(row,col+1)
        cell.NumberFormat = "@"
        cell.Value = data[col]

xlsApp = win32com.client.Dispatch("Excel.Application")
xlsApp.Visible = False
xlsWorkBook = xlsApp.Workbooks.Add()
xlsWorkSheet = xlsWorkBook.Worksheets.Add()
note1 = ["HDR0","HDR1","CTL","OPC","LEN","ini","inc","opd","len","dX"]
rlt = ["FF","FF","12","67"]
rlt.append("%02X" % (glen+4))
rlt.append("%02X" % gini)
rlt.append("%02X" % ginc)
rlt.append("%02X" % gopd)
rlt.append("%02X" % glen)
gdn = ((gini+ginc) ^ gopd)&0xFF
#print ("(%02x+%02x)^%02x=%02x"%(gini,ginc,gopd,gdn))
for row in range(glen):
#    cell = xlsWorkSheet.Cells(1,row)
#    cell.NumberFormat = "@"
#    cell.Value = "%02x" % gdn
    rlt.append("%02X" % gdn)
    temp = gdn
    gdn = ((gdn+ginc) ^ gopd)&0xFF
    #print ("(%02x+%02x)^%02x=%02x"%(temp,ginc,gopd,gdn))
rlt.append("CS")
#print rlt   
OutputToXls(xlsWorkSheet,1,note1)
OutputToXls(xlsWorkSheet,2,rlt) 
xlsWorkBook.Close(True,r'D:\TXCHK.xlsx')
xlsApp.Quit()
del xlsApp
