"""
test_feature_extractor.py
-------------------------

Conjunto de pruebas unitarias para el módulo
feature_extractor.py.

Estas pruebas verifican la correcta extracción,
normalización y representación de las características
estructurales utilizadas por el clasificador de
complejidad algorítmica.

Objetivos de las pruebas
------------------------

1. Validar el contrato de extract_features().
2. Verificar la dimensión del vector de salida.
3. Comprobar la normalización en el rango [0,1].
4. Detectar correctamente:
   - Bucles for
   - Bucles while
   - Profundidad de anidamiento
   - Recursividad
   - Ordenamientos
   - Búsqueda binaria
   - División por 2
   - Accesos indexados
   - Features avanzadas de la versión v3
5. Validar patrones asociados a complejidades
   asintóticas conocidas.
6. Verificar el comportamiento interno de
   FeatureExtractor.

Autores:
    Cristian Cortes
    Katherine Arboleda

Proyecto:
    Clasificador Inteligente de Complejidad Algorítmica
    mediante Redes Neuronales Multicapa (MLP)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
import numpy as np
from complexity.feature_extractor import extract_features, FeatureExtractor, FEATURE_SIZE


# ── Contract ─────────────────────────────────────────────────────────────────

class TestExtractFeaturesContract:

    def test_returns_numpy_array(self):
        assert isinstance(extract_features("x = 1"), np.ndarray)

    def test_output_length_is_feature_size(self):
        assert len(extract_features("x = 1")) == FEATURE_SIZE

    def test_feature_size_is_20(self):
        assert FEATURE_SIZE == 20

    def test_all_values_in_0_1(self):
        code = "for i in range(n):\n    for j in range(n):\n        pass"
        f = extract_features(code)
        assert np.all(f >= 0.0) and np.all(f <= 1.0)

    def test_syntax_error_returns_zeros(self):
        np.testing.assert_array_equal(extract_features("def :((("), np.zeros(FEATURE_SIZE))

    def test_empty_string_returns_expected_vector(self):
        expected = np.zeros(FEATURE_SIZE)
        expected[16] = 0.5  # loop_count_ratio()

        np.testing.assert_array_equal(
            extract_features(""),
            expected
        )

    def test_comments_only_returns_expected_vector(self):
        expected = np.zeros(FEATURE_SIZE)
        expected[16] = 0.5

        np.testing.assert_array_equal(
            extract_features("# comment\n# another"),
            expected
        )


# ── Feature-index tests ───────────────────────────────────────────────────────
# Index map:
#  0=for_loops  1=while_loops  2=max_depth  3=has_recursion  4=recursive_calls
#  5=has_sort   6=has_binary_search  7=total_calls  8=num_lines
#  9=has_divide_by_2  10=sequential_loops  11=has_hash_access
# 12=nested_loop_depth_2  13=has_sort_plus_loop  14=recursive_divide
# 15=has_sort_in_function  16=loop_count_ratio  17=has_triple_nest
# 18=calls_per_line  19=has_two_rec_calls

class TestForLoopDetection:
    def test_single_for(self):
        assert extract_features("for i in range(n):\n    pass")[0] == pytest.approx(1/10)

    def test_double_for(self):
        assert extract_features("for i in range(n):\n    for j in range(n):\n        pass")[0] == pytest.approx(2/10)

    def test_no_for(self):
        assert extract_features("x = 1 + 1")[0] == pytest.approx(0.0)


class TestWhileLoopDetection:
    def test_single_while(self):
        assert extract_features("while n > 0:\n    n -= 1")[1] == pytest.approx(1/10)

    def test_no_while(self):
        assert extract_features("for i in range(n):\n    pass")[1] == pytest.approx(0.0)


class TestMaxDepthDetection:
    def test_depth_1(self):
        assert extract_features("for i in range(n):\n    pass")[2] == pytest.approx(1/5)

    def test_depth_2(self):
        code = "for i in range(n):\n    for j in range(n):\n        pass"
        assert extract_features(code)[2] == pytest.approx(2/5)

    def test_depth_3(self):
        code = "for i in range(n):\n    for j in range(n):\n        for k in range(n):\n            pass"
        assert extract_features(code)[2] == pytest.approx(3/5)

    def test_sequential_loops_keep_depth_1(self):
        code = "for i in range(n):\n    pass\nfor j in range(n):\n    pass"
        assert extract_features(code)[2] == pytest.approx(1/5)


class TestRecursionDetection:
    def test_recursive_function(self):
        code = "def fib(n):\n    if n<=1: return n\n    return fib(n-1)+fib(n-2)"
        f = extract_features(code)
        assert f[3] == pytest.approx(1.0)   # has_recursion
        assert f[4] > 0.0                   # recursive_calls

    def test_non_recursive(self):
        code = "def add(a, b):\n    return a + b"
        f = extract_features(code)
        assert f[3] == pytest.approx(0.0)
        assert f[4] == pytest.approx(0.0)

    def test_two_recursive_calls(self):
        code = "def fib(n):\n    if n<=1: return n\n    return fib(n-1)+fib(n-2)"
        assert extract_features(code)[4] == pytest.approx(2/5)


class TestSortDetection:
    def test_sorted_builtin(self):
        assert extract_features("result = sorted(arr)")[5] == pytest.approx(1.0)

    def test_list_sort_method(self):
        assert extract_features("arr.sort()")[5] == pytest.approx(1.0)

    def test_no_sort(self):
        assert extract_features("x = 1 + 1")[5] == pytest.approx(0.0)


class TestBinarySearchDetection:
    def test_binary_search_pattern(self):
        code = (
            "def bs(arr, target):\n"
            "    lo, hi = 0, len(arr)-1\n"
            "    while lo <= hi:\n"
            "        mid = (lo+hi)//2\n"
            "        if arr[mid]==target: return mid\n"
            "        elif arr[mid]<target: lo=mid+1\n"
            "        else: hi=mid-1\n"
            "    return -1"
        )
        assert extract_features(code)[6] == pytest.approx(1.0)

    def test_simple_loop_not_binary_search(self):
        assert extract_features("for i in range(n):\n    pass")[6] == pytest.approx(0.0)


class TestDivideBy2Detection:
    def test_floor_div_2(self):
        assert extract_features("mid = (lo+hi)//2")[9] == pytest.approx(1.0)

    def test_div_by_3_not_detected(self):
        assert extract_features("x = n//3")[9] == pytest.approx(0.0)


class TestHashAccess:
    def test_list_index(self):
        assert extract_features("x = arr[0]")[11] == pytest.approx(1.0)

    def test_dict_access(self):
        assert extract_features("v = d['key']")[11] == pytest.approx(1.0)

    def test_no_subscript(self):
        assert extract_features("x = 1+1")[11] == pytest.approx(0.0)


# ── New v3 features ───────────────────────────────────────────────────────────

class TestNestedLoopDepth2:
    """Feature 12: exactly depth-2 nesting, no depth-3+"""

    def test_double_nested_is_1(self):
        code = "for i in range(n):\n    for j in range(n):\n        pass"
        assert extract_features(code)[12] == pytest.approx(1.0)

    def test_triple_nested_is_0(self):
        code = "for i in range(n):\n    for j in range(n):\n        for k in range(n):\n            pass"
        assert extract_features(code)[12] == pytest.approx(0.0)

    def test_single_loop_is_0(self):
        assert extract_features("for i in range(n):\n    pass")[12] == pytest.approx(0.0)


class TestHasSortPlusLoop:
    """Feature 13: sort() AND a sequential loop together"""

    def test_sort_with_loop(self):
        code = "arr.sort()\nfor i in range(len(arr)-1):\n    print(arr[i])"
        assert extract_features(code)[13] == pytest.approx(1.0)

    def test_sort_without_loop(self):
        assert extract_features("return sorted(arr)")[13] == pytest.approx(0.0)

    def test_loop_without_sort(self):
        assert extract_features("for i in range(n):\n    pass")[13] == pytest.approx(0.0)


class TestRecursiveDivide:
    """Feature 14: recursion + //2 → merge-sort / log pattern"""

    def test_merge_sort_pattern(self):
        code = (
            "def merge_sort(arr):\n"
            "    if len(arr)<=1: return arr\n"
            "    mid = len(arr)//2\n"
            "    left = merge_sort(arr[:mid])\n"
            "    right = merge_sort(arr[mid:])\n"
            "    return left+right"
        )
        assert extract_features(code)[14] == pytest.approx(1.0)

    def test_simple_recursion_no_divide(self):
        code = "def f(n):\n    if n==0: return 0\n    return f(n-1)"
        assert extract_features(code)[14] == pytest.approx(0.0)

    def test_divide_no_recursion(self):
        assert extract_features("mid = n//2")[14] == pytest.approx(0.0)


class TestLoopCountRatio:
    """Feature 16: for/(for+while) ratio"""

    def test_only_for_loops_returns_1(self):
        f = extract_features("for i in range(n):\n    pass")
        assert f[16] == pytest.approx(1.0)

    def test_only_while_loops_returns_0(self):
        f = extract_features("while n > 0:\n    n -= 1")
        assert f[16] == pytest.approx(0.0)

    def test_no_loops_returns_half(self):
        f = extract_features("x = 1 + 1")
        assert f[16] == pytest.approx(0.5)

    def test_mixed_returns_between_0_and_1(self):
        code = "for i in range(n):\n    pass\nwhile m>0:\n    m-=1"
        f = extract_features(code)
        assert 0.0 < f[16] < 1.0


class TestHasTripleNest:
    """Feature 17: depth >= 3"""

    def test_triple_nested_is_1(self):
        code = "for i in range(n):\n    for j in range(n):\n        for k in range(n):\n            pass"
        assert extract_features(code)[17] == pytest.approx(1.0)

    def test_double_nested_is_0(self):
        code = "for i in range(n):\n    for j in range(n):\n        pass"
        assert extract_features(code)[17] == pytest.approx(0.0)

    def test_single_loop_is_0(self):
        assert extract_features("for i in range(n):\n    pass")[17] == pytest.approx(0.0)


class TestHasTwoRecursiveCalls:
    """Feature 19: exactly 2 recursive calls per function → O(2^n)"""

    def test_fibonacci_is_1(self):
        code = "def fib(n):\n    if n<=1: return n\n    return fib(n-1)+fib(n-2)"
        assert extract_features(code)[19] == pytest.approx(1.0)

    def test_single_recursive_call_is_0(self):
        code = "def f(n):\n    if n==0: return 0\n    return f(n-1)"
        assert extract_features(code)[19] == pytest.approx(0.0)

    def test_no_recursion_is_0(self):
        assert extract_features("x = 1+1")[19] == pytest.approx(0.0)

    def test_hanoi_two_recursive_calls(self):
        code = (
            "def hanoi(n, s, t, a):\n"
            "    if n==1: return\n"
            "    hanoi(n-1, s, a, t)\n"
            "    hanoi(n-1, a, t, s)"
        )
        assert extract_features(code)[19] == pytest.approx(1.0)


# ── Complexity fingerprint tests ──────────────────────────────────────────────

class TestComplexityFingerprints:

    def test_o1_no_loops_no_recursion(self):
        code = "def get(arr): return arr[0]"
        f = extract_features(code)
        assert f[0] == 0.0   # no for
        assert f[1] == 0.0   # no while
        assert f[3] == 0.0   # no recursion

    def test_ologn_has_binary_search_and_divide(self):
        code = (
            "def bs(arr, t):\n"
            "    lo, hi = 0, len(arr)-1\n"
            "    while lo<=hi:\n"
            "        mid=(lo+hi)//2\n"
            "        if arr[mid]==t: return mid\n"
            "        elif arr[mid]<t: lo=mid+1\n"
            "        else: hi=mid-1\n"
            "    return -1"
        )
        f = extract_features(code)
        assert f[6] == pytest.approx(1.0)   # has_binary_search
        assert f[9] == pytest.approx(1.0)   # has_divide_by_2
        assert f[16] == pytest.approx(0.0)  # only while loops → ratio=0

    def test_on_single_loop_ratio_1(self):
        code = "def find(arr, t):\n    for x in arr:\n        if x==t: return True\n    return False"
        f = extract_features(code)
        assert f[0] == pytest.approx(1/10)
        assert f[2] == pytest.approx(1/5)
        assert f[16] == pytest.approx(1.0)  # only for loops

    def test_onlogn_sort_plus_loop(self):
        code = (
            "def remove_dups(arr):\n"
            "    arr.sort()\n"
            "    result = [arr[0]]\n"
            "    for i in range(1, len(arr)):\n"
            "        if arr[i]!=arr[i-1]: result.append(arr[i])\n"
            "    return result"
        )
        f = extract_features(code)
        assert f[5]  == pytest.approx(1.0)  # has_sort
        assert f[13] == pytest.approx(1.0)  # has_sort_plus_loop
        assert f[15] == pytest.approx(1.0)  # has_sort_in_function

    def test_on2_depth2_not_depth3(self):
        code = (
            "def bubble(arr):\n"
            "    for i in range(len(arr)):\n"
            "        for j in range(len(arr)-1):\n"
            "            if arr[j]>arr[j+1]: arr[j],arr[j+1]=arr[j+1],arr[j]\n"
            "    return arr"
        )
        f = extract_features(code)
        assert f[2]  == pytest.approx(2/5)  # max_depth=2
        assert f[12] == pytest.approx(1.0)  # nested_loop_depth_2
        assert f[17] == pytest.approx(0.0)  # no triple nest

    def test_on3_triple_nest(self):
        code = (
            "def mm(A,B):\n"
            "    n=len(A)\n"
            "    C=[[0]*n for _ in range(n)]\n"
            "    for i in range(n):\n"
            "        for j in range(n):\n"
            "            for k in range(n):\n"
            "                C[i][j]+=A[i][k]*B[k][j]\n"
            "    return C"
        )
        f = extract_features(code)
        assert f[2]  == pytest.approx(3/5)  # max_depth=3
        assert f[17] == pytest.approx(1.0)  # has_triple_nest
        assert f[12] == pytest.approx(0.0)  # depth-2 flag is 0 when depth-3 exists

    def test_o2n_two_recursive_calls(self):
        code = "def fib(n):\n    if n<=1: return n\n    return fib(n-1)+fib(n-2)"
        f = extract_features(code)
        assert f[3]  == pytest.approx(1.0)  # has_recursion
        assert f[19] == pytest.approx(1.0)  # has_two_rec_calls
        assert f[0]  == pytest.approx(0.0)  # no for loops

    def test_output_clipped_at_1_for_many_loops(self):
        lines = "\n".join(f"for i{i} in range(n):\n    pass" for i in range(11))
        f = extract_features(lines)
        assert f[0] == pytest.approx(1.0)


# ── FeatureExtractor internal unit tests ──────────────────────────────────────

class TestFeatureExtractorInternal:

    def _make(self, code):
        import ast
        ext = FeatureExtractor()
        tree = ast.parse(code)
        ext.visit(tree)
        ext.detect_recursion(tree)
        return ext

    def test_for_counter(self):
        e = self._make("for i in range(n):\n    for j in range(n):\n        pass")
        assert e.for_loops == 2

    def test_while_counter(self):
        assert self._make("while True:\n    break").while_loops == 1

    def test_max_depth_3(self):
        code = "for i in range(n):\n    for j in range(n):\n        for k in range(n):\n            pass"
        assert self._make(code).max_depth == 3

    def test_function_name_registered(self):
        assert "my_func" in self._make("def my_func():\n    pass").function_names

    def test_has_sort_true(self):
        assert self._make("sorted(arr)").has_sort is True

    def test_has_sort_false(self):
        assert self._make("x = 1+1").has_sort is False

    def test_divide_by_2(self):
        assert self._make("mid = n//2").has_divide_by_2 is True

    def test_hash_access(self):
        assert self._make("x = arr[0]").has_hash_access is True

    def test_sequential_loops(self):
        code = (
            "for i in range(n):\n    pass\n"
            "for j in range(n):\n"
            "    for k in range(n):\n        pass"
        )
        e = self._make(code)
        assert e.sequential_loops() == 2

    def test_nested_loop_depth_2_true(self):
        code = "for i in range(n):\n    for j in range(n):\n        pass"
        assert self._make(code).nested_loop_depth_2() == 1.0

    def test_nested_loop_depth_2_false_for_depth3(self):
        code = "for i in range(n):\n    for j in range(n):\n        for k in range(n):\n            pass"
        assert self._make(code).nested_loop_depth_2() == 0.0

    def test_has_triple_nest_true(self):
        code = "for i in range(n):\n    for j in range(n):\n        for k in range(n):\n            pass"
        assert self._make(code).has_triple_nest() == 1.0

    def test_two_recursive_calls_flag(self):
        code = "def fib(n):\n    if n<=1: return n\n    return fib(n-1)+fib(n-2)"
        assert self._make(code).has_two_recursive_calls() == 1.0

    def test_loop_count_ratio_for_only(self):
        assert self._make("for i in range(n):\n    pass").loop_count_ratio() == pytest.approx(1.0)

    def test_loop_count_ratio_while_only(self):
        assert self._make("while n>0:\n    n-=1").loop_count_ratio() == pytest.approx(0.0)

    def test_loop_count_ratio_no_loops(self):
        assert self._make("x = 1").loop_count_ratio() == pytest.approx(0.5)