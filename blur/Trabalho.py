import cv2
img = cv2.imread("gato_dormiu.JPG", cv2.IMREAD_COLOR)


blur = cv2.blur(img, (20, 25))

cv2.imshow('gato', blur)

cv2.imwrite('gato_dormiu_novo.JPG', blur)
print('Imagem Salva no Disco')

cv2.waitKey(0)
cv2.destroyAllWindows()

