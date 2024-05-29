"""
7kyu
Mumbling

This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""

def accum(st):

    st_low = st.lower()
    list_st = []
    count = 0
    for i in st_low:
        list_st.append(i.upper() + i * count)
        count += 1
    res_str = "-".join(list_st)

    return res_str

"""
Optimal

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
"""
