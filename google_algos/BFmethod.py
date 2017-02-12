# brute force O(n^2)


GRPA = [2,2,3,4,9]
GRPB = [2,3,4,4,9]
GRPC = [2,3,4,9]
TOTAL = 8


def BFmethod(grp, total):

    for i in range(len(grp)):
        compliment = total - grp[i]
        for j in range(len(grp)-i):
            if grp[j] == compliment:
                return True

    return False


print(BFmethod(GRPA,TOTAL))
print(BFmethod(GRPB,TOTAL))
print(BFmethod(GRPC,TOTAL))
