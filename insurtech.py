import streamlit as st
import pandas as pd

# 1. إعداد الصفحة
st.set_page_config(page_title="SecureNow Egypt", page_icon="🛡️", layout="centered")

# 2. تهيئة مخزن البيانات (Session State)
if 'users_db' not in st.session_state:
    st.session_state.users_db = {'admin': '123'} # مستخدم افتراضي
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None
if 'db_policies' not in st.session_state:
    st.session_state.db_policies = []

# --- واجهة الدخول واختيار اللغة ---
if not st.session_state.logged_in:
    st.title("🛡️ SecureNow Egypt")
    
    # اختيار اللغة
    lang = st.radio("Choose Language / اختر اللغة", ["العربية", "English"], horizontal=True)
    
    auth_tabs = st.tabs(["تسجيل الدخول (Login)", "إنشاء حساب (Sign Up)"] if lang == "العربية" else ["Login", "Sign Up"])

    # --- تسجيل الدخول ---
    with auth_tabs[0]:
        with st.form("login"):
            u = st.text_input("Username / اسم المستخدم")
            p = st.text_input("Password / كلمة المرور", type="password")
            if st.form_submit_button("Enter / دخول"):
                if u in st.session_state.users_db and st.session_state.users_db[u] == p:
                    st.session_state.logged_in = True
                    st.session_state.current_user = u
                    st.rerun()
                else:
                    st.error("خطأ في البيانات / Invalid Credentials")

    # --- إنشاء حساب جديد ---
    with auth_tabs[1]:
        with st.form("signup"):
            new_u = st.text_input("Choose Username / اختر اسم مستخدم")
            new_p = st.text_input("Password / كلمة مرور", type="password")
            conf_p = st.text_input("Confirm / تأكيد الكلمة", type="password")
            if st.form_submit_button("Create / إنشاء"):
                if new_p == conf_p and new_u:
                    st.session_state.users_db[new_u] = new_p
                    st.success("Account Created! / تم إنشاء الحساب")
                else:
                    st.error("Check details / تأكد من البيانات")

# --- واجهة التطبيق الحقيقية (بعد الدخول) ---
else:
    st.sidebar.title(f"Welcome, {st.session_state.current_user} 👋")
    menu = ["شراء تأمين", "تأميناتي", "Admin"]
    choice = st.sidebar.radio("Go to:", menu)
    
    if st.sidebar.button("Logout / خروج"):
        st.session_state.logged_in = False
        st.rerun()

    if choice == "شراء تأمين":
        st.header("⚡ اطلب بوليصتك الآن")
        cat = st.selectbox("النوع:", ["🚗 سيارة", "📱 موبايل", "📦 شحنة"])
        days = st.number_input("المدة (أيام):", 1, 30)
        price = days * 50 # سعر افتراضي
        st.metric("التكلفة", f"{price} EGP")
        if st.button("تفعيل ✅"):
            st.session_state.db_policies.append({"User": st.session_state.current_user, "Type": cat, "Price": price})
            st.balloons()
            st.success("تم التفعيل!")

    elif choice == "تأميناتي":
        st.header("📋 بوالصك النشطة")
        user_pols = [p for p in st.session_state.db_policies if p['User'] == st.session_state.current_user]
        if user_pols:
            st.table(pd.DataFrame(user_pols))
        else:
            st.info("لا توجد بوالص حالياً.")

    elif choice == "Admin":
        st.header("📊 لوحة الإدارة")
        if st.session_state.db_policies:
            st.write("إجمالي المبيعات:")
            st.table(pd.DataFrame(st.session_state.db_policies))
        else:
            st.write("لا توجد بيانات.")
            