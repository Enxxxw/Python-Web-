from openpyxl.workbook import Workbook
from openpyxl.styles import Border, Side, Alignment

wb = Workbook()
sheet0 = wb.worksheets[0]

cell = sheet0.cell(row=2, column=2)
cell.value = "我是中国人"
cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
cell.border = Border(
    top = Side(style='thin', color='000000'),
    right = Side(style='medium', color='0000FF'),
    left = Side(style='medium', color='0000FF'),
    bottom = Side(style='thin', color='000000'),
)

wb.save('files/p6.xlsx')