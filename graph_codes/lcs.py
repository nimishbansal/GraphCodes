string1 = "aasdbsahdbashdbsaaabcd"
string2 = "sdbsahdbasdbsahdbash"


def lcs(str1, str2):
    print("checking", str1,str2)
    if len(str1) == 0 or len(str2) == 0:
        return 0
    if str1[0] == str2[0]:
        return 1 + lcs(str1[1:], str2[1:])
    else:
        return max(lcs(str1, str2[1:]), lcs(str1[1:], str2))


print(lcs(string1, string2))
