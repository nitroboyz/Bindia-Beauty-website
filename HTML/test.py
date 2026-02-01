
from random import randint

#the following variable will be used in the rest of the exercise
pm = 'justin pierre james trudeau'
instructor = 'narendra pershad'
harry = "You've gotta ask yourself a question: do I feel lucky? …well, do ya, punk?"
numbers = [randint(5, 10) for _ in range(20)]
d = {
    3462: 'Artificial Intelligence',
    3468: 'Software Engineering Technician',
    3469: 'Software Engineering Technology',
    3472: 'Artificial Intelligence (FT)',
    3478: 'Software Engineering Technician (FT)',
    3528: 'Health Informatics Technology (FT)',
    3609: 'Game - Programming',
    3668: 'Health Informatics Technology',
    3679: 'Game - Programming (FT)'}
print(d.get(3462))