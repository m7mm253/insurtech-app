import streamlit as st
import base64
import re

# 1. إعدادات الصفحة
st.set_page_config(page_title="SecureNow Egypt", page_icon="🛡️", layout="wide")

# 2. وظيفة تحميل الخلفية (الصورة بتاعتك)
def get_base64_img(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

bg_data = get_base64_img('background.png')

# 3. الـ CSS (الديزاين الجديد المستوحى من Lemonade)
style_css = f"""
<style>
    header, footer, #MainMenu {{visibility: hidden;}}
    .stApp {{
        background-image: url("data:image/png;base64,{bg_data}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        direction: RTL;
    }}
    .navbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 60px;
        background-color: rgba(10, 25, 41, 0.85);
        position: fixed;
        top: 0; left: 0; width: 100%;
        z-index: 999;
    }}
    .login-card {{
        background-color: rgba(10, 25, 41, 0.9);
        border: 2px solid #00f2fe;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 0 25px rgba(0, 242, 254, 0.3);
    }}
    .display-preview {{
        background-color: rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        height: 380px;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    h1, h2, h3, p, label {{ color: white !important; text-align: right; }}
</style>
"""
st.markdown(style_css, unsafe_allow_html=True)

# 4. الـ Navbar العلوي
st.markdown('<div class="navbar"><div style="color: white; font-size: 22px; font-weight: bold;">🛡️ SecureNow</div><div style="color: white; direction: RTL; gap: 15px; display: flex;"><span>الرئيسية</span><span>الخدمات</span></div><button style="background-color: #00f2fe; border: none; padding: 5px 15px; border-radius: 5px;">ابدأ</button></div>', unsafe_allow_html=True)

st.write("##") # مسافة للأمان

# 5. الـ Hero Section (تقسيمة Lemonade)
col_right, col_left = st.columns([1, 1.2], gap="large")

with col_right:
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown("<h2 style='margin-bottom: 0;'>مستقبل التأمين</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 15px; opacity: 0.8;'>حماية ذكية مدعومة بالذكاء الاصطناعي</p>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        u = st.text_input("اسم المستخدم", placeholder="User123")
        p = st.text_input("كلمة المرور", type="password")
        submit = st.form_submit_button("دخول")
        
        if submit:
            if not u or not p:
                st.error("❌ الخانات فاضية")
            elif bool(re.search(r'[^a-zA-Z0-9\u0621-\u064A ]', u)):
                st.error("⚠️ ممنوع الرموز (@, #, $)")
            elif u == "admin" and p == "123":
                st.success("تم الدخول!")
            else:
                st.error("❌ البيانات غلط")
    st.markdown('</div>', unsafe_allow_html=True)

with col_left:
    st.markdown('<div class="display-preview"><h3 style="color: #00f2fe;">[ واجهة عرض البيانات ]</h3></div>', unsafe_allow_html=True)
    st.markdown('<div style="display: flex; justify-content: center; gap: 20px; margin-top: 15px;"><span style="color: #00f2fe; border-bottom: 2px solid #00f2fe;">السيارات</span><span style="color: white; opacity: 0.5;">الموبايل</span></div>', unsafe_allow_html=True)