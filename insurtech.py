import streamlit as st
import base64
import re

# 1. إعدادات الصفحة واسم التطبيق
st.set_page_config(page_title="InsurTech", page_icon="🛡️", layout="wide")

# 2. وظيفة تحميل الخلفية (تأكد أن الملف اسمه background.png)
def get_base64_img(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

bg_data = get_base64_img('background.png')

# 3. الـ CSS السحري (RTL + إخفاء الأدوات + Responsive)
style_css = f"""
<style>
    /* إخفاء شريط الأدوات العلوي والأسفل تماماً */
    header, footer, #MainMenu {{visibility: hidden;}}
    
    /* ضبط الخلفية والاتجاه العام للعربية */
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("data:image/png;base64,{bg_data}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        direction: RTL;
        text-align: right;
    }}

    /* كارت تسجيل الدخول */
    .auth-card {{
        background: rgba(10, 25, 41, 0.9);
        border: 2px solid #00f2fe;
        border-radius: 20px;
        padding: 40px;
        max-width: 500px;
        margin: auto;
        box-shadow: 0 0 30px rgba(0, 242, 254, 0.3);
    }}

    /* تحسين الخانات والزراير للموبايل */
    h1, h2, h3, p, label {{ color: white !important; font-family: 'Tahoma', sans-serif; }}
    .stButton>button {{
        width: 100% !important;
        background-color: #00f2fe !important;
        color: #0a1929 !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        height: 48px !important;
    }}
    
    /* منع الرموز من قلب اتجاه الخانات */
    input {{ direction: RTL !important; text-align: right !important; }}
</style>
"""
st.markdown(style_css, unsafe_allow_html=True)

# 4. إدارة حالة الجلسة (Session State)
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# 5. واجهة المستخدم (UI)
if not st.session_state.logged_in:
    # شريط علوي بسيط للغة والتسجيل الجديد
    col_lang, col_reg = st.columns([1, 1])
    with col_lang:
        st.selectbox("🌐 اللغة", ["العربية", "English"])
    with col_reg:
        if st.button("إنشاء حساب جديد"):
            st.toast("سيتم فتح صفحة التسجيل قريباً")

    st.write("##") # مسافة

    # حاوية الدخول الرئيسية
    st.markdown('<div class="auth-card">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>🛡️ InsurTech</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; opacity: 0.8;'>سجل دخولك للوصول لنظام التأمين الذكي</p>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        u = st.text_input("اسم المستخدم", placeholder="User123")
        p = st.text_input("كلمة المرور", type="password")
        
        col_check, col_forgot = st.columns([1, 1])
        with col_check:
            remember = st.checkbox("تذكرني")
        with col_forgot:
            # زر "نسيت كلمة المرور" داخل الفورم لضبط الشكل
            pass # سيتم وضعه بالخارج ليعمل كـ Button

        submit = st.form_submit_button("تسجيل الدخول")
        
        # --- نظام التنبيهات الذكي (التحقق من البيانات) ---
        if submit:
            if not u or not p:
                st.error("❌ عذراً، يجب إدخال اسم المستخدم وكلمة المرور")
            elif bool(re.search(r'[^a-zA-Z0-9\u0621-\u064A ]', u)):
                st.error("⚠️ خطأ: لا يسمح باستخدام رموز خاصة مثل (#, $, @, *)")
            elif u == "admin" and p == "123":
                st.session_state.logged_in = True
                st.success("تم الدخول بنجاح! 🎉")
                st.rerun()
            else:
                st.error("❌ خطأ في البيانات، تأكد من صحة الحساب")
    
    if st.button("Forgot Password / نسيت كلمة المرور؟"):
        st.info("💡 يرجى مراسلة الدعم الفني لاستعادة حسابك.")
        
    st.markdown('</div>', unsafe_allow_html=True)

# 6. واجهة التطبيق بعد الدخول
else:
    st.success("أهلاً بك في لوحة تحكم InsurTech")
    if st.button("تسجيل الخروج"):
        st.session_state.logged_in = False
        st.rerun()