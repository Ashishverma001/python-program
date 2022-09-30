
def marks(**data):
    with open ('marks.txt','a') as f:
        for n,m in data.items():
            f.write(f'{n}:{m}\n')

marks(ashish=200, jhon=120)
marks(rob=130, jack=150, ankit= 90, rock=100)
marks()
