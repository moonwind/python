import xlrd
import xlwt
from datetime import datetime
excel = xlrd.open_workbook("D:\\ex.xls")
sheet = excel.sheets()[0]
print(sheet.row_values(0))
print(sheet.col_values(0))

print(sheet.nrows)



from time import *
from xlwt.Workbook import *
from xlwt.Style import *

style = XFStyle()

wb = Workbook()
ws0 = wb.add_sheet('0')

colcount = 200 + 1
rowcount = 60 + 1

t0 = time()
print("\nstart: %s" % ctime(t0))

print("Filling...")
for col in xrange(colcount):
    print(col) 
    for row in xrange(rowcount):
        #ws0.write(row, col, "BIG(%d, %d)" % (row, col))
        ws0.write(row, col, "BIG")

t1 = time() - t0
print("\nsince starting elapsed %.2f s" % (t1))

print("Storing...")
wb.save('D:\\big-16Mb.xls')

t2 = time() - t0
print("since starting elapsed %.2f s" % (t2))

w = Workbook()
ws = w.add_sheet('Image')
ws.insert_bitmap('C:\\Users\\Li\\Downloads\\xlwt-1.0.0\\xlwt-1.0.0\\examples\python.bmp', 2, 2)
ws.insert_bitmap('C:\\Users\\Li\\Downloads\\xlwt-1.0.0\\xlwt-1.0.0\\examples\python.bmp', 10, 2)

w.save('D:\\image.xls')
