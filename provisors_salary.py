from parts_of_salary.parts_of_provisor import PartsOfSalaryPharmacist


def amount_of_salary(hours: int,
                     plan_3_percent: float,
                     etm_percent: float,
                     gold: int,
                     amount_of_profit: int) -> float:

    salary_parts = PartsOfSalaryPharmacist(
        etm_percent=etm_percent,
        plan_3_percent=plan_3_percent,
        ke=amount_of_profit,
        hours=hours
    )

    total = (
            salary_parts.plan_3_realization() +
            salary_parts.etm_realization() +
            salary_parts.category_effectivity() +
            salary_parts.tpk +
            salary_parts.rate +
            gold
    )
    print(f"ВП: {round(salary_parts.plan_3_realization(), 2)},\n"
          f"ВТМ: {round(salary_parts.etm_realization(), 2)},\n"
          f"КЕ: {round(salary_parts.category_effectivity(), 2)},\n"
          f"ТПК: {round(salary_parts.tpk, 2)},\n"
          f"СТ: {round(salary_parts.rate, 2)}")
    return round(total, 2)


print(amount_of_salary(int(input('Години: ')),
                       float(input('Виконання плану 3: ')),
                       float(input('Виконання ВТМ: ')),
                       int(input('Голд: ')),
                       int(input('Виторг: '))))
