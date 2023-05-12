from stegano import lsb
from stegano import exifHeader
from steganocryptopy.steganography import Steganography

def shorthandPng(fili, message):
    file_name = fili.split('.')[0]
    secret = lsb.hide(fili, message) # 'img/boy.jpg', 'welcome to the club!'
    secret.save(f'{file_name}-secret.png')
    
    result = lsb.reveal(f'{file_name}-secret.png')
    print(result)

def shorthandAny(fili, to_fili, message):
    sercet = exifHeader.hide(fili, to_fili, message) # 'img/boy.jpg', 'img/boy-secret.jpg', 'привет, пидр'

    result = exifHeader.reveal(to_fili) #  'img/boy-secret.jpg'
    result = result.decode()
    print(result)

typi = input('jpg or png: ')
url = input('path to file: ')
if typi != 'png':
    to_url = input('path to secret-file: (you must create copy file) ')

if typi != 'png':
    message = input('message: (if png only english) ')
else:
    message = input('message: ')

if typi == 'png':
    shorthandPng(url, message)
else:
    shorthandAny(url, to_url, message)


# ==============================================

# Steganography.generate_key("")
# secret = Steganography.encrypt("key.key", "img/Puh.png", "secter.txt")
# secret.save('img/Puh-2.png')

# result = Steganography.decrypt("key.key", "img/Puh-2.png")

