

# return: int
def get_var():
    X = input()
    while not X.isdigit():
        X = input()
    return int(X)



# param: int, list of int
def test_case(N, list):
    results = []
    

    for i in range(1,N):
        
        if list[i] not in results:
            if list[i] == list[i-1]:
                results.append(list[i])
            elif i != 1 and list[i] == list[i-2]:
                results.append(list[i])












    if len(results) == 0:
        results.append("-1")


    results.sort()
    return " ".join(results)




'''Call the program'''

# number of test cases
T = get_var()

for i in range(T):
    # number of cows
    N = get_var()
    # what each of the cows like. List
    # (1 ≤ h_i ≤ N)
    hay = input().split()
    

    print(test_case(N, hay))
