def set_dict(x):
    abbr = ['kr', 'us', 'jp', 'de', 'sk', 'hu', 'no']
    name = ['대한민국', '미국', '일본', '독일', '슬로바키아', '헝가리', '노르웨이']
    for index, i in enumerate(abbr):
        x[i] = name[index]


def get_dict(x):
    for i in x.keys():
        print(f'{i} : \t{x[i]}')


domain = {}
set_dict(domain)
get_dict(domain)
