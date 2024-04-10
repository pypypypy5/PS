N, K = map(int, input().split())

li = list(map(int, input().split()))

def merge(arr):
    if len(arr) > 1:

        left = arr[0:len(arr)//2]
        right = arr[len(arr)//2:]

        merge(left)
        merge(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(left):
            arr[k] = right[j]
            j += 1
            k += 1

    else:
        pass

merge(li)

print(li[-K])