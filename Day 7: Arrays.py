
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
arr = reversed(arr)
for m in arr:
    print(m ,end=" ")
