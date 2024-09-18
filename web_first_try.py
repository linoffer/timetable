from flask import Flask, redirect, url_for, render_template, request
import json

list1 = []
app = Flask(__name__)


@app.route("/")
def welcome_page():
    return render_template("file1.html")

@app.route("/file2", methods=['POST'])
def second_page():
    html_data = request.form["enter_value"]
    list1.append(html_data)
    return render_template("file2.html", html_data=html_data)







if __name__ == "__main__":
    app.run(debug=True)

print(list1)