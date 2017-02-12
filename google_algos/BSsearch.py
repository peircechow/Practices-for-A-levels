#slightly more efficient O(nlogn)

GRPA = [2,2,3,4,9]
GRPB = [2,3,4,4,9]
GRPC = [2,3,4,9]
TOTAL = 8


#take first element, then binary search for it's compliment

def BSsearch(grp, total):
    for i in range(len(grp)):
        element = grp[i]
        compliment = total - element
        compGrp = grp[i+1:]
        
        low = 0
        high = len(compGrp)-1
        while low <= high:
            middle = (low+ high) //2
            if compliment == compGrp[middle]:
                return True
            elif compliment < compGrp[middle]: #need to go lower
                high = middle -1
                print("Lower")
            elif compliment > compGrp[middle]: #need to go higher
                low = middle+1
                print("Higher")
            else:
                print("AAAA")

    return False

print(BSsearch(GRPA,TOTAL))
print()
print(BSsearch(GRPB,TOTAL))
print()
print(BSsearch(GRPC,TOTAL))

