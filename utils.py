
from typing import Tuple

import numpy as np
from matplotlib import pyplot as plt


def show_image(image: np.ndarray, figure_size: Tuple[int, int] = (8, 8)):
    plt.figure(figsize=figure_size)
    plt.imshow(image)
    plt.show()
