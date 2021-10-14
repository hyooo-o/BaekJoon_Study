def solution(people, limit):
    count = 0
    people.sort()
    i = 0
    j = len(people) - 1
    while i <= j :
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            count += 1
    return count

people = [70, 80, 50, 50]
limit = 100

print(solution(people, limit))