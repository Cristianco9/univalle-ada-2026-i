"""
complexity_dataset.py
---------------------
Dataset expandido: ~150 snippets etiquetados con su complejidad.
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

    # ── O(1) ── 22 samples ───────────────────────────────────────────────────
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
    ("""
def stack_push(stack, val):
    stack.append(val)
    return stack
""", 0),
    ("""
def dict_set(d, key, val):
    d[key] = val
""", 0),
    ("""
def absolute(n):
    return n if n >= 0 else -n
""", 0),
    ("""
def multiply(a, b):
    return a * b
""", 0),
    ("""
def get_middle(arr):
    return arr[len(arr) // 2]
""", 0),
    ("""
def toggle(flag):
    return not flag
""", 0),
    ("""
def clamp(val, lo, hi):
    if val < lo:
        return lo
    if val > hi:
        return hi
    return val
""", 0),
    ("""
def head(lst):
    return lst[0] if lst else None
""", 0),
    ("""
def tail(lst):
    return lst[-1] if lst else None
""", 0),
    ("""
def increment(n):
    return n + 1
""", 0),
    ("""
def negate(n):
    return -n
""", 0),
    ("""
def is_positive(n):
    return n > 0
""", 0),

    # ── O(log n) ── 20 samples ────────────────────────────────────────────────
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
    ("""
def find_peak(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo
""", 1),
    ("""
def log_steps(n):
    steps = 0
    while n > 1:
        n = n // 2
        steps += 1
    return steps
""", 1),
    ("""
def first_bad_version(n, is_bad):
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        if is_bad(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
""", 1),
    ("""
def search_matrix(matrix, target):
    lo, hi = 0, len(matrix) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
""", 1),
    ("""
def count_half(n):
    result = 0
    while n > 1:
        n //= 2
        result += 1
    return result
""", 1),
    ("""
def binary_search_leftmost(arr, target):
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
def interpolation_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
""", 1),
    ("""
def find_min_rotated(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > arr[hi]:
            lo = mid + 1
        else:
            hi = mid
    return arr[lo]
""", 1),
    ("""
def is_power_of_two(n):
    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2
    return True
""", 1),
    ("""
def count_bits(n):
    count = 0
    while n:
        n >>= 1
        count += 1
    return count
""", 1),
    ("""
def exp_search(arr, target):
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    lo, hi = i // 2, min(i, len(arr) - 1)
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
def divide_conquer_min(n):
    steps = 0
    while n > 1:
        n = n // 2
        steps += 1
    return steps
""", 1),

    # ── O(n) ── 25 samples ───────────────────────────────────────────────────
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
def contains(arr, target):
    for x in arr:
        if x == target:
            return True
    return False
""", 2),
    ("""
def average(arr):
    total = 0
    for x in arr:
        total += x
    return total / len(arr)
""", 2),
    ("""
def count_negatives(arr):
    count = 0
    for x in arr:
        if x < 0:
            count += 1
    return count
""", 2),
    ("""
def build_prefix_sum(arr):
    prefix = []
    total = 0
    for x in arr:
        total += x
        prefix.append(total)
    return prefix
""", 2),
    ("""
def filter_positives(arr):
    result = []
    for x in arr:
        if x > 0:
            result.append(x)
    return result
""", 2),
    ("""
def map_double(arr):
    result = []
    for x in arr:
        result.append(x * 2)
    return result
""", 2),
    ("""
def find_index(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1
""", 2),
    ("""
def sum_until(arr, limit):
    total = 0
    for x in arr:
        if total + x > limit:
            break
        total += x
    return total
""", 2),
    ("""
def count_greater(arr, threshold):
    count = 0
    for x in arr:
        if x > threshold:
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
    ("""
def string_reverse(s):
    result = ""
    for c in s:
        result = c + result
    return result
""", 2),
    ("""
def remove_duplicates(arr):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result
""", 2),
    ("""
def zip_lists(a, b):
    result = []
    for i in range(min(len(a), len(b))):
        result.append((a[i], b[i]))
    return result
""", 2),
    ("""
def product_list(arr):
    product = 1
    for x in arr:
        product *= x
    return product
""", 2),
    ("""
def find_second_max(arr):
    first = second = float('-inf')
    for x in arr:
        if x > first:
            second = first
            first = x
        elif x > second:
            second = x
    return second
""", 2),

    # ── O(n log n) ── 20 samples ──────────────────────────────────────────────
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
def sort_and_deduplicate(arr):
    arr.sort()
    return list(dict.fromkeys(arr))
""", 3),
    ("""
def rank_elements(arr):
    sorted_arr = sorted(set(arr))
    rank_map = {v: i for i, v in enumerate(sorted_arr)}
    return [rank_map[x] for x in arr]
""", 3),
    ("""
def heap_sort(arr):
    import heapq
    heap = arr[:]
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]
""", 3),
    ("""
def sort_by_abs(arr):
    return sorted(arr, key=abs)
""", 3),
    ("""
def closest_pair_sorted(arr):
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr) - 1):
        min_diff = min(min_diff, arr[i+1] - arr[i])
    return min_diff
""", 3),
    ("""
def sort_strings_by_length(words):
    return sorted(words, key=len)
""", 3),
    ("""
def merge_and_sort(a, b):
    combined = a + b
    combined.sort()
    return combined
""", 3),
    ("""
def top_k_elements(arr, k):
    arr.sort(reverse=True)
    return arr[:k]
""", 3),
    ("""
def sort_tuples(pairs):
    return sorted(pairs, key=lambda x: x[1])
""", 3),
    ("""
def sort_and_binary_search(arr, target):
    arr.sort()
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
""", 3),
    ("""
def find_kth_smallest(arr, k):
    return sorted(arr)[k - 1]
""", 3),
    ("""
def sort_and_group(arr):
    arr.sort()
    groups = []
    i = 0
    while i < len(arr):
        j = i
        while j < len(arr) and arr[j] == arr[i]:
            j += 1
        groups.append(arr[i:j])
        i = j
    return groups
""", 3),
    ("""
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
""", 3),
    ("""
def sort_frequency(arr):
    from collections import Counter
    freq = Counter(arr)
    return sorted(arr, key=lambda x: freq[x])
""", 3),
# ── O(n log n) — 20 snippets nuevos ──────────────────────────────────────────
  ("""
def count_smaller(arr, target):
    arr.sort()
    count = 0
    for x in arr:
        if x < target:
            count += 1
    return count
""", 3),
 
    ("""
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
 
def merge_sort_clean(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort_clean(arr[:mid]), merge_sort_clean(arr[mid:]))
""", 3),
 
    ("""
def find_duplicates_sorted(arr):
    arr.sort()
    duplicates = []
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            duplicates.append(arr[i])
    return duplicates
""", 3),
 
    ("""
def intersection_sorted(a, b):
    a.sort()
    b.sort()
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            result.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return result
""", 3),
 
    ("""
def sort_and_remove_dups(arr):
    if not arr:
        return []
    arr.sort()
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            result.append(arr[i])
    return result
""", 3),
 
    ("""
def majority_element(arr):
    arr.sort()
    return arr[len(arr) // 2]
""", 3),
 
    ("""
def two_sum_sorted(arr, target):
    arr.sort()
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        s = arr[lo] + arr[hi]
        if s == target:
            return (arr[lo], arr[hi])
        elif s < target:
            lo += 1
        else:
            hi -= 1
    return None
""", 3),
 
    ("""
def group_anagrams_count(words):
    words.sort()
    count = 1
    groups = 1
    for i in range(1, len(words)):
        if sorted(words[i]) == sorted(words[i-1]):
            count += 1
        else:
            groups += 1
            count = 1
    return groups
""", 3),
 
    ("""
def find_median_two(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    return arr[n//2]
""", 3),
 
    ("""
def sort_colors(arr):
    arr.sort()
    return arr
""", 3),
 
    ("""
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged
""", 3),
 
    ("""
def sort_by_second(pairs):
    return sorted(pairs, key=lambda x: x[1])
""", 3),
 
    ("""
def nth_largest(arr, n):
    arr.sort()
    return arr[-n]
""", 3),
 
    ("""
def timsort_wrapper(arr):
    result = arr.copy()
    result.sort()
    return result
""", 3),
 
    ("""
def sort_and_zip(a, b):
    a.sort()
    b.sort()
    return list(zip(a, b))
""", 3),
 
    ("""
def unique_sorted(arr):
    return sorted(set(arr))
""", 3),
 
    ("""
def bottom_up_merge_sort(arr):
    width = 1
    n = len(arr)
    while width < n:
        for i in range(0, n, width * 2):
            left = arr[i:i + width]
            right = arr[i + width:i + width * 2]
            merged = []
            li = ri = 0
            while li < len(left) and ri < len(right):
                if left[li] <= right[ri]:
                    merged.append(left[li])
                    li += 1
                else:
                    merged.append(right[ri])
                    ri += 1
            merged.extend(left[li:])
            merged.extend(right[ri:])
            arr[i:i + len(merged)] = merged
        width *= 2
    return arr
""", 3),
 
    ("""
def sort_and_count_inversions(arr):
    arr.sort()
    count = 0
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] > arr[i]:
                count += 1
    return arr
""", 3),
 
    ("""
def rank_transform(arr):
    sorted_unique = sorted(set(arr))
    rank_map = {v: i+1 for i, v in enumerate(sorted_unique)}
    return [rank_map[x] for x in arr]
""", 3),
 
    ("""
def smallest_k_elements(arr, k):
    return sorted(arr)[:k]
""", 3),

    # ── O(n²) ── 22 samples ───────────────────────────────────────────────────
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
    ("""
def count_inversions(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count
""", 4),
    ("""
def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
""", 4),
    ("""
def max_subarray_brute(arr):
    max_sum = float('-inf')
    n = len(arr)
    for i in range(n):
        current = 0
        for j in range(i, n):
            current += arr[j]
            max_sum = max(max_sum, current)
    return max_sum
""", 4),
    ("""
def transpose(matrix):
    n = len(matrix)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][i] = matrix[i][j]
    return result
""", 4),
    ("""
def all_pairs_product(arr):
    result = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            result.append(arr[i] * arr[j])
    return result
""", 4),
    ("""
def gnome_sort(arr):
    i = 0
    while i < len(arr):
        if i == 0 or arr[i] >= arr[i-1]:
            i += 1
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
    return arr
""", 4),
    ("""
def is_matrix_symmetric(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            if M[i][j] != M[j][i]:
                return False
    return True
""", 4),
    ("""
def find_closest_pair(arr):
    min_diff = float('inf')
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            diff = abs(arr[i] - arr[j])
            if diff < min_diff:
                min_diff = diff
    return min_diff
""", 4),
    ("""
def matrix_scalar_multiply(M, k):
    n = len(M)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = M[i][j] * k
    return result
""", 4),
    ("""
def count_zero_submatrices(M):
    count = 0
    n = len(M)
    for i in range(n):
        for j in range(n):
            if M[i][j] == 0:
                count += 1
    return count
""", 4),
    ("""
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
""", 4),
    ("""
def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
""", 4),
    ("""
def find_duplicates(arr):
    duplicates = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates
""", 4),
    ("""
def matrix_diagonal_sum(M):
    n = len(M)
    total = 0
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                total += M[i][j]
    return total
""", 4),
# ── O(n²) — 20 snippets nuevos ───────────────────────────────────────────────
  ("""
def naive_contains_duplicate(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i != j and arr[i] == arr[j]:
                return True
    return False
""", 4),
 
    ("""
def matrix_vector_multiply(M, v):
    n = len(M)
    result = [0] * n
    for i in range(n):
        for j in range(n):
            result[i] += M[i][j] * v[j]
    return result
""", 4),
 
    ("""
def count_pairs_equal_sum(arr, target):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] + arr[j] == target:
                count += 1
    return count // 2
""", 4),
 
    ("""
def naive_string_search(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            positions.append(i)
    return positions
""", 4),
 
    ("""
def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
""", 4),
 
    ("""
def max_rectangle_naive(heights):
    n = len(heights)
    max_area = 0
    for i in range(n):
        for j in range(i, n):
            min_h = min(heights[i:j+1])
            max_area = max(max_area, min_h * (j - i + 1))
    return max_area
""", 4),
 
    ("""
def outer_product(a, b):
    result = []
    for x in a:
        row = []
        for y in b:
            row.append(x * y)
        result.append(row)
    return result
""", 4),
 
    ("""
def is_unique_pairs(arr):
    pairs = set()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            pairs.add((arr[i], arr[j]))
    return len(pairs)
""", 4),
 
    ("""
def naive_lcs_length(s1, s2):
    m, n = len(s1), len(s2)
    max_len = 0
    for i in range(m):
        for j in range(n):
            length = 0
            while (i + length < m and j + length < n
                   and s1[i+length] == s2[j+length]):
                length += 1
            max_len = max(max_len, length)
    return max_len
""", 4),
 
    ("""
def spiral_order(matrix):
    result = []
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            result.append(matrix[i][j])
    return result
""", 4),
 
    ("""
def distance_matrix(points):
    n = len(points)
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dist[i][j] = (dx*dx + dy*dy) ** 0.5
    return dist
""", 4),
 
    ("""
def count_smaller_pairs(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                count += 1
    return count
""", 4),
 
    ("""
def all_substrings(s):
    result = []
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            result.append(s[i:j])
    return result
""", 4),
 
    ("""
def min_distance_pair(arr):
    min_dist = float('inf')
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            dist = abs(arr[i] - arr[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist
""", 4),
 
    ("""
def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3
    sorted_flag = False
    while not sorted_flag:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted_flag = True
        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted_flag = False
            i += 1
    return arr
""", 4),
 
    ("""
def max_sum_subarray_brute(arr):
    n = len(arr)
    max_sum = float('-inf')
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            max_sum = max(max_sum, s)
    return max_sum
""", 4),
 
    ("""
def check_matrix_identity(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            expected = 1 if i == j else 0
            if M[i][j] != expected:
                return False
    return True
""", 4),
 
    ("""
def naive_set_intersection(a, b):
    result = []
    for x in a:
        for y in b:
            if x == y and x not in result:
                result.append(x)
    return result
""", 4),
 
    ("""
def count_zero_rows(matrix):
    count = 0
    for row in matrix:
        all_zero = True
        for val in row:
            if val != 0:
                all_zero = False
        if all_zero:
            count += 1
    return count
""", 4),
 
    ("""
def flatten_matrix(matrix):
    result = []
    for row in matrix:
        for val in row:
            result.append(val)
    return result
""", 4),

    # ── O(n³) ── 15 samples ───────────────────────────────────────────────────
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
    ("""
def all_triplet_products(arr):
    n = len(arr)
    products = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                products.append(arr[i] * arr[j] * arr[k])
    return products
""", 5),
    ("""
def naive_matrix_power(A, p):
    n = len(A)
    result = [[1 if i==j else 0 for j in range(n)] for i in range(n)]
    for _ in range(p):
        temp = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    temp[i][j] += result[i][k] * A[k][j]
        result = temp
    return result
""", 5),
    ("""
def three_sum(arr):
    result = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    result.append([arr[i], arr[j], arr[k]])
    return result
""", 5),
    ("""
def cube_sum(n):
    total = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total += i * j * k
    return total
""", 5),
    ("""
def matrix_chain_naive(A, B, C):
    n = len(A)
    result = [[0]*n for _ in range(n)]
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += A[i][k] * B[k][j]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += temp[i][k] * C[k][j]
    return result
""", 5),
    ("""
def all_index_triplets(n):
    triplets = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                triplets.append((i, j, k))
    return triplets
""", 5),
    ("""
def sum_of_products_triplets(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total += arr[i] + arr[j] + arr[k]
    return total
""", 5),
    ("""
def count_distinct_triplets(arr):
    seen = set()
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                t = tuple(sorted([arr[i], arr[j], arr[k]]))
                seen.add(t)
    return len(seen)
""", 5),
    ("""
def build_3d_table(n):
    table = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                table.append(i + j + k)
    return table
""", 5),
    ("""
def max_triplet_sum(arr):
    max_sum = float('-inf')
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                s = arr[i] + arr[j] + arr[k]
                if s > max_sum:
                    max_sum = s
    return max_sum
""", 5),
    ("""
def count_zero_triplets(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[i] * arr[j] * arr[k] == 0:
                    count += 1
    return count
""", 5),

    # ── O(2^n) ── 18 samples ──────────────────────────────────────────────────
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
        return
    hanoi(n-1, source, aux, target)
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
    ("""
def count_ways(n):
    if n <= 0:
        return 1
    return count_ways(n - 1) + count_ways(n - 2)
""", 6),
    ("""
def power_set(arr):
    if not arr:
        return [[]]
    head = arr[0]
    tail = power_set(arr[1:])
    return tail + [[head] + s for s in tail]
""", 6),
    ("""
def coin_change_naive(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    min_coins = float('inf')
    for coin in coins:
        result = coin_change_naive(coins, amount - coin)
        min_coins = min(min_coins, result + 1)
    return min_coins
""", 6),
    ("""
def subset_sum_exists(arr, target):
    if target == 0:
        return True
    if not arr:
        return False
    return (
        subset_sum_exists(arr[1:], target - arr[0])
        or subset_sum_exists(arr[1:], target)
    )
""", 6),
    ("""
def climbing_stairs(n):
    if n <= 2:
        return n
    return climbing_stairs(n-1) + climbing_stairs(n-2)
""", 6),
    ("""
def all_permutations(arr):
    if len(arr) <= 1:
        return [arr[:]]
    result = []
    for i in range(len(arr)):
        arr[0], arr[i] = arr[i], arr[0]
        for p in all_permutations(arr[1:]):
            result.append([arr[0]] + p)
        arr[0], arr[i] = arr[i], arr[0]
    return result
""", 6),
    ("""
def max_gold(grid, i=0, j=0):
    if i >= len(grid) or j >= len(grid[0]):
        return 0
    down = max_gold(grid, i+1, j)
    right = max_gold(grid, i, j+1)
    return grid[i][j] + max(down, right)
""", 6),
    ("""
def count_binary_strings(n):
    if n == 0:
        return 1
    return count_binary_strings(n-1) + count_binary_strings(n-1)
""", 6),
    ("""
def word_break_naive(s, words):
    if not s:
        return True
    for word in words:
        if s.startswith(word):
            if word_break_naive(s[len(word):], words):
                return True
            if word_break_naive(s[len(word):], words):
                return True
    return False
""", 6),
    ("""
def decode_ways(s, i=0):
    if i == len(s):
        return 1
    if s[i] == '0':
        return 0
    ways = decode_ways(s, i+1)
    if i+1 < len(s) and int(s[i:i+2]) <= 26:
        ways += decode_ways(s, i+2)
    return ways
""", 6),
    ("""
def partition_equal_subset(arr, target, i=0):
    if target == 0:
        return True
    if i == len(arr) or target < 0:
        return False
    return (
        partition_equal_subset(arr, target - arr[i], i+1)
        or partition_equal_subset(arr, target, i+1)
    )
""", 6),
    ("""
def count_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return count_paths(m-1, n) + count_paths(m, n-1)
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
        print(f"  {name:12s}: {dist[cls]} samples")