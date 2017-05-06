#-*- coding: UTF-8 -*-
__author__ = 'zuohaitao'

import xlrd
import MySQLdb
import uniout

#注意这里的workbook首字母是小写
data = xlrd.open_workbook('demoSocial.xls')

#查看文件中包含sheet的名称
data.sheet_names()

#得到第一个工作表，或者通过索引顺序 或 工作表名称
table = data.sheets()[0]
table = data.sheet_by_index(0)
#table = data.sheet_by_name(u'Sheet1')

#循环行,得到索引的列表
for rownum in range(table.nrows):

    #print str(table.row_values(rownum))
    print table.row_values(rownum)





    # for i in table.row_values(rownum):
    #     print i[0]

#print data.sheet_names()
if __name__ == '__main__':
    main()