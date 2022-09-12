from django import template


reg = template.Library()

@reg.tag
def url1(name, *args):
    return f'{name}/1{args}'


class A:
    c = 1
    def b(self):
        print(self.c)

l = A()

l.b()
