import streamlit as st
import re # مكتبة الـ Regular Expressions للبحث عن الرموز

# ... (نفس كود الـ CSS والخلفية من المرة اللي فاتت) ...

# دالة للتحقق من وجود رموز خاصة
def has_special_chars(string):
    # بتبحث عن أي رمز مش حرف أو رقم
    return bool(re.search(r'[^a-zA-Z0-9 ]', string))

# --- داخل الـ Form بتاع تسجيل الدخول أو إنشاء الحساب ---
with st.sidebar.form("auth_form"):
    u = st.text_input("اسم المستخدم")
    p = st.text_input("كلمة المرور", type="password")
    submit = st.form_submit_button("دخول")

    if submit:
        # 1. تنبيه لو الخانات فاضية
        if not u or not p:
            st.error("❌ عذراً، لا يمكن ترك اسم المستخدم أو كلمة المرور فارغة")
        
        # 2. تنبيه لو استخدم رموز خاصة (@, #, $, إلخ)
        elif has_special_chars(u):
            st.error("⚠️ خطأ: اسم المستخدم يجب أن يحتوي على حروف وأرقام فقط (بدون @، #، *، إلخ)")
        
        # 3. التحقق من صحة البيانات
        else:
            if u == "admin" and p == "123":
                st.session_state.logged_in = True
                st.toast("تم الدخول بنجاح 🎉")
                st.rerun()
            else:
                st.error("❌ بيانات الدخول غير صحيحة")