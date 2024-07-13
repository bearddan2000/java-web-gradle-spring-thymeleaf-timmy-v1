from flask import Flask, render_template, request
import json, logging, datetime

from entity.page import Project
from entity.helper.week import Week
from entity.helper.legend import Legend

logging.basicConfig(level=logging.INFO)

app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates"
)
def read_data():
    infile = 'data.json'
    with open(infile) as f:
        return json.load(f)

def build_html(report_id):
    d = read_data()
    return Project(report_id, d)

def build_index_day_number_html():
    x = datetime.datetime.now()
    index = int(x.strftime("%w"))
    return index-1

@app.route('/', methods=['GET'])
def getIndex():
    w = Week(read_data())
    return render_template("index.html", week=w)

@app.route('/current', methods=['GET'])
def getCurrent():
    w = Week(read_data())
    project = build_html(0)
    project.create_stats()
    index = build_index_day_number_html()
    current = project.reports[index]

    logging.info(current)

    return render_template("current.html", 
        item=current, week=w)

@app.route('/historical', methods=['GET'])
def getPreview():
    w = Week(read_data())
    project = build_html(0)
    return render_template("historical.html", reports=project.reports, week=w)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)