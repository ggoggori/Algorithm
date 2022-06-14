n = int(input())
string = list(input())
temp = []
for _ in range(n-1):
    relative = input()
    for i in range(len(string)):
        if string[i] != relative[i]:
            string[i] = '?'
print(''.join(string))    