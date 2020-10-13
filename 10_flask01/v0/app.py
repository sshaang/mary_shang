# Team Random: Ethan Machleder, Mary Shang, Jessica Yeung
# SoftDev
# K10: Putting Little Pieces Together
# 2020-10-13

from flask import Flask
app = Flask(__name__

@app.route("/") # refers to the root route
def hello_world():
    print(__name__) # prints __main__ to the terminal
    return "No hablo queso!"  # prints "No hablo queso!" on the webpage in plain text

app.run() # similar to the dot operator in Java; starts up the web server
