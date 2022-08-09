
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        m = n* factorial(n-1)
        return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

    
    
    
