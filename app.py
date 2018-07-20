from flask import Flask ,render_template
import random
app = Flask(__name__)


@app.route('/')
def website():
	return render_template('perfect.html')


if __name__== "__main__":
	app.run(port=8000,debug=True)

