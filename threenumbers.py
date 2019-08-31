
# A >= B >= C
# A, B, C are random selected digits satisfy requirements before.

# (100A + 10B + C) - (100C + 10B + A) = 99(A - C)
# Therefore, after subtraction, all three digits numbers can be represent as 99(A - C).

#  When we reach  495, the operation repeats itself, returning 495 every time.

count = 1
lst = [1,2,3,4,5,6,7,8,9]
while len(set(lst))!=1:
    i = 0
    count = count + 1
    for i in range(0, 9):
        x = lst[i] * 99
        hund = x//100
        tens = x//10%10
        unit = x%10
        if hund <tens:
            hund, tens = tens, hund
        if tens < unit:
            tens, unit = unit, tens
        y = 99*(hund-unit)
        hund = y // 100
        tens = y // 10 % 10
        unit = y % 10
        if hund < tens:
            hund, tens = tens, hund
        if tens < unit:
            tens, unit = unit, tens
        j = hund - unit
        lst[i] = j
    print(lst)
print("There at most are total of " + str(count) + "  dealing needed to obtain final number: " + str(lst[0]*99))

