
print("type()도 함수인가? 그렇다")

a = 30
b = "30"

c = type(a)
d = type(b)
print(c)
print(d)

print("여기서부터는 난이도가 상승한다")

e = type(c)
print(e)

print(type(type(type(e))))
