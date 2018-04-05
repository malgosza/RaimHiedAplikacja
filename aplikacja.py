from flask import Flask
from flask import render_template

aplikacja=Flask(__name__)

@aplikacja.route("/")
def stronaStartowa():
    return render_template('ankietaStrona1.html')


if __name__ == '__main__':
    aplikacja.run(debug=True)