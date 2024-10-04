from openpyxl import load_workbook
import os

wb_path = os.path.join("files", "p10.xlsx")
wb_object = load_workbook(wb_path)
sheet_obj = wb_object.worksheets[0]

# idx -> 从哪个位置开始
# amount -> 多少个
sheet_obj.delete_rows(7,2)
sheet_obj.delete_cols(2,1)

wb_object.save('files/p14.xlsx')