import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("売上データ可視化アプリ")

# CSVアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロード", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("データプレビュー")
    st.dataframe(df)

    # 月別売上集計
    monthly_sales = df.groupby("Month")["Amount"].sum()
    st.write("月別売上集計")
    st.bar_chart(monthly_sales)

    # 顧客別売上集計
    customer_sales = df.groupby("Customer")["Amount"].sum()
    st.write("顧客別売上集計")
    st.line_chart(customer_sales)
