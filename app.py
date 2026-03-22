# Main Application File for AI Job Finder Project
# ฟังก์ชันควบคุมหน้าแรก
from flask import Flask, render_template

app = Flask(__name__)

# --- 1. หน้าหลักและข้อมูลทั่วไป ---
@app.route('/')
def index(): return render_template('index.html')

@app.route('/about')
def about(): return render_template('about.html')

@app.route('/contact')
def contact(): return render_template('contact.html')

# --- 2. ระบบหางานและข่าวสาร ---
@app.route('/jobs')
def jobs(): return render_template('job.html')

@app.route('/news')
def news(): return render_template('news.html')

@app.route('/services')
def services(): return render_template('services.html')

# --- 3. ระบบสมาชิกและการรักษาความปลอดภัย ---
@app.route('/login')
def login(): return render_template('login.html')

@app.route('/register')
def register(): return render_template('register.html')

@app.route('/profile')
def profile(): return render_template('profile.html')

@app.route('/security')
def security(): return render_template('security.html')

# --- 4. แผงควบคุมและสถิติ AI ---
@app.route('/dashboard')
def dashboard(): return render_template('dashboard.html')

@app.route('/status')
def status(): return render_template('status.html')

@app.route('/recommendations')
def recommendations(): return render_template('recommendations.html')

# --- 5. คลังความรู้และผลงาน AI ---
@app.route('/portfolio')
def portfolio(): return render_template('portfolio.html')

@app.route('/dictionary')
def dictionary(): return render_template('dictionary.html')

@app.route('/faq')
def faq(): return render_template('faq.html')

# --- 6. ช่วยเหลือและนโยบาย ---
@app.route('/help')
def help_center(): return render_template('help.html')

@app.route('/terms')
def terms(): return render_template('terms.html')

@app.route('/privacy')
def privacy(): return render_template('privacy.html')

@app.route('/settings')
def settings(): return render_template('settings.html')

if __name__ == '__main__':
    # รันโปรเจกต์ในโหมด Debug เพื่อให้นักพัฒนาแก้ไขโค้ดได้ง่ายขึ้น
    app.run(debug=True)