import os.path
import yaml

import flask

from bookr import cfg


APP = flask.Flask(__name__)


@APP.route('/api/books')
def list():
    return flask.jsonify(cfg.CONF["books"])


@APP.route('/api/books/<txt_file>')
def book(txt_file):
    with open(cfg.datapath(txt_file), encoding='utf-8') as f:
        resp = flask.Response(f.read())
        resp.headers["Content-Type"] = "text/plain; charset=UTF-8"
        return resp


@APP.route('/api/word_analysis/<word_analysis_file>')
def word_analysis(word_analysis_file):
    with open(cfg.datapath(word_analysis_file)) as f:
        return flask.jsonify(yaml.safe_load(f))


@APP.route('/api/sentence_analysis/<sentence_analysis_file>')
def sentence_analysis(sentence_analysis_file):
    with open(cfg.datapath(sentence_analysis_file)) as f:
        return flask.jsonify(yaml.safe_load(f))