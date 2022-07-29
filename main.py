def reciprocal_sum(a: int, b: int) -> float:
    sum = 0
    for i in range(a, b+1):
        sum += 1/i
    return sum


if __name__ == '__main__':
    n = 1000  # number of prisoners, boxes, and slips
    print(reciprocal_sum(1,10000000))
