from flask import Flask, render_template

app = Flask(__name__)

# --- รวมทุก Route ไว้ที่นี่ที่เดียว ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jobs')
def jobs():
    return render_template('job.html') # เช็คชื่อไฟล์ให้ตรงกับ templates นะครับ

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/security')
def security():
    return render_template('security.html')

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/recommendations')
def recommendations():
    return render_template('recommendations.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# --- จบส่วน Route ---

if __name__ == '__main__':
    app.run(debug=True)