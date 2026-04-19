import streamlit as st
import pandas as pd
from datetime import datetime

# إعداد الصفحة لتكون سريعة التحميل
st.set_page_config(page_title="SecureNow Egypt", page_icon="🛡️")

# --- محاكاة قاعدة البيانات (عشان نتفادى مشاكل الملفات حالياً) ---
if 'db_policies' not in st.session_state:
    st.session_state.db_policies = []
if 'db_claims' not in st.session_state:
    st.session_state.db_claims = []

st.title("🛡️ SecureNow Egypt")
st.info("أهلاً بك في منصة التأمين المرن - نسخة تجريبية (MVP)")

# --- القائمة الجانبية ---
menu = ["شراء تأمين", "تأميناتي ومطالباتي", "لوحة الإدارة (Admin)"]
choice = st.sidebar.radio("انتقل إلى:", menu)

# --- 1. واجهة الشراء ---
if choice == "شراء تأمين":
    st.subheader("⚡ اختر بوليصتك المناسبة")
    
    category = st.selectbox("نوع التأمين:", ["🚗 سيارة (يومي)", "📱 موبايل (سفر)", "📦 شحنة صغيرة"])
    days = st.slider("المدة باليوم:", 1, 30, 1)
    
    # حساب السعر
    rates = {"🚗 سيارة (يومي)": 50, "📱 موبايل (سفر)": 15, "📦 شحنة صغيرة": 5}
    total = rates[category] * days
    
    st.metric("السعر الإجمالي", f"{total} EGP")
    
    phone = st.text_input("أدخل رقم الموبايل لتأكيد الشراء")
    
    if st.button("تفعيل التأمين ✅"):
        if phone:
            new_p = {"ID": len(st.session_state.db_policies)+101, "User": phone, "Type": category, "Status": "Active"}
            st.session_state.db_policies.append(new_p)
            st.success(f"تم تفعيل التأمين! رقم البوليصة: {new_p['ID']}")
            st.balloons()
        else:
            st.error("من فضلك أدخل رقم الموبايل أولاً")

# --- 2. واجهة المطالبات ---
elif choice == "تأميناتي ومطالباتي":
    st.subheader("📋 متابعة بوالصك")
    if st.session_state.db_policies:
        st.table(pd.DataFrame(st.session_state.db_policies))
        
        st.divider()
        st.subheader("⚠️ تقديم طلب تعويض (Claim)")
        p_id = st.number_input("أدخل رقم البوليصة:", min_value=101)
        desc = st.text_area("وصف الحادث")
        if st.button("إرسال المطالبة"):
            new_c = {"PolicyID": p_id, "Description": desc, "Status": "Pending"}
            st.session_state.db_claims.append(new_c)
            st.warning("تم إرسال طلبك وجاري مراجعته.")
    else:
        st.write("لا توجد بوالص نشطة حالياً.")

# --- 3. لوحة الإدارة ---
elif choice == "لوحة الإدارة (Admin)":
    st.subheader("📊 إحصائيات النظام")
    col1, col2 = st.columns(2)
    col1.metric("عدد العملاء", len(st.session_state.db_policies))
    col2.metric("طلبات التعويض", len(st.session_state.db_claims))
    
    st.write("**طلبات التعويض الواردة:**")
    if st.session_state.db_claims:
        st.table(pd.DataFrame(st.session_state.db_claims))
    else:
        st.write("لا توجد طلبات حالياً.")