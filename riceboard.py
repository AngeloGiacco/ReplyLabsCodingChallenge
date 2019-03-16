import math
i = 0
with open("input.txt", "r") as file:
    with open("output.txt", "w") as output_file:
        for line in file:
            total = 0
            i = i + 1
            if i == 1:
                test_cases = int(line)
            else:
                splitup = line.split(" ")
                R = int(splitup[0])
                N = int(splitup[1])
                M = int(splitup[2])
                #print("R is "+str(R))
                #print("N is "+str(N))
                #print("M is "+str(M))

                #print("-----------")
                for e in range(0, N**2):
                    total = total + R**e

                print(total)


                    #print("Square "+str(e)+" is "+str(R**e))
                #print("-----------")
                #print(total)

                total_waste = total%int(M)
                #print(total_waste)

                #outputting
                output_file.write("Case #"+str(i-1)+": "+str(total_waste)+"\n")
