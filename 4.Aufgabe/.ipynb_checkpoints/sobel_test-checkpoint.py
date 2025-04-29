import sobel_demo as nd
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import time


def rgb_2_gray(img, mode='lut'):
    if mode == 'lut':
        return np.round(img[:,:,0] * 0.2126 + img[:,:,1] * 0.7152 + img[:,:,2] * 0.0722)
    else:
        return np.round(img[:,:,0] * 0.2126 + img[:,:,1] * 0.587 + img[:,:,2] * 0.114)


img = io.imread("lena.jpg")
gray = rgb_2_gray(img).astype("float64")

# TODO: define filters in x in y direction
filter_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
], dtype=np.float64)

filter_y = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
], dtype=np.float64)


start = time.time()
# TODO: filter image in x direction (nd.sobel(gray, filter_x))
filtered_x = nd.sobel(gray, filter_x)
end = time.time()
duration = end-start
print("Duration in milliseconds: ", duration*1000)


# Plot both results
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Sobel X (Horizontal Edges)")
plt.imshow(sobel_x, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Sobel Y (Vertical Edges)")
plt.imshow(sobel_y, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

start = time.time()
# TODO: filter image in y direction (nd.sobel(gray, filter_y))
filtered_y = nd.sobel(gray, filter_y)
end = time.time()
duration = end-start
print("Duration in milliseconds: ", duration*1000)

# TODO compute Gradient magnitude