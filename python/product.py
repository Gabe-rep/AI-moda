from ImageAnalysis import*
import re

def prod ():
    tags = image_analysis() 
    #print (tags)
    
    #salvare tutti i tags in un file txt
    with open('file.txt', 'w') as f:
        for tags in tags:
            f.write("%s\n" % tags)

    #estrare la parola da cercare
    filepath = r"C:\Users\GabinStewellSimoKams\Desktop\AI-moda\file.txt"
    fileObject = open(filepath, 'r',encoding = 'utf-8')
    txt_html = fileObject.read()
    print (txt_html)
    try :
        prod = [req for req in re.findall(r"(?<=)wearing a(.*)", txt_html)][0]
        print (prod)
    except :
        IndexError



