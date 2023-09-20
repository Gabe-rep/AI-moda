from ImageAnalysis import*
import re

def prod ():
    tags = image_analysis() 
    #print (tags)

    #salvare tutti i tags in un file txt
    with open(r"C:\Users\GabinStewellSimoKams\Desktop\AI-moda\HttpTrigger1\file.txt", "w") as f:
        for tags in tags:
            f.write("%s\n" % tags)
    #estrare la parola da cercare
    filepath = r"C:\Users\GabinStewellSimoKams\Desktop\AI-moda\HttpTrigger1\file.txt"
    fileObject = open(filepath, 'r',encoding = 'utf-8')
    txt_html = fileObject.read()
    print (txt_html)

    # estrazione del vestito con filtro 
    try :
        prod = [req for req in re.findall(r"(?<=)wearing a(.*?)and", txt_html)][0]
        print(prod)
        return prod
    except :
        IndexError



