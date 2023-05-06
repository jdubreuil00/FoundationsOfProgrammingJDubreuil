import time
import random
import bubbleSort
import shellSort
import insertionSort
import interpolSearch
import linearSearch
import mergeSort
import selectionSort

# Number of items to be entered in the list.
numofitems = 40000

# Uses the random sample function to generate unique numbers for each entry in the list.
largelistofnum = random.sample(range(numofitems+1),numofitems)
largelistofnumcopy = largelistofnum

# prints items in the list
# print(largelistofnum)

# Stamps time ahead of sorting funciton call
dts = time.time()

"""
I commented/uncommented each algorithm for the tests.
Wanted to run each on a seperate tread simultaneously 
but needed to get to work on the final. I will try to do
this at another time.
"""
bubbleSort.bubblesort(largelistofnum)
# Time stamp after the sorting function is complete
dte = time.time()
dts2 = time.time()
shellSort.shellSort(largelistofnumcopy)
# Time stamp after the sorting function is complete
dte2 = time.time()
# insertionSort.insertion_sort(largelistofnum)
# mergeSort.merge_sort(largelistofnum)
# selectionSort.selection_sort(largelistofnum)
# interpolSearch.intpolsearch(largelistofnum)
# linearSearch.linear_search(largelistofnum)


# Prints the number of items in the list.
print(len(largelistofnum))
# Gets the difference in seconds to determine how long it took the sort to complete.
elapsedtimebubble = dte - dts
elapsedtimeshell = dte2 - dts2
# Converts the time to milliseconds.
elapsedtimebubble *= 1000
elapsedtimeshell *= 1000
# Prints the ellapsed time in milliseconds.
print(f'Elapsed time {elapsedtimebubble:.4f} for bubble sort')
print(f'Elapsed time {elapsedtimeshell:.4f} for shell sort')