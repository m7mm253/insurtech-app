import streamlit as st
import base64
import re

# 1. إعدادات الصفحة
st.set_page_config(page_title="InsurTech", page_icon="🛡️", layout="wide")

# 2. وظيفة تحميل الخلفية (لازم تتأكد إن الصورة مرفوعة باسم background.png)
def get_base64_img(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

bg_data = get_base64_img('background.png')

# 3. CSS مطور للموبايل (Media Queries)
style_css = f"""
<style>
    header, footer, #MainMenu {{visibility: hidden;}}
    
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url("data:image/png;base64,{bg_data}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* تصميم الـ Navbar ليكون مرن */
    .nav-bar {{
        background: rgba(10, 25, 41, 0.95);
        padding: 10px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: fixed;
        top: 0; left: 0; width: 100%;
        z-index: 1000;
        border-bottom: 2px solid #00f2fe;
    }}

    /* ضبط الحاويات للموبايل */
    @media (max-width: 768px) {{
        .login-box {{
            margin-top: 80px !important;
            padding: 20px !important;
        }}
        h1 {{ font-size: 28px !important; }}
        .display-screen {{ height: 250px !important; margin-top: 20px; }}
    }}

    .login-box {{
        background: rgba(15, 32, 54, 0.9);
        border: 1px solid #00f2fe;
        border-radius: 15px;
        padding: 30px;
        direction: RTL;
    }}

    .display-screen {{
        background: rgba(0,0,0,0.3);
        border: 1px solid rgba(0, 242, 254, 0.2);
        border-radius: 15px;
        height: 400px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
    }}

    h1, h2, h3, p, label {{ color: white !important; text-align: right; }}
    
    /* جعل أزرار الاستريم ليت تتفاعل صح */
    .stButton>button {{
        width: 100% !important;
        background-color: #00f2fe !important;
        color: #0a1929 !important;
        border-radius: 8px !important;
        border: none !important;
        height: 45px;
    }}
</style>
"""
st.markdown(style_css, unsafe_allow_html=True)

# 4. الـ Navbar
st.markdown("""
    <div class="nav-bar">
        <div style="font-size: 20px; font-weight: bold; color: #00f2fe;">🛡️ InsurTech</div>
        <div style="color: white; direction: RTL; font-size: 14px; display: flex; gap: 10px;">
            <span>الرئيسية</span>
            <span>الدعم</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# مسافة للأمان عشان الـ Navbar ميتغطاش
st.write("###")

# 5. الجسم الرئيسي باستخدام الترتيب الذكي
# في الموبايل الـ Login هيظهر الأول وبعده الشاشة
col_right, col_left = st.columns([1, 1.2])

with col_right:
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown("<h1>أمن مستقبلك بلمسة</h1>", unsafe_allow_html=True)
    
    with st.form("mobile_login_form"):
        user = st.text_input("اسم المستخدم")
        pwd = st.text_input("كلمة المرور", type="password")
        
        # الزرار هنا لازم يكون جوه الـ form عشان يشتغل
        submitted = st.form_submit_button("تسجيل الدخول")
        
        if submitted:
            if not user or not pwd:
                st.error("الخانات فاضية!")
            elif user == "admin" and pwd == "123":
                st.success("تم الدخول!")
                st.balloons()
            else:
                st.error("البيانات خطأ")
    st.markdown('</div>', unsafe_allow_html=True)

with col_left:
    st.markdown("""
        <div class="display-screen">
            <h3 style="color: #00f2fe; padding: 10px;">[ واجهة التحليل الذكي ]</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # أزرار سفلية بسيطة
    cols = st.columns(3)
    cols[0].markdown("<p style='text-align:center; font-size:12px; color:#00f2fe;'>سيارات</p>", unsafe_allow_html=True)
    cols[1].markdown("<p style='text-align:center; font-size:12px; color:white;'>ممتلكات</p>", unsafe_allow_html=True)
    cols[2].markdown("<p style='text-align:center; font-size:12px; color:white;'>سفر</p>", unsafe_allow_html=True)