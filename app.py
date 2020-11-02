from flask import Flask, render_template, request, url_for, redirect
from flask_restful import Api, Resource, reqparse
import datetime
import os


app= Flask(__name__)
api= Api(app)
app.config["MAX_CONTENT_LENGTH"] = 10485760000
app.config["UPLOAD_FOLDER"] = "./UploadedFiles"

arguments = reqparse.RequestParser() 
arguments.add_argument("name", type=str)

today = str(datetime.date.today())
today = today.split("-")
today.reverse()
dateToday = ""
for n, i in enumerate(today):
    if n < 2:
        dateToday+= i + "-"
    else:
        dateToday+=i


class Transify(Resource):
  def post(self):
    files= request.files.getlist("files")
    args = arguments.parse_args()
    
    userDirectory = os.path.join(app.config["UPLOAD_FOLDER"], args["name"].lower())
    fileUploadDirectory = os.path.join(app.config["UPLOAD_FOLDER"], args["name"].lower(), dateToday)

    if not os.path.isdir(userDirectory):
        os.mkdir(userDirectory)
        os.mkdir(fileUploadDirectory)
    elif not os.path.isdir(fileUploadDirectory):
        os.mkdir(fileUploadDirectory)

    for file in files:
      file.save(os.path.join(fileUploadDirectory, file.filename))

    return redirect("/")

@app.route("/")
def home():
  return render_template("index.html")

api.add_resource(Transify, "/upload")

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, threaded=True)
	