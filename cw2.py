import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def sorted_barplot(rank_metric: np.ndarray, player_names: np.ndarray, err=None):
    """
    Function for making a sorted bar plot based on values in P, and labelling the plot with the
    corresponding names
    :param rank_metric: An array of length num_players with the metric to rank them by
    :param player_names: Array containing names of each player
    :param err: The error (for error bars) in the rank_metric array
    :return: the figure with the barplot
    """
    with sns.axes_style("darkgrid"):
        M = len(rank_metric)
        xx = np.linspace(0, M, M)
        fig = plt.figure(figsize=(20, 24))
        sorted_indices = np.argsort(rank_metric)
        sorted_names = player_names[sorted_indices]
        plt.barh(xx, rank_metric[sorted_indices], xerr=err,
                 ecolor='black', color=(1.0, 0.6, 0.75))
        plt.yticks(np.linspace(0, M, M), labels=sorted_names[:, 0])
        plt.ylim([-2, 109])
        plt.xlabel('Skill Mean')
        plt.show()
    return fig

