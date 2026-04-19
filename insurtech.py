import streamlit as st
import base64

# 1. إعداد الصفحة (Wide Layout) وإخفاء زوائد Streamlit
st.set_page_config(page_title="SecureNow Egypt", page_icon="🛡️", layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* ضبط خلفية الصفحة بالكامل (الديكور بتاعك) */
            .stApp {
                background-image: url("data:image/png;base64,{base64_bg}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }
            
            /* تخصيص الـ Header (شريط التنقل العلوي) */
            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 15px 50px;
                background-color: rgba(10, 25, 41, 0.7); /* أزرق داكن شفاف */
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                z-index: 999;
                color: white;
            }
            .navbar-logo {
                font-size: 24px;
                font-weight: bold;
                display: flex;
                align-items: center;
            }
            .navbar-links {
                display: flex;
                gap: 25px;
            }
            
            /* تصميم القسم الرئيسي (البطل - Hero Section) */
            .hero-section {
                display: flex;
                flex-direction: row-reverse; /* يجعل العربي يمين والإنجليزي شمال */
                justify-content: space-between;
                align-items: center;
                margin-top: 120px; /* مسافة لأسفل Navbar */
                padding: 50px;
                gap: 50px;
            }
            
            /* تصميم خانات الدخول (اليمين في العربي - زي "The first AI...") */
            .login-container {
                flex: 1;
                direction: RTL; /* العربي يمين */
                text-align: right;
            }
            .stForm {
                background-color: rgba(10, 25, 41, 0.9) !important;
                border: 2px solid #00f2fe !important;
                border-radius: 20px !important;
                padding: 30px !important;
                box-shadow: 0 0 25px rgba(0, 242, 254, 0.4);
            }
            
            /* تصميم قسم العرض (الشمال - زي شاشة Roblox) */
            .display-container {
                flex: 1.2;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
            .display-box {
                background-color: rgba(10, 25, 41, 0.8);
                border-radius: 20px;
                width: 100%;
                height: 350px;
                border: 1px solid rgba(255, 255, 255, 0.2);
                box-shadow: 0 0 15px rgba(255, 255, 255, 0.1);
                display: flex;
                align-items: center;
                justify-content: center;
                color: rgba(255, 255, 255, 0.6);
            }
            
            /* تصميم أزرار العرض (الأسفل - زي "Shop with UI...") */
            .demo-buttons {
                margin-top: 20px;
                display: flex;
                gap: 20px;
                justify-content: center;
            }
            .demo-btn {
                background: none;
                border: none;
                color: white;
                font-size: 16px;
                opacity: 0.6;
                transition: 0.3s;
                cursor: pointer;
            }
            .demo-btn:hover, .demo-btn-active {
                opacity: 1;
                border-bottom: 2px solid white;
            }

            /* ألوان وتعديلات الخطوط */
            h1, h2, h3, p, label { color: white !important; font-family: 'Tahoma', sans-serif;}
            </style>
            """

# 2. وظيفة تحميل الخلفية (الديكور بتاعك)
def get_base64_img(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return ""

base64_bg = get_base64_img('background.png')

# 3. تطبيق الـ CSS
st.markdown(hide_st_style.format(base64_bg=base64_bg), unsafe_allow_html=True)

# 4. بناء الـ UI (مستوحى من Lemonade)

# --- 1. Navbar ---
st.markdown(f"""
    <div class="navbar">
        <div class="navbar-logo">🍋 SecureNow</div>
        <div class="navbar-links">
            <a>ابدأ التأمين</a>
            <a>الأسئلة الشائعة</a>
            <a>تواصل معنا</a>
        </div>
        <div>
            <button style='background-color: white; color: black; border-radius: 5px; padding: 8px 15px; border: none; font-weight: bold;'>شراء بوليصة</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 2. Hero Section ---
st.markdown("<div class='hero-section'>", unsafe_allow_html=True)

# (اليمين للعربي - تسجيل الدخول)
with st.container():
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.markdown("<h1>أول تطبيق تأمين<br>بذكاء اصطناعي في مصر</h1>", unsafe_allow_html=True)
    st.markdown("<p style='opacity: 0.7; margin-bottom: 30px;'>انضم لآلاف المؤمن عليهم الذين يستخدمون SecureNow للحصول على عروض تأمين فورية ودقيقة في ثوانٍ معدودة.</p>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        st.markdown("<h3>تسجيل الدخول</h3>", unsafe_allow_html=True)
        u = st.text_input("اسم المستخدم")
        p = st.text_input("كلمة المرور", type="password")
        submit = st.form_submit_button("دخول للنظام")
    
    st.markdown("</div>", unsafe_allow_html=True)

# (الشمال - قسم العرض)
with st.container():
    st.markdown("<div class='display-container'>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="display-box">
            <span>هنا سيظهر عرض سريع للباقة التأمينية المختارة<br>أو رسم بياني تحليلي</span>
        </div>
    """, unsafe_allow_html=True)
    
    # أزرار العرض (الأسفل)
    st.markdown(f"""
        <div class="demo-buttons">
            <button class="demo-btn demo-btn-active">اختيار باقة</button>
            <button class="demo-btn">نظام التسعير</button>
            <button class="demo-btn">المطالبات</button>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True) # نهاية Hero Section