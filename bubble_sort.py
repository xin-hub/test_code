"""Bubble sort implementation in Python."""


def bubble_sort(values):
    """Return a new list sorted in ascending order using bubble sort."""
    items = list(values)
    n = len(items)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]
    print(bubble_sort(sample))
