import streamlit as st
from parts_of_salary.parts_of_provisor import PartsOfSalaryPharmacist

st.title("Калькулятор зарплати провізора")

hours = st.number_input('Години', min_value=0)
plan_3 = st.number_input('Виконання плану 3 (%)', min_value=0.0)
etm = st.number_input('Виконання ВТМ (%)', min_value=0.0)
gold = st.number_input('Голди', min_value=0)
profit = st.number_input('Виторг ', min_value=0)

if st.button("Розрахувати"):
    salary_parts = PartsOfSalaryPharmacist(
        etm_percent=etm,
        plan_3_percent=plan_3,
        ke=profit,
        hours=hours
    )

    total = (
        salary_parts.plan_3_realization() +
        salary_parts.etm_realization() +
        salary_parts.tpk +
        salary_parts.rate +
        gold
    )

    st.success(f"Загальна зарплата: {round(total, 2)} грн")

    with st.expander("Деталізація"):
        st.write(f"ВП: {round(salary_parts.plan_3_realization(), 2)} грн")
        st.write(f"ВТМ: {round(salary_parts.etm_realization(), 2)} грн")
        st.write(f"ТПК: {round(salary_parts.tpk, 2)} грн")
        st.write(f"СТ: {round(salary_parts.rate, 2)} грн")
