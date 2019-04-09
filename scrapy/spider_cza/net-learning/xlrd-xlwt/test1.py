import os,xlrd, xlwt
"""
1、打开一个文件对象。
data = xlrd.open_workbook(filename)
2、获取页表
2.1、通过索引顺序获取
table = data.sheets()[0]
table = data.sheet_by_index(0)
2.2、通过名字获取
table = data.sheet_by_name(sheet_name)

获取book中所有工作表的名字
names = data.sheet_names()

行的操作（列参考行）
nrows = table.nrows  #获取该sheet中的有效行
table.row(i)  #返回该行中所有单元格对象组成的列表
table.row_values(i)  #返回由该行中所有单元格的数据组成的列表

单元格的操作
table.cell(r,x)  #返回单元格的对象
table.cell_type(r,x)  #返回单元格中的数据类型
table.cell_value(r,x)  #返回单元格中的数据
table.write_merge(x, x + p, y, n + q, string, style)  #x表示行，m表示行数，y为列，string表示要写入的内容，style表示样式
"""

current_path = os.path.dirname((os.path.abspath(__file__)))
resFilename = (os.sep).join([current_path, 'database', 'database.xlsx'])

if __name__ == "__main__":
    filename = 'database.xlsx'
    rData = xlrd.open_workbook(filename)
    table = rData.sheet_by_name('database')
    nrows = table.nrows
    nclos = table.ncols
    print(nrows,nclos)
    # for i in range(nrows):
    #     print(table.row_values(i))

    # wData = xlwt.Workbook()
    # sheet1 = wData.add_sheet('database')
    # for i in range(nrows):
    #     r = table.row_values(i)
    #     for d in range(len(r)):
    #         sheet1.write(i, d, r[d])
    # wData.save(resFilename)