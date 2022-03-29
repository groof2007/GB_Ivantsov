def tutors_klasses_gen(tutors: list, klasses: list):
    return ((tutors[i], klasses[i]) if i < len(klasses) else (tutors[i], None) for i in range(len(tutors)))


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

school_gen = (tutors_klasses_gen(tutors, klasses))
print(type(school_gen))

for _ in range(len(tutors)):
    print(next(school_gen))