from yandex import Translater
import requests
 
 
 
while True:
    ex = input("lütfen ceviri gir :")
    tr = Translater()
    tr.set_key('trnsl.1.1.20150402T161203Z.4171d3e9fde51a72.f0e40825e77f19dedb9cbc700a89cb9e63a67673') # Api key found on https://translate.yandex.com/developers/keys
    tr.set_from_lang('en')
    tr.set_to_lang('tr')
    tr.translate()
    tr.set_text(ex)
    print (tr.translate())
