from openpyxl.workbook import Workbook
from openpyxl.styles import Alignment, Font

wb = Workbook()
sheet0 = wb.worksheets[0]

sheet0.row_dimensions[2].height = 50
sheet0.column_dimensions['B'].width = 50

cell = sheet0.cell(row=2, column=2)
cell.value = "我是中国人"
cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
cell.font = Font(color='FF0000', size=30, name='仿宋')

wb.save('files/p8.xlsx')