// Do not forget to instal: pip3 install translate
from translate import Translator

translator= Translator(to_lang="ja")

try:
    text_for_translate = input("Write here the sentence in English you want to translate: ")
    with open('test.txt', mode = 'w') as init_file:
        init_file = init_file.write(text_for_translate)
    with open('test.txt', mode = 'r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('testJA.txt', mode = 'w') as tran_file:
            tran_file = tran_file.write(translation)
except FileExistsError:
    print("Check your file path!")
