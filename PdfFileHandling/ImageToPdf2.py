import img2pdf

# open the pdf file
file = open("./PdfFileHandling/myreport.pdf", "wb")

# convert the list of images and paste to the pdf file
file.write(img2pdf.convert(['./PdfFileHandling/image.png', './PdfFileHandling/sample.png']))

# close the pdf file
file.close()
