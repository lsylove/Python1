
print("순차형 언어의 실행흐름")
print()


def exclaim():
    print("소리치기!")


def subtract_spoiler(a, b):
    print(a, "에서", b, "빼기")

    c = a - b
    exclaim()
    print("뺐더니", c, "임")
    exclaim()

    return c


exclaim()
exclaim()
a = 30
b = 40
c = subtract_spoiler(a, b)
exclaim()
d = subtract_spoiler(b, c)
print(c)
print(d)
