import cv2
img = cv2.imread("gato_pipoca.JPG", cv2.IMREAD_COLOR)


enhance = cv2.detailEnhance(img)
canny = cv2.Canny(enhance, 80, 200)

cv2.imshow('gato', canny)

cv2.imwrite('gato_pipoca_novo.JPG', canny)
print('Imagem Salva no Disco')

cv2.waitKey(0)
cv2.destroyAllWindows()

