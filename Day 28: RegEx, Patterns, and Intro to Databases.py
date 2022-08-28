
if __name__ == '__main__':
    N = int(input().strip())
    g = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        if "@gmail.com" in emailID:
            g.append(firstName)
        
g = sorted(g)
for m in g:
    print (m)
    
    
    
    
