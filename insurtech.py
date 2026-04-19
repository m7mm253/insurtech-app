import streamlit as st
import pandas as pd
import base64

# --- إعدادات الصفحة ---
st.set_page_config(page_title="SecureNow Egypt", page_icon="🛡️", layout="wide")

# --- دالة لتحميل الصورة وتحويلها ---
def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

# --- دالة وضع الخلفية ---
def set_bg():
    bin_str = get_base64('background.png')
    if bin_str:
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .main {{ background: rgba(0,0,0,0); }}
        .stForm {{
            background-color: rgba(0, 20, 40, 0.8);
            border-radius: 10px;
            padding: 20px;
            border: 1px solid #00f2fe;
        }}
        h1, h2, h3, p, label {{ color: white !important; }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    else:
        st.sidebar.warning("⚠️ يرجى رفع ملف background.png")

set_bg()

# --- إدارة الحالة (Session State) ---
if 'users_db' not in st.session_state:
    st.session_state.users_db = {'admin': '123'} 
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- واجهة الدخول ---
if not st.session_state.logged_in:
    # اختيار اللغة من القائمة الجانبية
    lang = st.sidebar.radio("Language / اللغة", ["العربية", "English"])
    
    st.sidebar.markdown("---")
    
    # هنا التصحيح: استخدمنا unsafe_allow_html بدلاً من unsafe_allow_safe
    st.sidebar.markdown(f"<h3 style='text-align: center; color: white;'>{'تسجيل الدخول' if lang == 'العربية' else 'Login'}</h3>", unsafe_allow_html=True)
    
    with st.sidebar.form("login"):
        u = st.text_input("Username / اسم المستخدم")
        p = st.text_input("Password / كلمة المرور", type="password")
        if st.form_submit_button("Enter / دخول"):
            if u in st.session_state.users_db and st.session_state.users_db[u] == p:
                st.session_state.logged_in = True
                st.session_state.current_user = u
                st.rerun()
            else:
                st.error("خطأ / Invalid Credentials")

# --- واجهة التطبيق (بعد الدخول) ---
else:
    st.title(f"Welcome, {st.session_state.current_user} 👋")
    if st.sidebar.button("Logout / خروج"):
        st.session_state.logged_in = False
        st.rerun()
    st.info("أهلاً بك في نظام التأمين المتطور.")