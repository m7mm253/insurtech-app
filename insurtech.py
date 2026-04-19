import streamlit as st
import base64
import re

# 1. إعداد الصفحة (تغيير الاسم كما طلبت)
st.set_page_config(page_title="InsurTech", page_icon="🛡️", layout="wide")

# 2. وظيفة تحميل الخلفية بأمان
def get_base64_img(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

bg_data = get_base64_img('background.png')

# 3. CSS احترافي (Lemonade Style + RTL)
style_css = f"""
<style>
    /* إخفاء الزوائد */
    header, footer, #MainMenu {{visibility: hidden;}}
    
    /* الخلفية والاتجاه */
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("data:image/png;base64,{bg_data}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white !important;
    }}

    /* النيف بار العلوي */
    .nav-bar {{
        background: rgba(10, 25, 41, 0.9);
        padding: 15px 60px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: fixed;
        top: 0; left: 0; width: 100%;
        z-index: 1000;
        border-bottom: 1px solid #00f2fe;
    }}

    /* كارت تسجيل الدخول */
    .login-box {{
        background: rgba(15, 32, 54, 0.95);
        border: 2px solid #00f2fe;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        direction: RTL;
    }}

    /* شاشة العرض الي في الشمال */
    .display-screen {{
        background: rgba(0,0,0,0.5);
        border: 1px solid rgba(0, 242, 254, 0.3);
        border-radius: 20px;
        height: 450px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
    }}

    /* تنسيق النصوص */
    h1, h2, h3, p, label {{ color: white !important; text-align: right; }}
    .stButton>button {{
        background-color: #00f2fe !important;
        color: #0a1929 !important;
        font-weight: bold !important;
        width: 100%;
        border-radius: 10px;
    }}
</style>
"""
st.markdown(style_css, unsafe_allow_html=True)

# --- 1. الـ Navbar (زي سكرين شوت ليمونيد) ---
st.markdown("""
    <div class="nav-bar">
        <div style="font-size: 24px; font-weight: bold; color: #00f2fe;">🛡️ InsurTech</div>
        <div style="display: flex; gap: 30px; color: white; direction: RTL;">
            <span>الرئيسية</span>
            <span>عن المنصة</span>
            <span>الدعم</span>
        </div>
        <button style="background: transparent; border: 1px solid #00f2fe; color: #00f2fe; padding: 5px 15px; border-radius: 5px;">Sign Up</button>
    </div>
""", unsafe_allow_html=True)

st.write("#") # سبيس تحت النيف بار

# --- 2. الجسم الرئيسي (Hero Section) ---
col_right, col_left = st.columns([1, 1.3], gap="large")

with col_right:
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 45px; margin-bottom: 10px;'>أمن مستقبل ك بلمسة</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; opacity: 0.8;'>أول نظام تأمين في مصر يعمل بالذكاء الاصطناعي بالكامل.</p>", unsafe_allow_html=True)
    
    # فورم الدخول مع التنبيهات
    with st.form("main_login"):
        user = st.text_input("اسم المستخدم")
        pwd = st.text_input("كلمة المرور", type="password")
        st.markdown("<p style='font-size: 12px; color: #00f2fe;'>نسيت كلمة المرور؟</p>", unsafe_allow_html=True)
        
        btn = st.form_submit_button("دخول للنظام")
        
        if btn:
            if not user or not pwd:
                st.error("❌ الخانات فاضية يا بطل")
            elif bool(re.search(r'[^a-zA-Z0-9\u0621-\u064A ]', user)):
                st.error("⚠️ ممنوع الرموز زي (@, #, $)")
            elif user == "admin" and pwd == "123":
                st.toast("نورت يا هندسة! 🚀")
            else:
                st.error("❌ البيانات غلط")
    st.markdown('</div>', unsafe_allow_html=True)

with col_left:
    st.markdown(f"""
        <div class="display-screen">
            <div>
                <h2 style="color: #00f2fe;">[ واجهة التحليل الذكي ]</h2>
                <p style="text-align: center;">اكتشف أفضل عروض التأمين المخصصة لك</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # الأزرار الي تحت الشاشة
    st.markdown("""
        <div style="display: flex; justify-content: center; gap: 40px; margin-top: 25px;">
            <span style="color: #00f2fe; border-bottom: 2px solid #00f2fe; padding-bottom: 5px; cursor: pointer;">تأمين السيارات</span>
            <span style="color: white; opacity: 0.6; cursor: pointer;">تأمين الممتلكات</span>
            <span style="color: white; opacity: 0.6; cursor: pointer;">تأمين السفر</span>
        </div>
    """, unsafe_allow_html=True)