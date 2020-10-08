from flask import Flask
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q3: Will this appear anywhere? How u know?

# Added the following to change the server from a development one to a production one
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    
app.run()  # Q4: Where have you seen similar constructs in other languages?
