def euclid_alg(num_1,num_2):
    num_a = num_1
    num_b = num_2

    if num_1==0:
        print("invalid, please input numbers that are nonzero")
    else:
        if num_2==0:
            print("invalid, please input numbers that are nonzero")
        else:
            if num_1==num_2:
                print(str(num_1)+" is the greatest common factor between "+str(num_1)+", "+str(num_2)+".")
            else:
                if num_1<num_2:
                    place_holder=num_1
                    num_1=num_2
                    num_2=place_holder
                rem = num_1%num_2
                while rem!=0:
                    num_1 = num_2
                    num_2 = rem
                    rem = num_1%num_2
                print(str(num_2) + " is the greatest common factor between " + str(num_a) + ", " + str(num_b) + ".")
print("Pick the numbers you want the greatest common factor of:")
c=int(input("Number 1: "))
d=int(input("Number 2: "))
euclid_alg(c,d)




