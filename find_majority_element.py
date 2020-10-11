#Aproach 2 - O(n) .. 1. consider 1st ele as majority ele, and counter = 1
#2. compared 1st ele to next ele..  if it is not equal then counter--. 
#if counter==0 then set counter=1 and majority = current val 
#3. if equal then counter++
#4. if we have majority element counter > 0 and majority variable has majority element

def find_majority_element(arr):
    maj = arr[0]
    count = 1

    for i in range(1,len(arr)):
        if(maj == arr[i]):
            count +=1
        else:
            count -=1
            if(count == 0):
                count = 1
                maj = arr[i]
    
    print("majority", maj, count)

if __name__ == "__main__":
    A = [1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2]
    A = [2,2,3,4,5]
    find_majority_element(A)