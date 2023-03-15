import numpy as np
import cv2

# Завантаження двох зображень
img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image2.jpg')

# Перетворення типу даних на float32
img1 = img1.astype(np.float32)
img2 = img2.astype(np.float32)

# Віднімання кольорів для кожного кольору R, G, B окремо
result_img = np.zeros_like(img1)
for i in range(3):
    result_img[:,:,i] = img1[:,:,i] - img2[:,:,i]

# Перетворення типу даних на uint8
result_img = np.clip(result_img, 0, 255)
result_img = result_img.astype(np.uint8)

# Відображення результату
cv2.imshow('Result', result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
