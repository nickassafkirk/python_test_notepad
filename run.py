import os
import json
from flask import Flask, render_template
# we import the flask class from Flask dependency


app = Flask(__name__)
"""
We create an instance of the flask class and save it as a variable called app.
The first arguement of the Flask class, is the name of the application's
module, ie our package.
Since we're just using a single module, we can use __name__ which is
a built-in python variable. Flask needs this so it knows where to look
for templates and static files.
"""


@app.route("/")
def index():
    """
    the @ symbol denotes a python decorator. Decorators wrap functions and
    add additional functionality to functions.
    The decorator lets python know that when we browse the root root directory,
    that it should trigger the index function and retunr "Hello world"
    """
    return render_template("index.html")


@app.route("/about")
def about():
    with open("data/company.json", "r") as json_data:
        # open's json file read-only and saves as variable json_data
        data = json.load(json_data)
    return render_template(
        "about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def career():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":  # _main_ = the name of the default module in python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
"""
If name is equal to "main" (both wrapped in double underscores),
then we're going to run our app with the following arguments.
The 'host' will be set to os.environ.get("IP"),
and I will set a default of "0.0.0.0".
We're using the os module from the standard library to get the
'IP' environment variable if it exists, but set a default value if
it's not found.
You should only have debug=True while testing your application in
development mode, but change it to debug=False before you submit
your project.
"""
