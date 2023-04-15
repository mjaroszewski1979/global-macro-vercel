from django.db.models import Max

# App imports
from .models import UserCars

def get_max_order(user) -> int:
    """
    This function will return integer holding the value of 1 in case of non existing
    UserCars model objects. Otherwise it will use django aggergate mechanism as well as 
    Max function to retrieve a maximum value of 'order' field incremented by 1.

    :type name: object
    :param user: contains data about logged-in user
    """
    existing_cars = UserCars.objects.filter(user=user)
    if not existing_cars.exists():
        return 1
    else:
        current_max = existing_cars.aggregate(max_order=Max('order'))['max_order']
        return current_max + 1

def reorder(user):
    """
    This function will firstly check for existing UserCars model objects and it will
    use django count function to obtain the number of instances. After incrementing 
    by 1 and passing to range function the returned sequence of numbers will serve as a
    new ordering for car objects belonging to logged-in user.

    :type name: object
    :param user: contains data about logged-in user
    """
    existing_cars = UserCars.objects.filter(user=user)
    if not existing_cars.exists():
        return
    num_of_cars = existing_cars.count()
    new_ordering = range(1, num_of_cars+1)
    for order, user_car in zip(new_ordering, existing_cars):
        user_car.order = order
        user_car.save()