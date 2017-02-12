#linear

GRPA = [2,2,3,4,9]
GRPB = [2,3,4,4,9]
GRPC = [2,3,4,9]
TOTAL = 8

def pointSearch(grp, total):
    back = 0
    front = len(grp)-1

    while back < front:
        addition = grp[back] + grp[front]
        if addition == total:
            return True
        elif addition < total:
            back+=1
        elif addition > total:
            front-=1

        else:
            print("AAAA")

    return False

print(pointSearch(GRPA, TOTAL))
print()
print(pointSearch(GRPB, TOTAL))
print()
print(pointSearch(GRPC, TOTAL))
print()
