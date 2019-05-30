# P = "aacbdbc"
# T = "abcddbcbdcaaaccbdbaacbcddaacbdbcaabbcd"
P = "abcd"
T = "cadabcdefghij"
q = (10 ** 9) + 7


def get_replaced(string):
    arr = []
    for i in string:
        # arr.apend(ord(i))
        arr.append(ord(i)-96)
    return arr


P = get_replaced(P)
T = get_replaced(T)

d = len(set(T))
# shifts = []
m = len(P)
n = len(T)
h = (d ** (m - 1)) % q  # vo 10**(m-1)
p = 0
t = (n-m+1) * [None]
t[0] = 0
for i in range(0, m):
    p = (d * p + P[i]) % q
    t[0] = (d * t[0] + T[i]) % q

print("p is", p)
print("t[0] is", t[0])

for s in range(0, n - m + 1):
    if p == t[s]:
        if P[0:m] == T[s:s + m]:
            print("Pattern with shift ", s)

    if s < n - m:
        t[s + 1] = (d * (t[s] - T[s] * h) + T[s + m]) % q  # vo minus karne ke baad 10 se multiply karke naya add karna
