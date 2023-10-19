from response import get_zalando_response

# in input un'imagine, enpoint, key del cognitive services

VISION_ENDPOINT = "https://testservice000.cognitiveservices.azure.com/"
VISION_KEY = "17c559cb3dcb4d88af6eceedcc98b552"

path_image = r"C:\Users\GabinStewellSimoKams\Desktop\AI-moda\HttpTrigger1\58ae0427a1e90ff8f7b5f1ec8a4c4be6.jpg"



get_zalando_response(VISION_ENDPOINT,VISION_KEY,path_image)