import streamlit as st
import pandas as pd
import numpy as np
import joblib  # أو pickle لتحميل الموديل الخاص بك

# إعدادات الصفحة
st.set_page_config(page_title="Credit Scoring System", layout="wide")

# العنوان والوصف
st.title("📊 نظام تقييم الجدارة الائتمانية والربحية")
st.markdown("""
هذا النظام يستخدم تقنيات التعلم الآلي للتنبؤ باحتمالية تعثر العملاء 
وتحليل الأثر المالي بناءً على قاعدة **5Cs of Credit**.
""")

# --- القائمة الجانبية لإدخال البيانات ---
st.sidebar.header("📋 إدخال بيانات العميل")

def user_input_features():
    income = st.sidebar.number_input("الدخل الشهري (Monthly Income)", min_value=0, value=5000)
    age = st.sidebar.slider("السن (Age)", 18, 75, 30)
    loan_amount = st.sidebar.number_input("قيمة القرض المطلوبة", min_value=0, value=10000)
    credit_history = st.sidebar.selectbox("التاريخ الائتماني", ("جيد جداً", "متعثر سابقاً", "لا يوجد تاريخ"))
    employment_years = st.sidebar.slider("سنوات الخبرة/العمل", 0, 40, 5)
    
    # تحويل البيانات لشكل يفهمه الموديل (مثال مبسط)
    data = {
        'Income': income,
        'Age': age,
        'LoanAmount': loan_amount,
        'YearsAtJob': employment_years,
        'CreditHistory': 1 if credit_history == "جيد جداً" else 0
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# --- عرض البيانات المدخلة ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🔍 مراجعة البيانات المستلمة")
    st.write(input_df)

# --- منطقة التنبؤ (Model Prediction) ---
# ملاحظة: هنا تفترض وجود موديل مسيف باسم 'credit_model.pkl'
# إذا لم يكن موجوداً، سنقوم بعمل محاكاة للنتيجة (Mock Prediction)

st.divider()

try:
    # تحميل الموديل الحقيقي
    # model = joblib.load('credit_model.pkl')
    # prediction = model.predict(input_df)
    # probability = model.predict_proba(input_df)[:, 1]
    
    # محاكاة للنتائج لغرض العرض فقط:
    probability = 0.15 if input_df['Income'][0] > 7000 else 0.65
    prediction = 1 if probability > 0.5 else 0
    
    st.subheader("🤖 نتيجة تحليل الذكاء الاصطناعي")
    
    if prediction == 0:
        st.success(f"✅ العميل مؤهل للحصول على القرض (احتمالية التعثر: {probability:.2%})")
        st.balloons()
    else:
        st.error(f"❌ خطر عالي: نوصي برفض الطلب (احتمالية التعثر: {probability:.2%})")

except Exception as e:
    st.warning("يرجى ربط ملف الموديل (pkl) الخاص بك لتفعيل التنبؤ الحقيقي.")

# --- تحليل الربحية (The Cost Analyst Touch) ---
st.divider()
st.subheader("💰 التحليل المالي والمخاطر (Profitability Analysis)")

with st.expander("عرض تفاصيل العائد والمخاطرة"):
    loan = input_df['LoanAmount'][0]
    interest_rate = 0.20 # افتراض فائدة 20%
    expected_profit = loan * interest_rate
    risk_cost = loan * probability # التكلفة المتوقعة للمخاطرة
    
    m1, m2, m3 = st.columns(3)
    m1.metric("العائد المتوقع", f"{expected_profit:,.0f} EGP")
    m2.metric("تكلفة المخاطرة (Expected Loss)", f"-{risk_cost:,.0f} EGP", delta_color="inverse")
    m3.metric("صافي الربح المتوقع", f"{(expected_profit - risk_cost):,.0f} EGP")

# إضافة رسم بياني بسيط لأهمية العوامل
st.subheader("📈 العوامل الأكثر تأثيراً في القرار")
chart_data = pd.DataFrame({
    'Factor': ['التاريخ الائتماني', 'الدخل', 'السن', 'قيمة القرض'],
    'Importance': [0.45, 0.30, 0.15, 0.10]
})
st.bar_chart(chart_data.set_index('Factor'))

st.info("💡 ملاحظة: هذا النظام يدعم اتخاذ القرار ولا يعوض التقييم البشري النهائي.")