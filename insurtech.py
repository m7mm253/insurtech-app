import streamlit as st
import base64
import re

# 1. إعداد الصفحة
st.set_page_config(page_title="InsurTech", page_icon="🛡️", layout="wide")

# 2. تحميل الخلفية (تأكد من وجود ملف background.png في مشروعك)
def get_base64_img(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

bg_data = get_base64_img('background.png')

# 3. الـ CSS لفرض الصورة كخلفية (بدون رمادي)
style_css = f"""
<style>
    header, footer, #MainMenu {{visibility: hidden;}}
    
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url("data:image/png;base64,{bg_data}");
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}
    
    .stVerticalBlock, .stColumn {{ background-color: transparent !important; }}

    .auth-card {{
        background: rgba(10, 25, 41, 0.9);
        border: 2px solid #00f2fe;
        border-radius: 20px;
        padding: 40px;
        max-width: 500px;
        margin: auto;
        box-shadow: 0 0 30px rgba(0, 242, 254, 0.3);
    }}

    h1, h2, h3, p, label {{ color: white !important; font-family: 'Tahoma', sans-serif; }}
    
    /* تنسيق الزراير */
    .stButton>button {{
        background-color: #00f2fe !important;
        color: #0a1929 !important;
        font-weight: bold !important;
        width: 100% !important;
        border-radius: 10px !important;
        height: 45px;
        border: none !important;
    }}
    
    .secondary-btn>button {{
        background-color: transparent !important;
        color: #00f2fe !important;
        border: 1px solid #00f2fe !important;
    }}
</style>
"""
st.markdown(style_css, unsafe_allow_html=True)

# 4. قاموس اللغات
texts = {
    "العربية": {
        "title": "🛡️ InsurTech",
        "subtitle": "سجل دخولك للوصول لنظام التأمين الذكي",
        "user": "اسم المستخدم",
        "pass": "كلمة المرور",
        "login": "تسجيل الدخول",
        "register": "إنشاء حساب جديد",
        "remember": "تذكرني",
        "forgot": "نسيت كلمة المرور؟",
        "err_empty": "❌ الخانات فارغة!",
        "err_symbols": "⚠️ لا تستخدم رموز مثل (@, #, $)",
        "err_wrong": "❌ البيانات غلط"
    },
    "English": {
        "title": "🛡️ InsurTech",
        "subtitle": "Login to access the smart insurance system",
        "user": "Username",
        "pass": "Password",
        "login": "Login",
        "register": "Create New Account",
        "remember": "Remember me",
        "forgot": "Forgot Password?",
        "err_empty": "❌ Fields are empty!",
        "err_symbols": "⚠️ No special characters allowed",
        "err_wrong": "❌ Invalid credentials"
    }
}

# 5. اختيار اللغة وتحويل الاتجاه
lang = st.sidebar.selectbox("🌐 Language / اللغة", ["العربية", "English"])
t = texts[lang]
direction = "RTL" if lang == "العربية" else "LTR"

# تطبيق الاتجاه
st.markdown(f'<div style="direction: {direction};">', unsafe_allow_html=True)

# 6. واجهة المستخدم
st.write("##") 
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="auth-card">', unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center;'>{t['title']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; opacity: 0.8;'>{t['subtitle']}</p>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        u = st.text_input(t["user"], placeholder="User123")
        p = st.text_input(t["pass"], type="password")
        st.checkbox(t["remember"])
        
        submit = st.form_submit_button(t["login"])
        
        if submit:
            if not u or not p:
                st.error(t["err_empty"])
            elif bool(re.search(r'[^a-zA-Z0-9\u0621-\u064A ]', u)):
                st.error(t["err_symbols"])
            elif u == "admin" and p == "123":
                st.success("Success!")
            else:
                st.error(t["err_wrong"])
    
    # أزرار إضافية (تسجيل جديد ونسيت الباسورد)
    st.write("---")
    
    # زر تسجيل جديد
    if st.button(t["register"]):
        st.info("سيتم تحويلك لصفحة التسجيل...")
        
    # زر نسيت كلمة المرور
    st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
    if st.button(t["forgot"]):
        st.warning("يرجى التواصل مع الدعم: support@insurtech.com")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)