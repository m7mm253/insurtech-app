import streamlit as st
import pandas as pd
import base64

# --- إعدادات الصفحة ---
st.set_page_config(page_title="SecureNow Egypt", page_icon="🛡️", layout="wide")

# --- دالة لتحميل الصورة وتحويلها عشان CSS ---
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- دالة وضع الخلفية بتصميم الصورة بتاعتك ---
def set_bg():
    try:
        # هنا بنحمل ملف الصورة اللي سميناه background.png
        bin_str = get_base64('background.png')
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        /* جعل محتوى الصفحة شفافاً فوق الخلفية */
        .main {{
            background: rgba(0,0,0,0);
        }}
        
        /* تخصيص مظهر خانات الدخول عشان تمشي مع ستايل التكنولوجيا */
        .stForm {{
            background-color: rgba(0, 48, 73, 0.85); /* لون أزرق غامق شفاف */
            border-radius: 15px;
            padding: 30px;
            border: 2px solid #00f2fe; /* حدود مضيئة */
            box-shadow: 0 0 20px rgba(0, 242, 254, 0.5);
        }}
        
        h1, h2, h3, .stText, p {{
            color: #ffffff !important; /* لون الخط أبيض */
            font-family: 'Segoe UI', sans-serif;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_safe=True)
    except FileNotFoundError:
        st.warning("⚠️ لم نجد ملف background.png. تأكد من وضعه في نفس الفولدر.")

# --- تطبيق الخلفية ---
set_bg()

# --- إدارة الحالة (Session State) ---
if 'users_db' not in st.session_state:
    st.session_state.users_db = {'admin': '123'} 
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None

# --- واجهة الدخول (ستظهر فوق الخلفية المضيئة) ---
if not st.session_state.logged_in:
    # بنعمل مسافة كبيرة فوق عشان عناصر الدخول تنزل تحت العنوان الكبير اللي في الصورة
    st.write("#") 
    st.write("#")
    
    # اختيار اللغة
    lang = st.sidebar.radio("🌐 Choose Language / اختر اللغة", ["العربية", "English"])
    
    st.sidebar.markdown("---")
    
    # قسم الدخول في القائمة الجانبية أو في المنتصف
    # عشان عناصر الـ form متداريش العنوان الكبير في الصورة، هنحطها في sidebar
    st.sidebar.markdown(f"<h3 style='text-align: center; color: white;'>{'تسجيل الدخول' if lang == 'العربية' else 'Login'}</h3>", unsafe_allow_safe=True)
    
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
                
    st.sidebar.markdown(f"<p style='text-align: center; color: white;'>{'ليس لديك حساب؟ قم بإنشاء واحد.' if lang == 'العربية' else 'No account? Create one.'}</p>", unsafe_allow_safe=True)

# --- واجهة التطبيق الرئيسية (بعد الدخول) ---
else:
    st.sidebar.title(f"Welcome, {st.session_state.current_user} 👋")
    # ... باقي كود التطبيق بتاعك (الشراء، التأميناتي) ...
    st.header("🛡️ لوحة التحكم - SecureNow")
    st.write("ابدأ تجربتك التقنية في عالم التأمين.")