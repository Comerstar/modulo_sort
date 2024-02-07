
def modulo_sort(lst):
    i = 2
    result = lst
    while True:
        temp = result
        count = [0] * i
        placed = [0] * i
        for j in temp:
            count[j % i] += 1
            placed[j % i] += 1
        for j in range(i - 1):
            count[j + 1] += count[j]
        result = [0] * len(temp)
        for j in range(len(temp)):
            result[count[temp[j] % i] - placed[temp[j] % i]] = temp[j]
            placed[temp[j] % i] -= 1
        sorted = True
        for j in range(len(result) - 1):
            if (result[j] > result[j + 1]):
                sorted = False
                break
        if sorted:
            return result
        i += 1
    
test = []
print("Input the integers of your list, then a non-integer.")
user_in = input()
try:
    while True:
        test.append(int(user_in))
        print("Inputted ", test)
        user_in = input()

except Exception:
    print(test)
    print(modulo_sort(test))    
