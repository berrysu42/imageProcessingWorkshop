import cv2 as cv

# Dosya yollarını tam ve doğru şekilde belirtin
resim_path = r'valorant.png'
resim_path2 = r'foto.jpeg'

# Görüntüleri yükleme
img_color = cv.imread(resim_path, 1)
img_gray = cv.imread(resim_path, cv.IMREAD_GRAYSCALE)
img2 = cv.imread(resim_path2, 0)
img3 = cv.imread(resim_path2, 0)

# Hataları kontrol etme
if img_color is None:
    print("Renkli görüntü yüklenemedi.")
if img_gray is None:
    print("Siyah beyaz görüntü yüklenemedi.")
if img2 is None:
    print("İkinci siyah beyaz görüntü yüklenemedi.")
if img3 is None:
    print("Üçüncü siyah beyaz görüntü yüklenemedi.")
else:
    # Görüntüleri gösterme
    cv.imshow("Renkli", img_color)
    cv.imshow("Siyah Beyaz", img_gray)
    cv.imshow("Siyah beyaz foto", img2)
    cv.imshow("Beriaka", img3)

cv.waitKey(0)
cv.destroyAllWindows()
