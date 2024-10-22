import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open('stinkbug.png'))
# print(repr(img))
imgplot = plt.imshow(img)

ii = img[:, :, 0]

plt.show()
