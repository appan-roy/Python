from openpyxl import Workbook

# create a workbook object
wb = Workbook()

# create the sheet
wb['Sheet'].title = "Frameworks"

# activate the sheet
sht = wb.active

# write data into cells
sht['A1'].value = "Name"
sht['B1'].value = "Status"
sht['A2'].value = "Python"
sht['B2'].value = "Active"
sht['A3'].value = "Java"
sht['B3'].value = "Inactive"
sht['A4'].value = "JavaScript"
sht['B4'].value = "Inactive"

# save the workbook
wb.save("./ExcelHandling/FinalReport.xlsx")