T = int(input())
for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))
    result_list = []
    for i in range(len(numbers)):
        if numbers[i-1]%2 == 1:
            result_list.append(numbers[i-1])
            result=sum(result_list)

    print(f"#{test_case} {result}")