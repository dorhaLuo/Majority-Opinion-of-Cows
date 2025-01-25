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
T = int(input())
N = []
hay = []

for i in range(T):
    # number of cows
    N.append(int(input()))
    # what each of the cows like. List inside list
    hay.append(input().split())
    

for i in range(T):
    print(test_case(N[i], hay[i]))
