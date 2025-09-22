from customer import Customer
from equipment import Equipment
from trainer import Trainer
from subscription import Subscription
from exercisePlan import ExercisePlan
from gym import Gym

customer = Customer("John", "Maple Street", "john@abv.bg")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()
gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))