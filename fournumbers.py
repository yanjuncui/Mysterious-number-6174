# https://plus.maths.org/content/mysterious-number-6174
# Kaprekar's operation.
# There are four unit digit numbers (from 0 to 9), which can not be all the same, not 1111, 2222....
# Then rearrange the digits to get the largest and smallest numbers these digits can make.
# Finally, subtract the smallest number from the largest to get a new number,
# and carry on repeating the operation for each new number.
# When we reach 6174 the operation repeats itself, returning 6174 every time.


# Solution:
# Assuming A, B, C, D are random selected digits satisfy requirements before.
# They satisfy A >= B >= C >= D

# (1000A + 100B + 10C + D) - (1000C + 100B + 10A + D) = 999(A - D) + 90(B - C)
# Therefore, after subtraction, all three digits numbers can be represent as 999(A - D) + 90(B - C).
# The range of B and C is less than the range of A and D


lst = [1,2,3,4,5,6,7,8,9]
lst2 = [[0,1],[0,1,2],[0,1,2,3],[0,1,2,3,4],[0,1,2,3,4,5],[0,1,2,3,4,5,6],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8,9]]
four1 = [0]*4
four2 = [1]*4
res = []
for i in range(0, 9):
    for j in range(0,lst[i]+1):
            x = lst[i] * 999 + lst2[i][j] * 90
            res.append(x)
print("There are total of these different combinations after first iteration:")
print(res)
# all different numbers
print("\n")

print("Here is the iteration results of every process: ")
res2 = [1]*10+[-1]*44
while len(set(res2))!=1:
    i = 0
    for i in range(0, len(res)):
        four1[0] = res[i]//1000
        four1[1] = (res[i] - four1[0] * 1000)//100
        four1[2] = (res[i] - four1[0] * 1000 - four1[1] * 100)//10
        four1[3] = res[i] % 10
        four1.sort(reverse = True)
        four1_str = "".join(str(x) for x in four1)
        #print(four1_str)
        res2[i]=four1_str
        #print(res2)
        y = 999*(four1[0]-four1[3])+90*(four1[1]-four1[2])
        res[i] = y
        four2[0] = y//1000
        four2[1] = (y - four2[0] * 1000)//100
        four2[2] = (y - four2[0] * 1000 - four2[1] * 100)//10
        four2[3] = y % 10
        four2.sort(reverse = True)
        four2_str = "".join(str(x) for x in four2)
        res2[i] = four2_str
        #print(res2)
    print(res)
