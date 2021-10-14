def solution(number, k):
    arr = []
    
    for (i, n) in enumerate(number):
        while arr and k > 0 and n > arr[-1]:
            arr.pop()
            k -= 1
        
        arr.append(n)
        
        if k == 0:
            arr.append(number[i+1:])
            break
            
    if k > 0 :
        arr = arr[:-k]

    answer = ''.join(arr)
    return answer