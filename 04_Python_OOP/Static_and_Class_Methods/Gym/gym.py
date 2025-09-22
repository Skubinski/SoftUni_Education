class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, eq):
        if eq not in self.equipment:
            self.equipment.append(eq)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subs):
        if subs not in self.subscriptions:
            self.subscriptions.append(subs)

    def subscription_info(self, subscription_id):
        subs = self.__find_element(self.subscriptions, subscription_id)
        customer_id = subs.customer_id
        customer = self.__find_element(self.customers, customer_id)
        trainer_id = subs.trainer_id
        trainer = self.__find_element(self.trainers, trainer_id)
        plan_id = subs.exercise_id
        plan = self.__find_element(self.plans, plan_id)
        equipment_id = plan.equipment_id
        equipment = self.__find_element(self.equipment, equipment_id)

        result = ""
        result += f"{subs.__repr__()}\n"
        result += f"{customer.__repr__()}\n"
        result += f"{trainer.__repr__()}\n"
        result += f"{plan.__repr__()}\n"
        result += f"{equipment.__repr__()}"

        return result

    def __find_element(self, iter, subs_id):
        for s in iter:
            if s.id == subs_id:
                return s

