if __name__ == '__main__':
    a = [7,1,5,6,4,3,9]
    print(a)
    def insertionSort(a):
        for i in range(1, len(a)):
            j = i - 1 
            current = a[i]
            while j >= 0 and a[j] > current:
                a[j+1] = a[j]
                j -= 1 
            a[j+1] = current
        return a
    a = insertionSort(a)
    print(a)