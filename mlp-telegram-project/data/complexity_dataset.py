"""
complexity_dataset.py
---------------------
Dataset de snippets de código Python etiquetados con su complejidad.
Clases:
  0 → O(1)
  1 → O(log n)
  2 → O(n)
  3 → O(n log n)
  4 → O(n²)
  5 → O(n³)
  6 → O(2^n)
"""

SAMPLES = [

    # ── O(1) ─────────────────────────────────────────────────────────────────
    ("""
def get_first(arr):
    return arr[0]
""", 0),

    ("""
def get_last(arr):
    return arr[-1]
""", 0),

    ("""
def is_empty(arr):
    return len(arr) == 0
""", 0),

    ("""
def add(a, b):
    return a + b
""", 0),

    ("""
def get_value(d, key):
    return d[key]
""", 0),

    ("""
def swap(a, b):
    return b, a
""", 0),

    ("""
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    return c
""", 0),

    ("""
def is_even(n):
    return n % 2 == 0
""", 0),

    ("""
def peek(stack):
    return stack[-1]
""", 0),

    ("""
def hash_lookup(table, key):
    return table.get(key, None)
""", 0),

    # ── O(log n) ──────────────────────────────────────────────────────────────
    ("""
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
""", 1),

    ("""
def find_sqrt(n):
    lo, hi = 0, n
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo - 1
""", 1),

    ("""
def search_rotated(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[lo] <= arr[mid]:
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
""", 1),

    ("""
def count_digits(n):
    count = 0
    while n > 0:
        n = n // 2
        count += 1
    return count
""", 1),

    ("""
def power(base, exp):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    return result
""", 1),

    ("""
def lower_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
""", 1),

    ("""
def upper_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo
""", 1),

    ("""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
""", 1),

    # ── O(n) ──────────────────────────────────────────────────────────────────
    ("""
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
""", 2),

    ("""
def sum_list(arr):
    total = 0
    for x in arr:
        total += x
    return total
""", 2),

    ("""
def find_max(arr):
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val
""", 2),

    ("""
def count_even(arr):
    count = 0
    for x in arr:
        if x % 2 == 0:
            count += 1
    return count
""", 2),

    ("""
def reverse_list(arr):
    result = []
    for i in range(len(arr) - 1, -1, -1):
        result.append(arr[i])
    return result
""", 2),

    ("""
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
""", 2),

    ("""
def sum_recursive(arr, i=0):
    if i == len(arr):
        return 0
    return arr[i] + sum_recursive(arr, i + 1)
""", 2),

    ("""
def copy_list(arr):
    result = []
    for x in arr:
        result.append(x)
    return result
""", 2),

    ("""
def find_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    for x in arr:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    return min_val, max_val
""", 2),

    ("""
def count_occurrences(arr, target):
    count = 0
    for x in arr:
        if x == target:
            count += 1
    return count
""", 2),

    ("""
def flatten_one_level(matrix):
    result = []
    for row in matrix:
        result.append(row[0])
    return result
""", 2),

    # ── O(n log n) ────────────────────────────────────────────────────────────
    ("""
def sort_and_find(arr, k):
    sorted_arr = sorted(arr)
    return sorted_arr[k]
""", 3),

    ("""
def get_median(arr):
    sorted_arr = sorted(arr)
    return sorted_arr[len(arr) // 2]
""", 3),

    ("""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
""", 3),

    ("""
def remove_duplicates_sorted(arr):
    arr.sort()
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            result.append(arr[i])
    return result
""", 3),

    ("""
def sort_and_count_unique(arr):
    arr_sorted = sorted(arr)
    count = 1
    for i in range(1, len(arr_sorted)):
        if arr_sorted[i] != arr_sorted[i-1]:
            count += 1
    return count
""", 3),

    ("""
def kth_largest(arr, k):
    arr.sort(reverse=True)
    return arr[k - 1]
""", 3),

    ("""
def sort_by_frequency(arr):
    from collections import Counter
    freq = Counter(arr)
    return sorted(arr, key=lambda x: -freq[x])
""", 3),

    # ── O(n²) ────────────────────────────────────────────────────────────────
    ("""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
""", 4),

    ("""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
""", 4),

    ("""
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
""", 4),

    ("""
def has_duplicate_pair(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                return True
    return False
""", 4),

    ("""
def matrix_add(A, B):
    n = len(A)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]
    return result
""", 4),

    ("""
def find_all_pairs_sum(arr, target):
    pairs = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs
""", 4),

    ("""
def longest_common_subsequence_len(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
""", 4),

    ("""
def print_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()
""", 4),

    # ── O(n³) ────────────────────────────────────────────────────────────────
    ("""
def matrix_multiply(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
""", 5),

    ("""
def find_triplets(arr, target):
    n = len(arr)
    triplets = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    triplets.append((arr[i], arr[j], arr[k]))
    return triplets
""", 5),

    ("""
def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
""", 5),

    ("""
def count_triplets_less_than(arr, target):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[i] + arr[j] + arr[k] < target:
                    count += 1
    return count
""", 5),

    # ── O(2^n) ────────────────────────────────────────────────────────────────
    ("""
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
""", 6),

    ("""
def count_subsets(arr, target, i=0):
    if i == len(arr):
        return 1 if target == 0 else 0
    return (
        count_subsets(arr, target - arr[i], i+1)
        + count_subsets(arr, target, i+1)
    )
""", 6),

    ("""
def generate_subsets(arr):
    if not arr:
        return [[]]
    rest = generate_subsets(arr[1:])
    return rest + [[arr[0]] + s for s in rest]
""", 6),

    ("""
def hanoi(n, source, target, aux):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, aux, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, aux, target, source)
""", 6),

    ("""
def all_paths(grid, i=0, j=0):
    if i == len(grid)-1 and j == len(grid[0])-1:
        return 1
    paths = 0
    if i + 1 < len(grid):
        paths += all_paths(grid, i+1, j)
    if j + 1 < len(grid[0]):
        paths += all_paths(grid, i, j+1)
    return paths
""", 6),

    ("""
def knapsack(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    if weights[n-1] > capacity:
        return knapsack(weights, values, capacity, n-1)
    return max(
        values[n-1] + knapsack(weights, values, capacity - weights[n-1], n-1),
        knapsack(weights, values, capacity, n-1)
    )
""", 6),
]

CLASS_NAMES = {
    0: "O(1)",
    1: "O(log n)",
    2: "O(n)",
    3: "O(n log n)",
    4: "O(n²)",
    5: "O(n³)",
    6: "O(2^n)",
}

if __name__ == "__main__":
    from collections import Counter
    labels = [label for _, label in SAMPLES]
    dist = Counter(labels)
    print(f"Total samples: {len(SAMPLES)}")
    for cls, name in CLASS_NAMES.items():
        print(f"  {name}: {dist[cls]} samples")