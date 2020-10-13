# Team Random: Ethan Machleder, Mary Shang, Jessica Yeung
# SoftDev
# K10: Putting Little Pieces Together
# 2020-10-13

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!" # print "No hablo queso!" on the webpage in plain text

app.run()
