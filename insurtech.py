import streamlit as st
import base64
import re

# 1. إعدادات الصفحة
st.set_page_config(page_title="SecureNow Egypt", page_icon="🛡️", layout="wide")

# 2. وظيفة تحميل الخلفية (الديكور)
def get_base64_img(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return ""

base64_bg = get_base64_img('background.png')

# 3. كود الـ CSS (الديزاين الجديد المستوحى من Lemonade)
# استخدمنا {{ }} بدلاً من { } عشان نتفادى الـ KeyError
style_css = f"""
<style>
    header, footer, #MainMenu {{visibility: hidden;}}
    
    .stApp {{
        background-image: url("data:image/png;base64,{base64_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* الـ Navbar العلوي */
    .navbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 60px;
        background-color: rgba(10, 25, 41, 0.8);
        position: fixed;
        top: 0; left: 0; width: 100%;
        z-index: 999;
    }}
    
    /* تقسيم الصفحة نصين (Hero Section) */
    .main-container {{
        display: flex;
        flex-direction: row-reverse;
        justify-content: space-around;
        align-items: center;
        padding: 100px 50px 20px 50px;
        gap: 30px;
    }}

    .login-card {{
        background-color: rgba(10, 25, 41, 0.9);
        border: 2px solid #00f2fe;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 0 30px rgba(0, 242, 254, 0.3);
        max-width: 450px;
    }}

    .display-preview {{
        background-color: rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        width: 100%;
        height: 400px;
        display: flex;
        align-items: center;
        justify-content: center;
    }}

    h1, h2, h3, p, label {{ color: white !important; direction: RTL; text-align: right; }}
</style>
"""
st.markdown(style_css, unsafe_allow_html=True)

# 4. بناء الهيكل (UI Structure)

# --- Navbar ---
st.markdown("""
    <div class="navbar">
        <div style="color: white; font-size: 24px; font-weight: bold;">🛡️ SecureNow</div>
        <div style="display: flex; gap: 20px; color: white; direction: RTL;">
            <span>الرئيسية</span>
            <span>الخدمات</span>
            <span>الأسعار</span>
        </div>
        <button style="background-color: #00f2fe; border: none; padding: 8px 20px; border-radius: 5px; font-weight: bold;">ابدأ الآن</button>
    </div>
""", unsafe_allow_html=True)

# --- Hero Section ---
col_right, col_left = st.columns([1, 1.2])

with col_right:
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 40px;'>مستقبل التأمين<br>بين يديك</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; opacity: 0.8;'>أول منصة مصرية تعتمد على الذكاء الاصطناعي لتوفير حماية ذكية وسهلة.</p>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        u = st.text_input("اسم المستخدم", placeholder="User123")
        p = st.text_input("كلمة المرور", type="password")
        
        # التنبيهات الذكية
        submit = st.form_submit_button("دخول للنظام")
        if submit:
            if not u or not p:
                st.error("❌ الخانات فارغة")
            elif bool(re.search(r'[^a-zA-Z0-9 ]', u)):
                st.error("⚠️ لا تستخدم رموز مثل (@, #, $)")
            elif u == "admin" and p == "123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("❌ البيانات غلط")
    st.markdown('</div>', unsafe_allow_html=True)

with col_left:
    st.markdown('<div class="display-preview">', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #00f2fe;'>[ شاشة عرض البيانات الذكية ]</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # أزرار الديمو تحت الشاشة (زي Lemonade)
    st.markdown("""
        <div style="display: flex; justify-content: center; gap: 30px; margin-top: 20px;">