from utils import *
from datetime import datetime


if __name__ == '__main__':
    #===============
    print("\n[[Food]]")
    apple = Food('apple')
    print(apple.name)
    # print('apple {}'.format(apple.calories))  #Error
    # apple.name = 'AAA'  # Error
    # print(apple.get_composition()) # Error
    apple.set_composition(1,2,3)
    print(apple.get_composition())
    print('apple {}'.format(apple.calories))

    banana = Food('banana',2,3,4)
    print('banana {}'.format(banana.calories))

    #===============
    print("\n[[Meal]]")
    meal = Meal('Lunch',datetime.today())
    print('meal {}'.format(meal.totalCalories))
    meal.add_food(apple)
    print('add food {}'.format(meal.totalCalories))
    meal.add_food(banana)
    print('add food {}'.format(meal.totalCalories))
    meal.empty_inTake()
    print('empty food {}'.format(meal.totalCalories))
    meal.add_food([apple,banana])
    print('add food {}'.format(meal.totalCalories))

    meal2 = Meal('Diner',datetime.today(),[apple,apple,apple])
    print('Diner {}'.format(meal2.totalCalories))

    #===============
    print("\n[[DailyIntakeCalories]]")
    today = DailyIntakeCalories(datetime.today())
    today.add_meal(meal)
    print('add meal {}'.format(today.total_intake_calories))
    today.add_meal(meal2)
    print('add meal {}'.format(today.total_intake_calories))
    today.empty_inTake()
    print('empty meal {}'.format(today.total_intake_calories))

    today.add_meal([meal,meal2])
    print('meal {}'.format(today.total_intake_calories))

    #===============
    print('End')
