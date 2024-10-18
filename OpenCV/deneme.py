import cv2 as cv

# Görüntüyü tam dosya uzantısıyla birlikte okumalısınız
img1 = cv.imread('foto.jpeg') # '.jpg' uzantısını ekledim
#.png örneği
#img2 = cv.imread('valorant.png')
print(img1) #resmi okuma matris
#print(img2.shape)
#print(img[300:400, :])  belirli bir kısmı göster
# img'nin düzgün yüklendiğini kontrol edelim


if img1 is None:
    print("Görüntü yüklenemedi.")
else:
    # Pencere ismi ve img parametreleri verilerek gösterim yapılır
    cv.imshow('Picture', img1)
    cv.waitKey(0)
    cv.destroyAllWindows()
"""
if img2 is None:
    print("Görüntü yüklenemedi.")
else:
    # Pencere ismi ve img parametreleri verilerek gösterim yapılır
    cv.imshow('Picture', img2)
    cv.waitKey(0)
    cv.destroyAllWindows()


"""










# print("Sürüm",cv2.__version__)

