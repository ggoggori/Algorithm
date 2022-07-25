inputs = "AJKDLSI412K4JSJ9D"

strings = []
digits = []
for i in inputs:
    if i.isalpha():
        strings.append(i)
    else:
        digits.append(int(i))

result = sorted(strings)
result.append(str(sum(digits)))

print("".join(result))

