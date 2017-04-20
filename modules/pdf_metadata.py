
from imports import *

def metadata():
    path=ask_for_pdf()
    try:
        pdfFile=PdfFileReader(open(path,'rb'))
    except:
        print("\nNo pdf was found")
        return
    metadatas=pdfFile.getDocumentInfo()
    print("\nMetadatas:")
    print("----------------------------")
    #metadatas is none, check first
    if(metadatas is not None):
        for data in metadatas:
            print("[+]"+data+ ":"+metadatas[data])

    print (colored.yellow("\n<Enter>\n"))
    input()
