import os
import img2pdf

# convert image to pdf
pdfData = img2pdf.convert("./PdfFileHandling/image.png")

# open the pdf file in write binary mode
file = open("./PdfFileHandling/myreport.pdf", "wb")

# paste the image pdf in the pdf file
file.write(pdfData)

# close the pdf file
file.close()
