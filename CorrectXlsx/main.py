'''
Created on 2013/12/11

@author: Robert
'''
import win32com.client
import sys
xlsApp = win32com.client.Dispatch("Excel.Application")
xlsApp.Visible = False
for file in sys.argv[1:]:
    print file
    xlsWorkBook = xlsApp.WorkBooks.Open(file)
    for CurrSheetNum in range(xlsWorkBook.WorkSheets.Count):
        CurrSheet = xlsWorkBook.WorkSheets[CurrSheetNum]
        for row in range(1,300):
            for col in range(1,300):
                cell = CurrSheet.Cells(row,col)
                cell.NumberFormat = "@"
                int_value = "%s" % cell.Value
                if(int_value.find(".")!=-1):
                    int_value = int_value[:int_value.find(".")]
                    int_value = int(int_value,16)
                    cell.Value = "%02X" % int_value
                

    xlsWorkBook.Close(True)
xlsApp.Quit()
del xlsApp
