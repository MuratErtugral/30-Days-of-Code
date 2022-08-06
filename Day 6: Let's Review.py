
T = int(input())

while T > 0:
    S = input()
    even=""
    odd =""
    for m in range(len(S)):
        if m % 2 == 0:
            even += S[m]
        else:
            odd += S[m]
    print(even,odd)
    T -=1
