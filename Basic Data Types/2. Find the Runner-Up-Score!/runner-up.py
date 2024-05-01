if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    unique_list = set(arr)
    sorted_list = sorted(unique_list, reverse=True)
    
    print(str(sorted_list[1]))
    
