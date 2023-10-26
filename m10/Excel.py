# import xlsxwriter
#
# # 创建新的Excel文件并添加工作表
# workbook = xlsxwriter.Workbook('demo.xlsx')
# worksheet = workbook.add_worksheet()
#
# # 加宽第一列，使文字更清楚
# worksheet.set_column('A:A', 20)
#
# # 添加用于高亮显示单元格的粗体格式
# bold = workbook.add_format({'bold': True})
#
# # 写一些简单的文字
# worksheet.write('A1', 'Hello')
#
# # 带格式的文本
# worksheet.write('A2', 'World', bold)
#
# # 写一些数字，用行/列表示法
# worksheet.write(2, 0, 123)
# worksheet.write(3, 0, 123.456)

# 插入图像
# worksheet.insert_image('B5', 'logo.png')

# workbook.close()

import xlsxwriter

today = xlsxwriter.Workbook("今天.xlsx")
sheet1 = today.add_worksheet("乘法")
for x in range(0, 100000):
    sheet1.write(x, 0, x + 1)
s=0
for i in range (0,100000):
    s = s + i+1
sheet1.write(0, 1, s)
today.close()
