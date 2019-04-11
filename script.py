from flask import Flask, render_template

app = Flask(__name__)

@app.route('/landing.html')
def home():
    return render_template("landing.html")


@app.route('/temp_x.html')
def temps():
    return render_template("temp_x.html")

@app.route('/humid_x.html')
def humidity():
    return render_template("humid_x.html")

@app.route('/clouds_x.html')
def clouds():
    return render_template("clouds_x.html")

@app.route('/winds_x.html')
def winds():
    return render_template("winds_x.html")

@app.route('/comparisons.html')
def comparisons():
    return render_template("comparisons.html")

@app.route('/data.html')
def data_used():
    return render_template("data.html")

if __name__ == "__main__":
    app.run(debug=True)
