
from flask import Flask, render_template
 
app = Flask(__name__)

@app.route('/')  
def message():
    return render_template("home.html")
  
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=False,port=5055,threaded=True)