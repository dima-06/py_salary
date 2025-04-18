class PartsOfSalaryPharmacist:
    def __init__(self,
                 etm_percent,
                 plan_3_percent,
                 ke,
                 hours) -> None:
        self.hours = hours / 180
        self.rate = 6588 * self.hours
        self.etm = etm_percent
        self.tpk = 1000 * self.hours
        self.plan_3 = plan_3_percent
        self.ke = ke

    def plan_3_realization(self):
        if self.plan_3 < 90:
            return 0
        elif 90 <= self.plan_3 < 95:
            return 6588 * 0.1 * self.hours
        elif 95 <= self.plan_3 < 100:
            return 6588 * 0.35 * self.hours
        elif 100 <= self.plan_3 < 105:
            return 6588 * 0.45 * self.hours
        elif 105 <= self.plan_3 < 110:
            return 6588 * 0.6 * self.hours
        elif 110 <= self.plan_3 < 115:
            return 6588 * 0.75 * self.hours
        elif self.plan_3 >= 115:
            return 6588 * 0.9 * self.hours

    def etm_realization(self):
        if self.etm < 90:
            return 0
        elif 90 <= self.etm < 95:
            return 6588 * 0.05 * self.hours
        elif 95 <= self.etm < 100:
            return 6588 * 0.15 * self.hours
        elif 100 <= self.etm < 105:
            return 6588 * 0.2 * self.hours
        elif 105 <= self.etm < 110:
            return 6588 * 0.25 * self.hours
        elif 110 <= self.etm < 115:
            return 6588 * 0.3 * self.hours
        elif self.etm >= 115:
            return 6588 * 0.35 * self.hours

    def category_effectivity(self):
        if self.ke < 200_000:
            return 0
        elif 200_000 <= self.ke < 250_000:
            return 600
        elif 250_000 <= self.ke < 300_000:
            return 900
        elif 300_000 <= self.ke < 400_000:
            return 1300
        elif 400_000 <= self.ke < 500_000:
            return 1800
        elif self.ke > 500_000:
            return 2400
