import os.path
import yaml

import flask
import jinja2

from bookr import cfg

TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), 'templates')

APP = flask.Flask(__name__)
jinja_loader = jinja2.ChoiceLoader([jinja2.FileSystemLoader(TEMPLATES_PATH)])
APP.jinja_loader = jinja_loader

@APP.route('/api/books')
def list():
    return flask.jsonify(cfg.CONF["books"])


@APP.route('/api/books/<txt_file>')
def book(txt_file):
    with open(cfg.datapath(txt_file), encoding='utf-8') as f:
        resp = flask.Response(f.read())
        resp.headers["Content-Type"] = "text/plain; charset=UTF-8"
        return resp


@APP.route('/word_analysis/<book_id>')
def word_analysis(book_id):
    books=cfg.CONF["books"]
    word_analysis_data={}
    for book in books:
        if(book["book_id"] == book_id):
            with open(cfg.datapath(book["word_analysis_file"])) as f:
                analyaml=yaml.safe_load(f)   
                word_analysis_data["lexical_diversity"] = round(analyaml["lexical_diversity"], 2)
                mf_string = ""
                for i in analyaml["most_frequent"]:
                    mf_string += (i + '; ')
                word_analysis_data["most_frequent"] = mf_string
                mr_string = ""
                for j in analyaml["most_rare"]:
                    mr_string += (j + '; ')
                word_analysis_data["most_rare"] = mr_string
                word_analysis_data["percentile_10"] = round(analyaml["percentile_10"])
                word_analysis_data["percentile_20"] = round(analyaml["percentile_20"])
                word_analysis_data["percentile_30"] = round(analyaml["percentile_30"])
                word_analysis_data["book_name"] = book["name"]
                word_analysis_data["book_author"] = book["author"]
    return flask.render_template('word_analysis.html', new_file_analysis=word_analysis_data)

@APP.route('/sentence_analysis/<book_id>')
def sentence_analysis(book_id):
    books=cfg.CONF["books"]
    sentence_analysis_data={}
    for book in books:
        if(book["book_id"] == book_id):
            with open(cfg.datapath(book["sentence_analysis_file"])) as f:
                analyaml_1=yaml.safe_load(f)   
                
                sentence_analysis_data["sentence_length_max"] = round(analyaml_1["sentence_length_max"])
                sentence_analysis_data["sentence_length_average"] = round(analyaml_1["sentence_length_average"])
                sentence_analysis_data["sentence_length_min"] = round(analyaml_1["sentence_length_min"])
                sentence_analysis_data["most_frequent_sentence_lengths"] = round(analyaml_1["most_frequent_sentence_lengths"])
                sentence_analysis_data["most_frequent_bigrams"] = round(analyaml_1["most_frequent_bigrams"])
                sentence_analysis_data["book_name"] = book["name"]
                sentence_analysis_data["book_author"] = book["author"]
    return flask.render_template('sentence_analysis.html', new_file_analysis_1=sentence_analysis_data)

@APP.route('/api/word_analysis/<word_analysis_file>')
def word_analysis_for_api(word_analysis_file):
    with open(cfg.datapath(word_analysis_file)) as f:
        return flask.render_template('word_analysis.html', wew=yaml.safe_load(f))

@APP.route('/api/sentence_analysis/<sentence_analysis_file>')
def sentence_analysis_for_api(sentence_analysis_file):
    with open(cfg.datapath(sentence_analysis_file)) as f:
        return flask.jsonify(yaml.safe_load(f))


@APP.route('/')
def index():
    return flask.render_template('index.html', books=cfg.CONF["books"])
