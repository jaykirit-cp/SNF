#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request,redirect
from flask import send_file, send_from_directory, safe_join, abort
from flask.helpers import url_for

from generate_report import *
import os
print(os.getcwd())

from sklearn.model_selection import train_test_split



#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')

#db = SQLAlchemy(app)



# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/',methods=['GET','POST'])
def home():
    return render_template('pages/SNF.html')


@app.route('/download', methods=['GET', 'POST'])
def download():
    global user_details
    if(request.method == 'POST'):
        print("Test")
        user_details= {
            "Name":request.form.get("name"),
            "Gender":request.form.get("gender"),
            "Age":request.form.get("age"),
            "Pregnancies":request.form.get("pregnancies"),
            "Glucose":request.form.get("glucose"),
            "Bloodpressure":request.form.get("bloodpressure"),
            "Skinthickness":request.form.get("skinthickness"),
            "Insulin":request.form.get("insulin"),
            "BMI":request.form.get('bmi'),
            "Diabetes Pedigree Function":request.form.get('dpf'),
            "Email Address":request.form.get('email')

            #"Gender":request.form.get("gender"),
            #"Diagnosis":request.form.get("Diagnosis"),
            #"Analysis":request.form.get("disease"),
            #"Image":""
            
        }
        print(user_details)
        report = Report()
        report.generate_report(user_details) #Added change here

        return redirect('/')
    return redirect('/')

    #return send_from_directory(directory="./reports", filename="report.pdf")

#IMAGE INPUT

#@app.route("/analyze_img",methods=['POST','GET'])
#def analyze_img():

    #if(request.method  == 'POST'):    
        #if(request.files):
            #report.refresh()
            #img = request.files['image']
            #img.save(os.path.join("./static/images",img.filename))
            #user_details['Image'] = img.filename
            #print(user_details)
            #report.generate_report(user_details)
            #test_img = cv2.imread(os.path.join(app.config['IMAGE_UPLOADS'], img.filename))

    #return redirect('user')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


# @app.route('/login')
# def login():
#     form = LoginForm(request.form)
#     return render_template('forms/login.html', form=form)


# @app.route('/register')
# def register():
#     form = RegisterForm(request.form)
#     return render_template('forms/register.html', form=form)


# @app.route('/forgot')
# def forgot():
#     form = ForgotForm(request.form)
#     return render_template('forms/forgot.html', form=form)


# Error handlers.

# @app.errorhandler(500)
# def internal_error(error):
#     #db_session.rollback()
#     return render_template('errors/500.html'), 500


# @app.errorhandler(404)
# def not_found_error(error):
#     return render_template('errors/404.html'), 404

# if not app.debug:
#     file_handler = FileHandler('error.log')
#     file_handler.setFormatter(
#         Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
#     )
#     app.logger.setLevel(logging.INFO)
#     file_handler.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)
#     app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port -  PORT:3000:
if __name__ == '__main__':
    app.run()
    