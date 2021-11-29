import sys
import yaml
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
from bookr import cfg
from bookr.taskmanage.task import Task


def distance(word_analysis_1, word_analysis_2):
    len_intersection = len(set(word_analysis_1["most_frequent"]) & set(word_analysis_2["most_frequent"]))
    return 1 / (len_intersection + 1)


def build_dendrogram():
    distances = []
    for i in range(len(cfg.CONF["books"]) - 1):
        with open(cfg.datapath(cfg.CONF["books"][i]["word_analysis_file"])) as f:
            word_analysis_1 = yaml.safe_load(f)
        for j in range(i + 1, len(cfg.CONF["books"])):
            with open(cfg.datapath(cfg.CONF["books"][j]["word_analysis_file"])) as f:
                word_analysis_2 = yaml.safe_load(f)

            d = distance(word_analysis_1, word_analysis_2)
            distances.append(d)

    Z = sch.linkage(distances, 'single')
    plt.figure()
    labels=[b["name"] for b in cfg.CONF["books"]]
    sch.dendrogram(Z, labels=labels, leaf_rotation=90.0, leaf_font_size=8)
    plt.savefig(cfg.datapath(cfg.CONF["dendrogram_file"]))


def create_task():
    task = Task("build_dendrogram")
    task.set_action(build_dendrogram)
    return task