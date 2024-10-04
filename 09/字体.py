from openpyxl.workbook import Workbook
from openpyxl.styles import Alignment, Font

wb = Workbook()
sheet0 = wb.worksheets[0]

cell = sheet0.cell(row=2, column=2)
cell.value = "我是中国人"
cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
# 设置字体颜色、大小、样式
cell.font = Font(color='FF0000', size=40, name='仿宋')

wb.save('files/p7.xlsx')