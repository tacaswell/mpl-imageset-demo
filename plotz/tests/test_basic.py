import numpy as np
import matplotlib.pyplot as plt

from matplotlib.testing.decorators import image_comparison


@image_comparison(["line"], style="mpl20")
def test_line():
    fig, ax = plt.subplots()
    ax.plot(range(5))


@image_comparison(["image.png"], style="mpl20")
def test_image():
    fig, ax = plt.subplots()
    ax.imshow(np.arange(36).reshape(6, 6))
