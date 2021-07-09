a = (int(i) for i in input().split())
def sum(list):
    f=1
    for i in a:
        f=f*i
    return f    
print(sum(a))