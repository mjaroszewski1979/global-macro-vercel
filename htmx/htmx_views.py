from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# App imports
from .models import Car, UserCars
from .utils import get_max_order, reorder

def check_username(request):
    """
    This function will check if submited username already exists. It filters user model
    with data obtained from post request send by htmx (forms name attribute) and returns http response.

    :type name: HttpRequest object
    :param request: contains metadata about the request
    """
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("This username already exists")
    else:
        return HttpResponse("This username is available")

@login_required
def add_car(request):
    """
    This function uses login_required decorator to secure view by forcing the client 
    to authenticate with a valid logged-in User. After fetching car producer submited via
    htmx post request it checks for existing UserCars objects. If car with provided car producer
    name does not exists this function will add new record to UserCars model. It will attach success
    message to request object and make it available in the frontend template.

    :type name: HttpRequest object
    :param request: contains metadata about the request
    """
    car_producer = request.POST.get('car_producer')
    car = Car.objects.get_or_create(producer=car_producer)[0]
    if not UserCars.objects.filter(car=car, user=request.user).exists():
        UserCars.objects.create(car=car, user=request.user, order=get_max_order(request.user))
    cars = UserCars.objects.filter(user=request.user)
    messages.success(request, f"ADDED {car_producer.upper()} TO LIST OF CARS")
    return render(request, 'partials/car_list.html', {'cars': cars})

@login_required
@require_http_methods(['DELETE'])
def delete_car(request, id):
    """
    This function uses login_required decorator to secure view by forcing the client 
    to authenticate with a valid logged-in User. It is also utilizing require_hhtp_methods
    decorator to enable only delete requests. This function will delete existing object
    from UserCars model with given id number.

    :type name: HttpRequest object
    :param request: contains metadata about the request
    :type name: int
    :param id: field added automatically by django - auto-incrementing primary key
    """
    UserCars.objects.get(id=id).delete()
    reorder(request.user)
    cars = UserCars.objects.filter(user=request.user)
    return render(request, 'partials/car_list.html', {'cars': cars})

@login_required
def search_car(request):
    """
    This function uses login_required decorator to secure view by forcing the client 
    to authenticate with a valid logged-in User. After fetching search text submited via
    htmx post request it filters existing Car model objects. It is also excluding from
    search results currently logged-in UserCars objects. It utilizes icontains parameter
    to ensure case insensitive filtering.

    :type name: HttpRequest object
    :param request: contains metadata about the request
    """
    search_text = request.POST.get('search')

    user_cars = UserCars.objects.filter(user=request.user)
    results = Car.objects.filter(producer__icontains=search_text).exclude(
        producer__in=user_cars.values_list('car__producer', flat=True)
    )
    context = {"results": results}
    return render(request, 'partials/search_results.html', context)

@login_required
def detail(request, id):
    """
    This function uses login_required decorator to secure view by forcing the client 
    to authenticate with a valid logged-in User. It returns details of a single model instance
    to be available in the frontend as a context dictionary.

    :type name: HttpRequest object
    :param request: contains metadata about the request
    :type name: int
    :param id: field added automatically by django - auto-incrementing primary key
    """
    user_car = get_object_or_404(UserCars, id=id)
    context = {"user_car": user_car}
    return render(request, 'partials/car_detail.html', context)

@login_required
def cars_partial(request):
    """
    This function uses login_required decorator to secure view by forcing the client 
    to authenticate with a valid logged-in User. It will return all UserCars model
    instances for currently logged-in user.

    :type name: HttpRequest object
    :param request: contains metadata about the request
    """
    cars = UserCars.objects.filter(user=request.user)
    return render(request, 'partials/car_list.html', {'cars': cars})

@login_required
def upload_photo(request, id):
    """
    This function uses login_required decorator to secure view by forcing the client 
    to authenticate with a valid logged-in User. It will fetch an existing instance of
    UserCars model given id provided in the frontend. It also obtains from request.FILES
    uploaded image using form attribute enctype="multipart/form-data". After saving UserCars 
    model instance with added image this function will make it available in frontend as a 
    context dictionary record.

    :type name: HttpRequest object
    :param request: contains metadata about the request
    :type name: int
    :param id: field added automatically by django - auto-incrementing primary key
    """
    user_car = get_object_or_404(UserCars, id=id)
    photo = request.FILES.get('photo')
    user_car.car.photo.save(photo.name, photo)
    context = {"user_car": user_car}
    return render(request, 'partials/car_detail.html', context)

def clear(request):
    """
    This function will use empty string as a HttpResponse to make it available for
    swapping content between two divs.

    :type name: HttpRequest object
    :param request: contains metadata about the request
    """
    return HttpResponse("")

def sort(request):
    """
    This function will work with JavaScript Sortable library for reorderable drag-and-drop lists.
    It will ensure that potential changes made to order of UserCars objects in the frontend are 
    also reflected in the backend. This function will take advantage of QuerySet prefetch_related method
    to avoid additional queries when accessing the related objects. It will utilize bulk update method
    to update different rows with different values. In this case we want to update all existing UserCars
    objects with new order values obtained using JS sortable and HTMX.

    :type name: HttpRequest object
    :param request: contains metadata about the request
    """
    cars_ids_order = request.POST.getlist('car_order')
    cars = []
    updated_cars = []
    user_cars = UserCars.objects.prefetch_related('car').filter(user=request.user)
    for index, car_id in enumerate(cars_ids_order, start=1):
        user_car = next(x for x in user_cars if x.id == int(car_id))

        if user_car.order != index:
            user_car.order = index
            updated_cars.append(user_car)
        cars.append(user_car)

        UserCars.objects.bulk_update(updated_cars, ['order'])
    return render(request, 'partials/car_list.html', {'cars': cars})