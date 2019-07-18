'''______RUNNER UP SCORE_____'''
if __name__ == "__main__":
    n = input()
    arr = map(int, n.split())
    arr = list(set(list(arr)))
    ar = len(arr)
    arr = sorted(arr)
    print(arr[arr-2])