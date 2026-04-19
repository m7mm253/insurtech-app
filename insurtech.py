import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="SecureNow Egypt", page_icon="🛡️", layout="centered")

# 2. إدارة الحالة (Session State) للغة وتسجيل الدخول
if 'language' not in st.session_state:
    st.session_state.language = 'العربية'
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- قاموس اللغات (Translations) ---
texts = {
    'العربية': {
        'welcome': 'مرحباً بك في SecureNow',
        'login': 'تسجيل الدخول',
        'user': 'اسم المستخدم',
        'pass': 'كلمة المرور',
        'enter': 'دخول',
        'logout': 'تسجيل خروج',
        'buy': 'شراء تأمين',
        'my_policies': 'تأميناتي',
        'admin': 'الإدارة',
        'error': 'بيانات الدخول غير صحيحة'
    },
    'English': {
        'welcome': 'Welcome to SecureNow',
        'login': 'Login',
        'user': 'Username',
        'pass': 'Password',
        'enter': 'Enter',
        'logout': 'Logout',
        'buy': 'Buy Insurance',
        'my_policies': 'My Policies',
        'admin': 'Admin Dashboard',
        'error': 'Invalid credentials'
    }
}

# --- شاشة اختيار اللغة وتسجيل الدخول ---
if not st.session_state.logged_in:
    st.title("🛡️ SecureNow")
    
    # اختيار اللغة
    lang = st.radio("Choose Language / اختر اللغة", ["العربية", "English"], horizontal=True)
    st.session_state.language = lang
    T = texts[st.session_state.language]
    
    st.subheader(T['login'])
    
    # واجهة تسجيل الدخول
    with st.form("login_form"):
        username = st.text_input(T['user'])
        password = st.text_input(T['pass'], type="password")
        submit = st.form_submit_button(T['enter'])
        
        if submit:
            # تجربة: اسم المستخدم admin وكلمة السر 123
            if username == "admin" and password == "123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error(T['error'])

# --- التطبيق الأصلي (يظهر بعد تسجيل الدخول) ---
else:
    T = texts[st.session_state.language]
    
    # القائمة الجانبية
    st.sidebar.title(f"🛡️ {T['welcome']}")
    choice = st.sidebar.radio("Menu", [T['buy'], T['my_policies'], T['admin']])
    
    if st.sidebar.button(T['logout']):
        st.session_state.logged_in = False
        st.rerun()

    # محتوى التطبيق (الجزء اللي عملناه قبل كدة)
    if choice == T['buy']:
        st.header(T['buy'])
        st.write("هنا تظهر واجهة الشراء...")
        # يمكنك وضع كود الشراء السابق هنا
        
    elif choice == T['my_policies']:
        st.header(T['my_policies'])
        st.write("هنا تظهر قائمة التأمينات...")

    elif choice == T['admin']:
        st.header(T['admin'])
        st.write("لوحة التحكم الخاصة بالإدارة")