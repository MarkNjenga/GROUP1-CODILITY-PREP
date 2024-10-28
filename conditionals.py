#Program to check if the array is sorted or not
def arraySortedOrNot(arr, n):
    #check if the array has one or no element
    if (n == 0 or n == 1):
        return True
    
    for i in range(1, n):
        #check if unsorted pair is found
        if (arr[i -1] > arr[i]):
            return False
    #if no unsorted pair
    return True  
arr = [30,30,45,63,78,92]
n = len(arr)  

#function that returns Yes if an array is sorted and No if it is not sorted
if (arraySortedOrNot(arr, n)):
    print('Yes')
else:
    print('No')     
    


###### Check if a string is a substring of another
def findSubstring(txt, pat):
    n = len(txt)
    m = len(pat)
    
    #itterate through txt
    for i in range(n - m + 1):
        #check substring match
        j = 0
        while j < m and txt[i + j] == pat[j]:
            j += 1
        #if there is a match
        if j == m:
            return i
    #if no match is found
    return -1
#check if pat is a substring of txt
if __name__ == "__main__":
    txt = "Canan"
    pat = "an"
    print(findSubstring(txt,pat))              
