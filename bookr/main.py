import click
from bookr import cfg, api

from bookr.graphs import GRAPH_FACTORY


@click.group()
def cli():
    pass


@cli.command()
@click.option('--host', default="0.0.0.0",
              help="server host", envvar="HOST")
@click.option('--port', default=5000, type=int,
              help="server port", envvar='PORT')
@click.option('--config', help="config file", required=True)
def serve(config, host, port):
    cfg.init(config)
    api.APP.run(host=host, port=port)


@cli.command()
@click.option('--config', help="config file", required=True)
@click.option('--graph', help="graph name", required=True)
def run_task_graph(config, graph):
    cfg.init(config)
    graph = GRAPH_FACTORY[graph]()
    graph.run()
