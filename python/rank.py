import string

def rank(st, we, n):
    names = st.split(",")
    result_names = {}
    alpha = list(string.ascii_lowercase)
    l = len(names)

    if l <= 1 : return "No participants"
    if n > l:
        return "Not enough participants"
    for i in range(l):
        weight = we[i]
        val = 0
        for c in names[i].lower():
            val += alpha.index(c)+1
        result_names[names[i]] = weight*val

    return sorted(result_names.items(),key=lambda x:x[1],reverse=True).pop(n-1)[0]

assert rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4), "Benjamin"
assert rank("Lagon,Lily", [1, 5], 2), "Lagon"
assert rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8), "Not enough participants"
assert rank("", [4, 2, 1, 4, 3, 1, 2], 6), "No participantss"

