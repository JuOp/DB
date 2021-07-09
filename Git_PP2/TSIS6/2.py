a = (int(i) for i in input().split())
def sum(list):
    f=0
    for i in a:
        f=f+i
    return f    
print(sum(a))