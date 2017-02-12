SUM = 28
ARRAY = [1,2,3,6,21,9]

def memCheck(ARRAY,SUM):
    iterations = 0
    numbers = {}
    for integer in ARRAY: #key is the number, value is the number of occurances
        if integer in numbers:
            numbers[integer] = numbers[integer]+1
        else:
            numbers[integer] = 1

    for i in ARRAY:
        remainder  = SUM - i
        if remainder in numbers:
            if i == remainder and numbers[remainder] > 1:
                return True, iterations
            return True ,iterations
        iterations += 1
    return False, iterations


print(memCheck(ARRAY,SUM))
