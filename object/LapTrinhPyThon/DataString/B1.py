##vi tri cua chuoi
#s = "abcdef"
#print(s)
#z = s[0]
#print(z)

## dia chi cu the trong bo nho
#s = "abcd"
#print(id(s))

### chr kem theo mot tham so don hoac so nguyen i 
### pham vi hop le cua so nguyen la tu 0 -> 1.114,111

## moi dia chi co mot bo nho id rieng
s = "abcd"
z0 = s[0]
z1 = s[1]
z2 = s[2]
z3 = s[3]
print(id(s))
print(id(z0))
print(id(z1))
print(id(z2))
print(id(z3))


"Toan tu s[n] : lay 1 phan tu tai dia chi so n ra khoi chuoi s"
"Toan tu s[n:m] : lay nhieu phan tu, tu vi tri n -> m, ra khoi chuoi s"
"n bo trong : lay tu dau , m bo trong -> lay den cuoi "

s = "abcdefgh"
z = s[3:]
print(s)
print(z)

s = "abcd"
z = s * 4
print(z)

var = 'Quan tri mang'
print(repr(var))

