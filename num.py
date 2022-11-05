num = [1, 7, 7]

bol = False
if num[len(num) - 1] == 7 and num[len(num) - 2] == 7:
    bol = True
else:
    for i in range(len(num) - 2):
        if num[i] == 7 and num[i + 1] == 7 or num[i] == 7 and num[i + 2] == 7:
            bol = True
print(bol)