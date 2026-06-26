'''def display(num):
    if num>10:
        return
    print(num)
    display(num+1)
display(1)

def display(num):
    if num>10:
        return
    display(num+1)
    print(num)
display(1)
'''


def display(s,ind):
    if ind==len(s):
        return
    print(s[ind])
    display(s,ind+1)
    print(s[ind])
display("python programming",0)
