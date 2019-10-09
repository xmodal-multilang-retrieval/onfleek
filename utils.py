
from datetime import datetime
from typing import Tuple

import numpy as np
import pytz
from matplotlib import pyplot as plt


LOCAL_TIMEZONE = pytz.timezone("America/Sao_Paulo")


def get_current_datetime():
    right_now = datetime.now()
    right_now = right_now.replace(tzinfo=pytz.UTC)
    right_now = right_now.astimezone(LOCAL_TIMEZONE)
    return right_now


def show_image(image: np.ndarray, figure_size: Tuple[int, int] = (8, 8)):
    plt.figure(figsize=figure_size)
    plt.imshow(image)
    plt.show()
