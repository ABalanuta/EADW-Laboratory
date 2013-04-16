'''
Created on 24 de Fev de 2013

@author: artur-adm
'''

def part(array, low, high):

    i = low    
    for j in range(low + 1, high + 1):
        #print "i=", i, "Array[low]=",array[low], "Pivot=", pivot
        if array[j] < array[low]:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i], array[low] = array[low], array[i]
    return i

def qsort(array, low, high):
    
    if low < high:
            pivot_loc = part(array, low, high)
            qsort(array, low, pivot_loc - 1)
            qsort(array, pivot_loc + 1, high)



#array = [101, 4, 2, 15, 99, 100, 1, 89, 46, 1, 035, 789]
#print array
#qsort(array, 0, len(array)-1)
#print array