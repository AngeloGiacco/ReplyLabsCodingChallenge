#length password is N
#forbidden sequence is M
#number of test Cases is T
import itertools
def allCharactersSame(s) :
    n = len(s)
    for i in range(1, n) :
        if s[i] != s[0] :
            return False

    return True

def clean(arr):
    arr = [int(num) for num in arr if num == '1' or num == '0']
    return(tuple(arr))

i = 0
safeArray = []
possibilitiesArray = []
with open("input.txt","r") as file:
    with open("output.txt","w") as output_file:
        for line in file:
            if i == 4:
                print(line)
            if i == 0:
                T = line[0]
            elif (i % 2) == 1:
                #load N from input file
                length_password = map(int, line.split())[0]
                #load M from input file
                length_forbidden = map(int,line.split())[1]
                delta = length_password - length_forbidden
                if length_forbidden > length_password:
                    safe = 2 ** length_password
                    safeArray.append(safe)
                elif length_forbidden == length_password:
                    safe = 2 ** length_password - 1
                    safeArray.append(safe)
                elif length_forbidden == 1:
                    safe = 1
                    safeArray.append(safe)
                else:
                    lst = list(itertools.product([0, 1], repeat=length_password))
                    possibilitiesArray.append(lst)
            else:
                tup = clean(list(line))
                print(tup)
                for password in lst:
                    if tup in password:
                        possibilitiesArray.remove(password)
                safeArray.append(len(possibilitiesArray))
            print(safeArray,i)
            i += 1
cases = length(safeArray)
for i in range(len(safeArray)):
    output_file.write("Case #"+str(cases)+":"+str(safeArray[i]))
