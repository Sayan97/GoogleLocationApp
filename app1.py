from flask import Flask
from string import Template
app = Flask(__name__)

html_template= Template("""
    <h1>Hello ${place_name}!</h1>
    <img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=${place_name}" alt="map of ${place_name}">
    <br>
    <img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=${place_name}" alt="street-view of ${place_name}">
    """)

@app.route("/")
def homepage():
    return "<h1>Hello World!</h1>"

@app.route("/weather/<n>")
def weather(n):
    s = "The weather function is not working for {name}"
    return s.format(name=n)

@app.route("/place/<some_place>")
def place_name_page(some_place):
    return html_template.substitute(place_name=some_place)

if __name__=="__main__":
    app.run(debug=True)
