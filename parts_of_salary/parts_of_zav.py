class PartsOfSalary:
    def __init__(self,
                 etm_percent,
                 plan_3_percent,
                 ke,
                 hours) -> None:
        self.hours = hours / 189
        self.rate = 8064 * self.hours
        self.etm = etm_percent
        self.tpk = 1000 * self.hours
        self.plan_3 = plan_3_percent
        self.ke = ke
        self.education = 2000 * self.hours

    def plan_3_realization(self):
        if self.plan_3 < 90:
            return 0
        elif 90 <= self.plan_3 < 95:
            return 8064 * 0.1 * self.hours
        elif 95 <= self.plan_3 < 100:
            return 8064 * 0.35 * self.hours
        elif 100 <= self.plan_3 < 105:
            return 8064 * 0.45 * self.hours
        elif 105 <= self.plan_3 < 110:
            return 8064 * 0.6 * self.hours
        elif 110 <= self.plan_3 < 115:
            return 8064 * 0.75 * self.hours
        elif self.plan_3 >= 115:
            return 8064 * 0.9 * self.hours

    def etm_realization(self):
        if self.etm < 90:
            return 0
        elif 90 <= self.etm < 95:
            return 8064 * 0.05 * self.hours
        elif 95 <= self.etm < 100:
            return 8064 * 0.15 * self.hours
        elif 100 <= self.etm < 105:
            return 8064 * 0.2 * self.hours
        elif 105 <= self.etm < 110:
            return 8064 * 0.25 * self.hours
        elif 110 <= self.etm < 115:
            return 8064 * 0.3 * self.hours
        elif self.etm >= 115:
            return 8064 * 0.35 * self.hours

    def category_effectivity_zav(self):
        if self.ke < 500_000:
            return 0
        elif 500_000 <= self.ke < 750_000:
            return 1500
        elif 750_000 <= self.ke < 1_000_000:
            return 2000
        elif 1_000_000 <= self.ke < 1_500_000:
            return 2500
        elif 1_500_000 <= self.ke < 2_000_000:
            return 3000
        elif 2_000_000 <= self.ke < 3_000_000:
            return 3500
