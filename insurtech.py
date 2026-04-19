import streamlit as st
import base64
import re

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="SecureNow Egypt", page_icon="🛡️", layout="wide")

# 2. كود الـ CSS (الاتجاه من اليمين للشمال + إخفاء الزوائد)
style_css = """
<style>
    /* إخفاء الهيدر والفوتر */
    header, footer, #MainMenu {visibility: hidden;}
    
    /* ضبط الاتجاه للعربية */
    .stApp {
        direction: RTL;
        text-align: right;
    }
    
    /* تحسين شكل الفورم */
    .stForm {
        background-color: rgba(0, 20, 40, 0.85);
        border: 1px solid #00f2fe;
        border-radius: 15px;
        padding: 20px;
    }
    
    /* توحيد لون الخط */
    h1, h2, h3, p, label, .stMarkdown {
        color: white !important;
    }
    
    /* جعل التنبيهات تظهر فوق كل شيء */
    .stAlert {
        direction: RTL;
        text-align: right;
    }
</style>
"""
st.markdown(style_css, unsafe_allow_html=True)

# 3. وظيفة الخلفية (بأمان)
def apply_bg():
    try:
        with open("background.png", "rb") as f:
            data = f.read()
            base64_img = base64.b64encode(data).decode()
        st.markdown(
            f'<style>.stApp {{background-image: url("data:image/png;base64,{base64_img}"); background-size: cover;}}</style>',
            unsafe_allow_html=True
        )
    except:
        # لو الصورة مش موجودة، حط لون كحلي عشان الصفحة متبيضش
        st.markdown('<style>.stApp {background-color: #001324;}</style>', unsafe_allow_html=True)

apply_bg()

# 4. دالة فحص الرموز الخاصة
def is_clean(text):
    return not bool(re.search(r'[^a-zA-Z0-9\u0621-\u064A ]', text))

# 5. إدارة الجلسة
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- واجهة الدخول ---
if not st.session_state.logged_in:
    with st.sidebar:
        st.markdown("<h2 style='text-align: center;'>🛡️ SecureNow</h2>", unsafe_allow_html=True)
        st.markdown("---")
        
        with st.form("login_form"):
            st.markdown("<h3 style='text-align: center;'>تسجيل الدخول</h3>", unsafe_allow_html=True)
            u = st.text_input("اسم المستخدم", placeholder="ادخل اسمك هنا...")
            p = st.text_input("كلمة المرور", type="password")
            st.checkbox("تذكرني على هذا الجهاز", value=True)
            
            submit = st.form_submit_button("دخول للنظام")
            
            if submit:
                if not u or not p:
                    st.error("❌ الخانات فاضية! مينفعش تسيبها كدة.")
                elif not is_clean(u):
                    st.error("⚠️ ممنوع استخدام رموز مثل (@, #, $, *, &)")
                else:
                    # بيانات تجريبية
                    if u == "admin" and p == "123":
                        st.session_state.logged_in = True
                        st.toast("أهلاً بك يا بطل! 🎉")
                        st.rerun()
                    else:
                        st.error("❌ البيانات غلط، جرب تاني")
        
        if st.button("نسيت كلمة المرور؟"):
            st.info("💡 كلم الإدارة عشان يغيرولك الباسورد.")

# --- واجهة التطبيق ---
else:
    st.title("لوحة التحكم - SecureNow")
    if st.sidebar.button("خروج"):
        st.session_state.logged_in = False
        st.rerun()
    st.success("تم الدخول بنجاح والاتصال مؤمن.")