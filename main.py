from flask import Flask, redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import subprocess
import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

def run_script2(args):
    script2_path = "flaskdetect.py"
    subprocess.call([sys.executable, script2_path] + args.split())



class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        args = "--weights best.pt --conf 0.5 --img-size 640 --source "+app.config['UPLOAD_FOLDER']+'/'+secure_filename(file.filename)+" --view-img --no-trace"
        run_script2(args)
        return redirect('/display/'+filename)
    return render_template('index.html', form=form)

@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='files/' + filename), code=301)

if __name__ == '__main__':
    app.run(debug=True)