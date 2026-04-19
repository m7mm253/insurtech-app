import streamlit as st
import base64

# 1. إعدادات الصفحة وإخفاء شريط Streamlit (App Mode)
st.set_page_config(page_title="SecureNow Egypt", page_icon="🛡️", layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            /* دعم اللغة العربية واتجاه النص RTL */
            body, .main, .stApp {
                direction: RTL;
                text-align: right;
            }
            /* تصحيح اتجاه العناصر داخل الفورم */
            .stTextInput, .stButton, .stCheckbox {
                direction: RTL;
                text-align: right;
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- دالة وضع الخلفية ---
def set_bg():
    try:
        with open("background.png", "rb") as f:
            bin_str = base64.b64encode(f.read()).decode()
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-position: center;
        }}
        .stForm {{
            background-color: rgba(0, 20, 40, 0.8);
            border-radius: 15px;
            padding: 25px;
            border: 1px solid #00f2fe;
            box-shadow: 0 0 15px rgba(0, 242, 254, 0.3);
        }}
        h3, p, label {{ color: white !important; font-family: 'Tahoma', sans-serif; }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except:
        st.sidebar.warning("⚠️ يرجى رفع background.png")

set_bg()

# --- المنطق (Logic) ---
if 'users_db' not in st.session_state:
    st.session_state.users_db = {'admin': '123'} 
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- واجهة الدخول ---
if not st.session_state.logged_in:
    # القائمة الجانبية (تسجيل الدخول)
    with st.sidebar:
        st.markdown("<h2 style='text-align: center;'>SecureNow</h2>", unsafe_allow_html=True)
        st.markdown("---")
        
        with st.form("login_form"):
            st.markdown("<h3>تسجيل الدخول</h3>", unsafe_allow_html=True)
            u = st.text_input("اسم المستخدم")
            p = st.text_input("كلمة المرور", type="password")
            
            # خيار تذكرني
            remember = st.checkbox("تذكرني على هذا الجهاز")
            
            submit = st.form_submit_button("دخول")
            
            if submit:
                if u in st.session_state.users_db and st.session_state.users_db[u] == p:
                    st.session_state.logged_in = True
                    st.session_state.current_user = u
                    st.toast("تم تسجيل الدخول بنجاح! 🎉") # تنبيه شيك بيظهر ويختفي
                    st.rerun()
                else:
                    st.error("❌ عذراً، اسم المستخدم أو الباسورد خطأ")

        # خيار نسيت كلمة المرور (UX)
        if st.button("نسيت كلمة المرور؟"):
            st.info("يرجى التواصل مع الدعم الفني لإعادة تعيين كلمة المرور: support@securenow.com")

# --- واجهة التطبيق بعد الدخول ---
else:
    st.title(f"مرحباً بك، {st.session_state.current_user}")
    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.logged_in = False
        st.rerun()
    st.success("أنت الآن تستخدم النسخة الاحترافية من التطبيق.")