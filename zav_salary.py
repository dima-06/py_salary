from parts_of_salary.parts_of_zav import PartsOfSalary


def amount_of_salary(hours: int,
                     plan_3_percent: float,
                     etm_percent: float,
                     gold: int,
                     overall_goal: int,
                     amount_of_profit: int,
                     other: int) -> float:

    salary_parts = PartsOfSalary(
        etm_percent=etm_percent,
        plan_3_percent=plan_3_percent,
        ke=amount_of_profit,
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
    print(f"ВП: {round(salary_parts.plan_3_realization(), 2)},\n"
          f"ВТМ: {round(salary_parts.etm_realization(), 2)},\n"
          f"КЕ: {round(salary_parts.category_effectivity_zav(), 2)},\n"
          f"ТПК: {round(salary_parts.tpk, 2)},\n"
          f"СТ: {round(salary_parts.rate, 2)},\n"
          f"Загальна ціль: {round((overall_goal * 1.2), 2)},\n"
          f"ФО: {round(salary_parts.education, 2)}")
    return round(total, 2)


print(amount_of_salary(int(input('Години: ')),
                       float(input('Виконання плану 3: ')),
                       float(input('Виконання ВТМ: ')),
                       int(input('Голд: ')),
                       int(input('Загальна ціль: ')),
                       int(input('Виторг аптеки: ')),
                       int(input('Інвентаризація, стажування і т.д.: '))))
