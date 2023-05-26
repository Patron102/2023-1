#pillow

from PIL import Image, ImageFilter, ImageEnhance, ImageOps
'''
#img = Image.open("C:/Users/ASUS/Desktop/파이썬 실습/photo/picture01.jpg")
img = Image.open("photo/picture01.jpg")
img.show() #이미지 보이기
img = Image.open("photo/picture01.jpg")
img.save("photo/1.jpg") #이미지를 다른 이름으로 저장

img = Image.open("photo/picture02.jpg")
img.show()
img = img.transpose(Image.FLIP_LEFT_RIGHT) #좌우반전
img.show()

img = Image.open("photo/picture03.jpg")
img.show()
img = img.transpose(Image.FLIP_TOP_BOTTOM) #상하반전
img.show()

img = Image.open("photo/picture05.jpg")
img.show()
img = img.rotate(45, expand=True) #사진 돌리기
#img = img.rotate(45)
img.show()

img = Image.open("photo/picture52.jpg")
img.show()
img = img.crop((100, 100, 600, 600)) #(x1,y1) (x2, y2)만큼 그림 자르기
img.show()

img = Image.open("photo/picture06.jpg")
img.show()
img = ImageEnhance.Brightness(img).enhance(3) #밝기 조절(어둡게 할땐 0.0~1.0)
img.show()

img = Image.open("photo/picture55.jpg")
img.show()
img = ImageOps.grayscale(img) #흑백으로 만들기
img.show()

img = Image.open("photo/picture56.jpg")
img.show()
img = img.filter(ImageFilter.EMBOSS) #엠보싱 효과
img.show()

img = Image.open("photo/picture73.jpg")
img.show()
img = img.filter(ImageFilter.CONTOUR) #연필효과?
img.show()

img = Image.open("photo/picture24.jpg")
img.show()
img = img.filter(ImageFilter.FIND_EDGES) #경계선 추출
img.show()
'''

#실습
'''
img = Image.open("photo/picture85.jpg") #파일 불러오기
img = img.transpose(Image.FLIP_TOP_BOTTOM) #상하반전
img = img.rotate(45, expand=True) #45도 돌리기
img = img.filter(ImageFilter.CONTOUR) #연필효과?
img.show()
'''

import random as r

randNum = r.randint(1,99)

if randNum <= 9:
	randNum = str(f"0{randNum}")
else:
	randNum = str(randNum)

img = Image.open(f"photo/picture{randNum}.jpg")
img.show()
img = img.transpose(Image.FLIP_TOP_BOTTOM)
img.show()
img = img.rotate(45, expand=True)
img.show()
img = img.filter(ImageFilter.FIND_EDGES)
img.show()