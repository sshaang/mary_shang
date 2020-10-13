# Team Random: Ethan Machleder, Mary Shang, Jessica Yeung
# SoftDev
# K10: Putting Little Pieces Together
# 2020-10-13

from flask import Flask
app = Flask(__name__) # create instance of class Flask

@app.route("/")       # assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   # where will this go? -- to the terminal
    return "No hablo queso!" # print "No hablo queso!" on the webpage in plain text

app.debug = True # display bugs on the webpage (if there's any)
app.run()
