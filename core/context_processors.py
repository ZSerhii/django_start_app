from random import shuffle  # , choice
from django.conf import settings

def students_names(request):
    students = ['Serhii', 'Andrii', 'Bohdan', 'Ira', 'Alex', 'Roman']

    shuffle(students)

    # used_dict = {index: 1 for index in range(len(students))}

    # random_list = []

    # while len(random_list) < len(students):
    #     elem = choice(students)

    #     index = students.index(elem)

    #     if used_dict[index]:
    #         random_list.append(elem)
    #         used_dict[index] = 0

    return {'students': students}


def base_url(request):
    return {'base_url': settings.BASE_URL}
