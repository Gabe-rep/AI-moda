from ImageAnalysis import*
import re

def prod():
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
    #print (txt_html)
    # estrazione del vestito con filtro
    try :
        prod1 = [req for req in re.findall(r"(?<=)wearing a(.*)", txt_html)]
        #print (prod1)
        prod2 = [req for req in re.findall(r"(?<=)up of a(.*)", txt_html)]
        #print (prod2)
        prod3 = [req for req in re.findall(r"(?<=)pair of(.*)", txt_html)]
        #print (prod3)
        prod4 = [req for req in re.findall(r"(?<=)in a(.*)", txt_html)]
        #print (prod4)
        prod5 = [req for req in re.findall(r"(?<=)a pair of(.*?)with", txt_html)]
        #print (prod5)
        lista_prod = [prod1, prod2, prod3, prod4, prod5]
        return lista_prod
    except :
        IndexError
    
    


