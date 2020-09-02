from PyPDF2 import PdfFileWriter, PdfFileReader
from os import listdir
from decimal import Decimal

def create_watermark(input_pdf):
    scaleX=True
    factor=0.8
    
    watermark_obj = PdfFileReader('watermark.pdf')
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = PdfFileReader('src/'+input_pdf)
    pdf_writer = PdfFileWriter()

    # Watermark all the pages
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)        
        factor1=Decimal(factor)
        scale=0
        if(scaleX==True):
            scale=Decimal((page.mediaBox.getWidth()/watermark_page.mediaBox.getWidth()))*factor1
        else:
            scale=Decimal((page.mediaBox.getHeight()/watermark_page.mediaBox.getHeight()))*factor1
            
        tx=(page.mediaBox.getWidth()-watermark_page.mediaBox.getWidth()*scale)/2
        ty=(page.mediaBox.getHeight()-watermark_page.mediaBox.getHeight()*scale)/2            

        page.mergeScaledTranslatedPage(watermark_page,scale,tx,ty,False)
        pdf_writer.addPage(page)

    with open('dest/'+input_pdf, 'wb') as out:
        pdf_writer.write(out)


for elm in listdir('src'):
    create_watermark(elm)




