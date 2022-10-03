from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key="dojoninja"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/form', methods=['POST'])
def process_form():
    
    session["name"] = request.form["name"]
    session["city"] = request.form["city"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    
    return redirect('/result')
    

@app.route('/result')
def display():
    return render_template("form.html")




if __name__ == "__main__":
    app.run(debug=True)