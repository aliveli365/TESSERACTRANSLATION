import pytesseract
from PIL import Image
from yandex import Translater


def donusturme (img):
    img = Image.open(img)
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
    result = pytesseract.image_to_string(img)
    tr = Translater()
    tr.set_key('KEY') # Api key found on https://translate.yandex.com/developers/keys
    tr.set_from_lang('en')
    tr.set_to_lang('tr')
    tr.translate()
    tr.set_text(result)
    with open("magic.txt",mode="w")as file:
        file.write(tr.translate())
        file.close()
        print(">ceviri tamamlandı...")
    return
    



while (True):
    resim = input("resim ekle :")
    donusturme(resim)
    

