from PyPDF2 import PdfFileWriter, PdfFileReader
from fpdf import FPDF

def createWaterMark(Y, X, Font, Size, Text):
    pdf = FPDF(format='Letter')
    pdf.add_page()
    pdf.set_font(Font, size=Size)
    pdf.set_text_color(0,0,0)
    for count, value in enumerate(Text):
        pdf.text(x=X, y=(Y+6*count), txt=value)
    pdf.output("watermark.pdf")

def createPDF(Y=5, X=5, Font='Arial', Size=10, target_page=2, Text="Default watermark"):
    createWaterMark(Y, X, Font, Size, Text)
    output = PdfFileWriter()
    input = PdfFileReader(open("2022-07-11_Patient Date of Birth.pdf", "rb"))
    watermark = PdfFileReader(open("watermark.pdf", "rb"))

    for page in range(0,input.getNumPages()):
        current_page = input.getPage(page)
        if page == target_page - 1:
            current_page.mergePage(watermark.getPage(0))

        output.addPage(current_page)

    outputStream = open("new_file.pdf", "wb")
    output.write(outputStream)
    outputStream.close()