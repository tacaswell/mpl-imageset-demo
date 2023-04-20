import numpy as np
import matplotlib.pyplot as plt

from matplotlib.testing.decorators import image_comparison


@image_comparison(["scatter"], style="mpl20")
def test_scatter():
    fig, ax = plt.subplots()
    ax.scatter(range(5), range(5))


@image_comparison(["hist.png"], style="mpl20")
def test_hist():
    np.random.seed(19680801)
    fig, ax = plt.subplots()
    ax.hist(np.random.randn(1000))
