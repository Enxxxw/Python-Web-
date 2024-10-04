from openpyxl.workbook import Workbook
from openpyxl.styles import Alignment, Font

wb = Workbook()
sheet = wb.worksheets[0]

cell = sheet.cell(row=1, column=1)
res = cell.coordinate
print(res)
