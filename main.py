from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classes')
def classes():
    return render_template('classes.html')

@app.route('/shows')
def shows():
    return render_template('shows.html')

@app.route('/work-with-us')
def work_with_us():
    return render_template('work_with_us.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['POST'])
def contact():
    service_type = request.form.get('service_type')
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # In production, this would send an email or store in database
    flash(f'Thank you {name}! We have received your {service_type} inquiry and will contact you at {email} soon.', 'success')
    return redirect(url_for('work_with_us'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
