import cv2
img = cv2.imread("gato.JPG", cv2.IMREAD_COLOR)


enhance = cv2.detailEnhance(img)
filtered = cv2.edgePreservingFilter(enhance)

cv2.imshow('gato', filtered)

cv2.imwrite('gato_novo.JPG', filtered)
print('Imagem Salva no Disco')

cv2.waitKey(0)
cv2.destroyAllWindows()
