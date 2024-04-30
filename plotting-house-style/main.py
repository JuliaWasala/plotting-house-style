# plotting code I use a lot that i will just dump here for now

import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerPathCollection

# rotate ticks on x-axis

def rotate_xticks():
    """Rotates all the x-ticks in the current figure.
    """
    for tick in plt.gca().get_xticklabels():
            tick.set_rotation(45)
            tick.set_horizontalalignment('right')


def update_legend_markersize(plot, marker_size: int = 36, kwargs: dict = {}):
    """
    function to plot a legend where all markers have a fixed size
    source: https://stackoverflow.com/questions/47115869/how-do-i-change-the-size-of-the-scatter-markers-in-the-legend
    inputs:
        plot: plot to plot the legend for 
            example: plot = plt.scatter(data)
        marker_size: size of the markers in the legend
        kwargs: keyword arguments for plt.legend

    side effects:
        plots a legend with markers of size marker_size
    """

    def _update_prop(handle, orig):
        """
        helper function to resize all markers
        in legend to a fixed size.
        source: https://stackoverflow.com/questions/47115869/how-do-i-change-the-size-of-the-scatter-markers-in-the-legend
        """
        handle.update_from(orig)
        handle.set_sizes([marker_size])

    plt.legend(handler_map={type(plot): HandlerPathCollection(update_func=_update_prop)}, **kwargs)