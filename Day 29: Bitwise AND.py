
def bitwiseAnd(N,K):
    # Write your code here
    maximum = 0
    for i in range(1,N+1):
        for j in range(1,i):
            h = i & j
            if maximum < h < K:
                maximum = h
            if maximum == K-1:
                return maximum
    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
