from django.shortcuts import render

# make a list that represents different virtual rooms
rooms = [
    {'id': 1, 'name': "Let's learn python"},
    {'id': 2, 'name': "Quality Assurance"},
    {'id': 3, 'name': "Frontend Development"},
]
# I want to render this data inside of the templates
# in order to pass this on so I can access the data from the variable
# rooms, I have to pass another argument in the functions below:
# in the render functions I can pass a 3rd argument, a dictionary containing
# as many key: value pairs as I need to access in my templates
# in this case it will be {'rooms': rooms}

# Create your views here.
# def home(request):
#     # the request object is gonna be the http object this is gonna tell me
#     # what kind of request method is sent, what kind of data is sent in,
#     # what is the user sending to the backend
#     return HttpResponse("Home, sweet home")

# gonna get rid of the HttpResponse and user the render method imported above
def home(request):
    # the render method takes 2 parameters that are needed and 1 optional
    # request -> http request that i pass into the function, this is how
    # i pass data back and forth
    # 'room.html' -> specify the template name
    return render(request, 'base/home.html', {'rooms': rooms})

# def room(request):
#     return HttpResponse("Room here!")
def room(request, pk):
    # I wanna access the values from each room in the template(dynamic routing)
    room = None
    # iterate over the rooms list
    for i in rooms:
        # if the room's id matches the pk(primary key), assign that value
        # to the room variable(make sure the pk argument is an integer)
        if i['id'] == int(pk):
            room = i
        # create a variable that will store the key: value pair dict that
        # will be accessed from the template
        context = {'room': room}

    return render(request, 'base/room.html', context)