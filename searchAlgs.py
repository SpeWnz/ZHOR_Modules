
# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints
else:
    from . import nicePrints

# =============================================================================

# Riceca binaria iterativa - Trova LA PRIMA OCCORRENZA in caso di ripetizioni
def binarySearchIterativa(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if array[mid - 1] != target:
                return mid
            high = mid - 1