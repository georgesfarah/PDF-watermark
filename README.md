# PDF-watermark
## How to use:

-copy your PDFs to the src folder.  
-add your watermark to this directory and name it watermark.pdf  
-run the script,the output files will be generated in dest folder  


### Note:
-you need to install PyPDF2: pip install PyPDF2  
-by default the watermark is 80% the height of the pdf, you can change it in the script(change value of variable factor)  
-you can scale the watermark using the pdf's width by changing the value of scaleX to True.  
-by default output files are not compressed, you can change it in the script(change value of compress to True,you need ghostscript installed on your machine and add its bin folder to environment variables path)     
-I used my course materials to showcase the script.all rights are reserved to their owners.  

### How to create watermark.pdf:

-open your image in photoshop  
-change layer opacity to 30%  
-save as: watermark.pdf  
