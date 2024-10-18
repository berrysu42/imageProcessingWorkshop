#kırmızı rengi yeşile çevirme
import cv2 as cv
img_bgr = cv.imread('foto.jpeg')

cv.imshow("Foto",img_bgr)
b,g,r=cv.split(img_bgr)

#kırmızı ve yeşil kanallarını birleştirme
img_new=cv.merge((b,r,g))

#yeşil renkli fotoyu göster
cv.imshow("Yeşil Resim",img_new)


cv.waitKey(0)
cv.destroyAllWindows()