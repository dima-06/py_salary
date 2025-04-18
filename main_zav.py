import streamlit as st
from parts_of_salary.parts_of_zav import PartsOfSalary

st.title("Калькулятор зарплати завідувача")

hours = st.number_input('Години', min_value=0)
plan_3 = st.number_input('Виконання плану 3 (%)', min_value=0.0)
etm = st.number_input('Виконання ВТМ (%)', min_value=0.0)
gold = st.number_input('Голди', min_value=0)
overall_goal = st.number_input('Загальна ціль', min_value=0)
profit = st.number_input('Виторг аптеки', min_value=0)
other = st.number_input('Інше (інвентаризація, стажування...)', min_value=0)

if st.button("Розрахувати"):
    salary_parts = PartsOfSalary(
        etm_percent=etm,
        plan_3_percent=plan_3,
        ke=profit,
        hours=hours
    )

    total = (
        salary_parts.plan_3_realization() +
        salary_parts.etm_realization() +
        salary_parts.category_effectivity_zav() +
        salary_parts.tpk +
        salary_parts.rate +
        salary_parts.education +
        gold +
        (overall_goal * 1.2) +
        other
    )

    st.success(f"Загальна зарплата: {round(total, 2)} грн")

    with st.expander("Деталізація"):
        st.write(f"ВП: {round(salary_parts.plan_3_realization(), 2)} грн")
        st.write(f"ВТМ: {round(salary_parts.etm_realization(), 2)} грн")
        st.write(f"КЕ: {round(salary_parts.category_effectivity_zav(), 2)} грн")
        st.write(f"ТПК: {round(salary_parts.tpk, 2)} грн")
        st.write(f"СТ: {round(salary_parts.rate, 2)} грн")
        st.write(f"ФО: {round(salary_parts.education, 2)} грн")
        st.write(f"Загальна ціль: {round((overall_goal * 1.2), 2)} грн")
