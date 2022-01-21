def is_sorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True


def bubble_sort_rec(lst, right, step=1):
    for i in range(right):
        if is_sorted(lst[i:right+1]):
            right = i
            break
    for i in range(0, right):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]

    if not is_sorted(lst):
      
        return bubble_sort_rec(lst, right - 1, step + 1)
    else:

        print(f"{lst}")

if __name__ == '__main__':
    lst = list(map(int, input("Enter Input : ").split()))
    bubble_sort_rec(lst, len(lst)-1)