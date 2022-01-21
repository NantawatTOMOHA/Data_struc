g_cComparisons = 0

def InsertionSort(ls):
    def _InsertionSort(idx):
        global g_cComparisons
        
        if idx < len(ls) and idx > 0:
            elem = ls[idx]
            pos = idx
            
            while pos > 0:
                g_cComparisons += 1
                if ls[pos - 1] <= ls[pos]:
                    break
                ls[pos - 1], ls[pos] = ls[pos], ls[pos - 1]
                pos -= 1
            
            _InsertionSort(idx + 1)
    
    _InsertionSort(1)

print(" *** Insertion sort ***")
inp = [int(n) for n in input("Enter some numbers : ").split()]
print()
InsertionSort(inp)
print((inp))
print('Data comparison =  '+ str(g_cComparisons))