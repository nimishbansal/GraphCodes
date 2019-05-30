P = "aacbdbc"
T = "abcddbcbdcaaaccbdbaacbcddaacbdbcaabbcd"
shifts = []
m = len(P)
n = len(T)
for i in range(n - m + 1):
    print(T[i:i + m], T[i:i + m] == P)
    if T[i:i + m] == P:
        shifts.append(i)

print(shifts)