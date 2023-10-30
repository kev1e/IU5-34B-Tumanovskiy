""""
Вариант Г:
17 Вариант (Дирижёр, Оркестр)
"""

from operator import itemgetter

class Сonductor:

    def __init__(self, id, name, date, cond_id):
        self.id = id
        self.name = name
        self.date = date
        self.cond_id = cond_id


class Orchestra:

    def __init__(self, id, name):
        self.id = id
        self.name = name


class СonductorInOrchestra:

    def __init__(self, cond_id, emp_id):
        self.cond_id = cond_id
        self.conductor_id = emp_id


# Компьютеры
orchestras = [
    Orchestra(1, 'Atlanta Symphony Orchestra'),
    Orchestra(2, 'National Symphony Orchestra'),
    Orchestra(3, 'New York Philharmonic'),

    Orchestra(11, 'Boston Symphony Orchestra'),
    Orchestra(22, 'Philadelphia Orchestra'),
    Orchestra(33, 'Cleveland Orchestra'),
]

# Микропроцессоры
conductors = [
    Сonductor(1, 'Topher Lyndon' , 1965, 1),
    Сonductor(2, 'Colton Parry',  1982, 2),
    Сonductor(3, 'Felix Damion',  1973, 3),
    Сonductor(4, 'Cam Raymond',  1988, 3),
    Сonductor(5, 'Armen Mackenzie',  1999, 3),
]

cio = [
    СonductorInOrchestra(1, 1),
    СonductorInOrchestra(2, 2),
    СonductorInOrchestra(3, 3),
    СonductorInOrchestra(3, 4),
    СonductorInOrchestra(3, 5),

    СonductorInOrchestra(11, 1),
    СonductorInOrchestra(22, 2),
    СonductorInOrchestra(33, 3),
    СonductorInOrchestra(33, 4),
    СonductorInOrchestra(33, 5),
]


def main():
    # Соединение данных один-ко-многим
    one_to_many_fq = [(comp.name, conductor.name, conductor.date)
                      for comp in orchestras
                      for conductor in conductors
                      if comp.id == conductor.cond_id]
    # Соединение данных один-ко-многим
    one_to_many_curr = [(comp.name, dia.cond_id, dia.conductor_id)
                      for comp in orchestras
                      for dia in cio
                      if comp.id == dia.cond_id]

    many_to_many_ans = [(comp_name, d.name)
                    for comp_name, comp_id, conductor_id in one_to_many_curr
                    for d in conductors if d.id == conductor_id]

    print("#####Task-№1#####")
    sorted(one_to_many_fq, key=itemgetter(0))
    i = 0
    j = 0
    while i < len(one_to_many_fq) and one_to_many_fq[i][0].startswith('A'):
        if i == j:
            print(one_to_many_fq[j][0])
        while j < len(one_to_many_fq) and one_to_many_fq[j][0] == one_to_many_fq[i][0]:
            print(one_to_many_fq[j][1] + ' ' + str(one_to_many_fq[j][2]))
            j += 1
        i = j

    print("#####Task-№2#####")
    sorted(one_to_many_fq, key=itemgetter(0,2))
    i = 0
    j = 0
    parks_maximus = []
    while i < len(one_to_many_fq):
        curr = 0
        while j < len(one_to_many_fq) and one_to_many_fq[j][0] == one_to_many_fq[i][0]:
            if one_to_many_fq[j][2] > curr:
                curr = one_to_many_fq[j][2]
            j += 1
        parks_maximus.append((one_to_many_fq[i][0], curr))
        i = j
    for e in parks_maximus:
        print(e)
    print("#####Task-№3#####")
    sorted(many_to_many_ans, key=itemgetter(0, 1))
    i = 0
    j = 0
    while i < len(many_to_many_ans) and j < len(many_to_many_ans):
        print(many_to_many_ans[i][0])
        while j < len(many_to_many_ans) and many_to_many_ans[j][0] == many_to_many_ans[i][0]:
            print('\t' + str(many_to_many_ans[j][1]))
            j += 1
        i = j
if __name__ == '__main__':
    main()

