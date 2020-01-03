from flask import Flask, render_template, request, redirect, send_file
from werkzeug import secure_filename
import svd
import imageio;


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/upload', methods=['GET, POST'])
def upload():
	
		
	return send_file(ret, attachment_filename=ret)

	#return render_template('downloads.html', val=ret)

@app.route('/downloads', methods=['POST'])
def downloads():

	f = request.files['file']
	f.save(secure_filename(f.filename))
	ret = svd.compres(f.filename);
	return render_template('downloads.html', val = ret)



if __name__ == "__main__":
    app.run()