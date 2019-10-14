from PIL import Image
from pytesseract import image_to_string  
import os

def start():
    output = []
    path = 'dadjokes'

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.jpg' in file:
                files.append(os.path.join(r, file))

    
    for f in files:
        print("examining "+f)
        sentence = image_to_string(Image.open(f))
        words = sentence.split(" ")
        mention = ""
        for w in words:
            if w[0]=="@"
            mention=w
        if len(words)>2:
            
            d = dict(id=f, mention=mention, sent=sentence)
            print(d)
            output.append(d)
            
        #print image_to_string(Image.open('test-english.jpg'), lang='eng')



if __name__ == '__main__':
   start()
