import os, datetime

today = str(datetime.date.today())
today = today.split("-")
today.reverse()
dateToday = ""
for n, i in enumerate(today):
    if n < 2:
        dateToday+= i + "-"
    else:
        dateToday+=i

config={}
args={
    "name": "Arik"
}
config["UPLOAD_FOLDER"] = "./UploadedFiles"

userDirectory = os.path.join(config["UPLOAD_FOLDER"], args["name"])
fileUploadDirectory = os.path.join(config["UPLOAD_FOLDER"], args["name"], dateToday)

print(os.path.isdir(fileUploadDirectory))

if not os.path.isdir(userDirectory):
    os.mkdir(userDirectory)
    os.mkdir(fileUploadDirectory)
elif not os.path.isdir(fileUploadDirectory):
    os.mkdir(fileUploadDirectory)



