import PyPDF2

# open pdf file in read binary mode
file = open("./PdfFileHandling/About Agatha.pdf", "rb")

# read pdf file
reader = PyPDF2.PdfFileReader(file)

# print number of pages
print(reader.numPages)

# get first pdf page
page1 = reader.getPage(0)

# extract pdf data
pdfData = page1.extractText()

# print pdf data
print(pdfData)

# assert pdf text
assert "piano" in pdfData, "Text not found"

# close the pdf file
file.close()