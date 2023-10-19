from ImageAnalysis import*
import re

def prod(VISION_ENDPOINT,VISION_KEY,path_image):
    tags = image_analysis(VISION_ENDPOINT,VISION_KEY,path_image)
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
        prod1 = list(set([req for req in re.findall(r"(?<=)wearing a(.*)", txt_html)]))
        #print (prod1)
        prod2 = list(set([req for req in re.findall(r"(?<=)up of a(.*)", txt_html)]))
        #print (prod2)
        prod3 = list(set([req for req in re.findall(r"(?<=)in a(.*)", txt_html)]))
        #print (prod4)
        prod4 = list(set([req for req in re.findall(r"(?<=)a pair of(.*?)with", txt_html)]))
        #print (prod5)
        return prod1, prod2, prod3, prod4
    except :
        IndexError



