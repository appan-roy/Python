from openpyxl import Workbook

# create a workbook object
wb = Workbook()

# create the sheet
wb['Sheet'].title = "Frameworks"

# activate the sheet
sht = wb.active

# declare the data in a list of tuple
data = [('Sl No', 'Prog Language', 'Status'), (1, 'Python', 'Active'), (2, 'Java', 'Inactive'), (3, 'JavaScript', 'Inactive')]

# write data into cells
for item in data:
    sht.append(item)

# save the workbook
wb.save("./ExcelHandling/FinalReport2.xlsx")