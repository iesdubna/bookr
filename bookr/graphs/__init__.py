
from bookr.graphs import download
from bookr.graphs import word_analysis


GRAPH_FACTORY = {
    "download": download.create_taskgraph,
    "word_analysis": word_analysis.create_taskgraph,
}

