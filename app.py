#import necessary libraries from flask import Flask, render_template, redirect
from flask import Flask, render_template, redirect
from flask_restful import Resource, Api, reqparse
import os
# from flask_pymongo import PyMongo
# import scrape_transit

# # import otherroute! which is another py file
# try:
#     # The typical way to import flask-cors
#     from flask_cors import CORS
# except ImportError:
#     # Path hack allows examples to be run without installation.
#     import os
#     parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     os.sys.path.insert(0, parentdir)

#     from flask_cors import CORS

#create Flask app instance
app = Flask(__name__)
api = Api(app)
# cors=CORS(app, resources=r'smallSst.json', allow_headers='Content-Type')

# setup conn to PyMongo
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/transitDB'
# mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/naturalLanguage")
def naturalLanguage():
    return render_template("naturalLanguage.html")

@app.route("/timeSeriesFunding")
def timeSeriesFunding():
    return render_template("timeSeriesFunding.html")

@app.route("/fundingBySource")
def fundingBySource():
    return render_template("fundingBySource.html")

@app.route("/transitAccesibility")
def transitAccesibility():
    return render_template("transitAccesibility.html")

@app.route("/resources")
def resources():
    # transitArticles=mongo.db.transitArticles.find_one()
    return render_template("resources.html")

@app.route("/methods")
def methods():
    return render_template("methods.html")

@app.route("/dataSources")
def dataSources():
    return render_template("dataSources.html")

# setup conn to PyMongo
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/marsDB'
# mongo = PyMongo(app)
 
# create route that scrapes mars data and store as dictionary and to MongoDB
# @app.route('/scrape')
# def scrape():
#     transitArticles=mongo.db.transitArticles
#     transit_data = scrape_transit.scrape_all()
#     transitArticles.replace_one({},transit_data, upsert=True)
#     return redirect('/resources')

if __name__ == '__main__':
    app.run(debug=True, port = 1123)