courses = {'count': 2,
           'title': 'Django Basics',
           'prereqs': [{'count': 3,
                     'title': 'Object-Oriented Python',
                     'prereqs': [{'count': 1,
                               'title': 'Python Collections',
                               'prereqs': [{'count':0,
                                         'title': 'Python Basics',
                                         'prereqs': []}]},
                              {'count': 0,
                               'title': 'Python Basics',
                               'prereqs': []},
                              {'count': 0,
                               'title': 'Setting Up a Local Python Environment',
                               'prereqs': []}]},
                     {'count': 0,
                      'title': 'Flask Basics',
                      'prereqs': []}]}

def prereqs(data, pres=None):
    # if pres is empty return set()
    pres = pres or set()

    if data['count'] == 0:
      return None
    else:
      for item in data['prereqs']:
        pres.add(item['title'])
        prereqs(item['prereqs'],pres)

prereqs(courses)



