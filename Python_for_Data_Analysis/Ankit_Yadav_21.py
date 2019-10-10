def count_chars():
    sentence = input(" Input Sentence: ")
    d = {}
    sentence = sentence.replace(" ","")
    for i in sentence[:]:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    print(d)


def my_sort_key(mydict, arr): #Performs Selection Sort on keys and maps sorted keys to original dictionary
    for key in mydict.keys():
        arr.append(key)
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
                arr[j+1] = key 
    n = {}  #New dictionary which stores sorted keys mapped with original dictionary
    for i in arr[:]:
        for k,v in mydict.items():
            if i == k:
                n[k] = v
    print(n)

def my_sort_value(mydict, arr): #Performs Selection Sort on values and maps sorted values to original dictionary
    for value in mydict.values():
        arr.append(value)
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
                arr[j+1] = key 
    n = {}   #New dictionary which stores sorted values mapped with original dictionary
    for i in arr[:]:
        for k,v in mydict.items():
            if i == v:
                n[k] = v
    print(n)

    
def dict_sort(mydict):
    option = input("please select operation: (1: sort by key, 2: sort by value")
    d = mydict
    arr = []
    if option == '1':
        my_sort_key(d, arr)
    elif option == '2':
        my_sort_value(d, arr)
    else:
        print("Please select either 1 or 2")