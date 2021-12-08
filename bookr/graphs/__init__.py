from bookr.graphs import download
from bookr.graphs import word_analysis
from bookr.graphs import sentence_analysis
from bookr.graphs import total

GRAPH_FACTORY = {
    "download": download.create_taskgraph,
    "word_analysis": word_analysis.create_taskgraph,
    "sentence_analysis": sentence_analysis.create_taskgraph,
    "total": total.create_taskgraph,
}

