import cv2 as cv
#resmi oku
img = cv.imread('valorant.png')
#görüntünün boyularını al (yükseklik ve genişlik)
print(img.shape)
height,width=img.shape[:2]
print("Genişlik ve yükseklik",height,width)
print(f'Görüntü yüksekliği: {height}')
print(f'Görüntü genişliği: {width}')
#diğer türlü print("Genişlik ve yükseklik",img.shape[1],img.shape[0])

cahannels=img.shape[2]
print(f'Kanal Sayısı {cahannels}')
print(f'Veri tipi: {img.dtype}')

cv.imshow("picture",img)
cv.waitKey(0)
cv.destroyAllWindows()

