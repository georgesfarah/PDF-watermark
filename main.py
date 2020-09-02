from PyPDF2 import PdfFileWriter, PdfFileReader
from os import listdir, system, remove, path, mkdir
from decimal import Decimal

scaleX=True
factor=0.8
compress=False

def create_watermark(input_pdf):
    
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

    if(compress==False):
        with open('dest/'+input_pdf, 'wb') as out:
            pdf_writer.write(out)
            
    else:
        if path.exists('dest_tmp')==False:
            mkdir('dest_tmp')
        input_pdf=input_pdf.replace(" ", "_")
        with open('dest_tmp/'+input_pdf, 'wb') as out:
            pdf_writer.write(out)
            
        output='dest/'+input_pdf
        system('gswin64c -q -dNOPAUSE -dBATCH -dSAFER -dSimulateOverprint=true -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -dEmbedAllFonts=true -dSubsetFonts=true -dAutoRotatePages=/None -dColorImageDownsampleType=/Bicubic -dColorImageResolution=150 -dGrayImageDownsampleType=/Bicubic -dGrayImageResolution=150 -dMonoImageDownsampleType=/Bicubic -dMonoImageResolution=150 -sOutputFile='+output+' dest_tmp/'+input_pdf)
        remove('dest_tmp/'+input_pdf)

######################################################## Main
if path.exists('dest')==False:
    mkdir('dest')
       
for elm in listdir('src'):
    create_watermark(elm)

if(path.exists('dest_tmp')==True):
    system('rmdir dest_tmp')




