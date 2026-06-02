import ast
import numpy as np

FEATURE_SIZE = 12


class FeatureExtractor(ast.NodeVisitor):

    def __init__(self):
        self.for_loops = 0
        self.while_loops = 0
        self.max_depth = 0
        self._depth = 0
        self.recursive_calls = 0
        self.function_names: set[str] = set()
        self.has_sort = False
        self.has_binary_search = False
        self.total_calls = 0
        self.has_divide_by_2 = False
        self.has_hash_access = False
        # Para contar bucles secuenciales (no anidados)
        self._loop_depths: list[int] = []

    def visit_FunctionDef(self, node):
        self.function_names.add(node.name)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        self.function_names.add(node.name)
        self.generic_visit(node)

    def _enter_loop(self, node):
        self._depth += 1
        self._loop_depths.append(self._depth)
        if self._depth > self.max_depth:
            self.max_depth = self._depth
        self.generic_visit(node)
        self._depth -= 1

    def visit_For(self, node):
        self.for_loops += 1
        self._enter_loop(node)

    def visit_While(self, node):
        self.while_loops += 1
        self._check_binary_search(node)
        self._enter_loop(node)

    def _check_binary_search(self, node):
        src = ast.unparse(node)
        keywords = ("mid", "lo", "hi", "left", "right", "low", "high")
        if sum(k in src for k in keywords) >= 3 and "//" in src:
            self.has_binary_search = True

    def visit_Call(self, node):
        self.total_calls += 1
        if isinstance(node.func, ast.Attribute):
            if node.func.attr in ("sort", "sorted"):
                self.has_sort = True
        if isinstance(node.func, ast.Name):
            if node.func.id == "sorted":
                self.has_sort = True
        self.generic_visit(node)

    def visit_BinOp(self, node):
        # Detectar //2 → patrón logarítmico
        if isinstance(node.op, ast.FloorDiv):
            if isinstance(node.right, ast.Constant) and node.right.value == 2:
                self.has_divide_by_2 = True
        self.generic_visit(node)

    def visit_Subscript(self, node):
        self.has_hash_access = True
        self.generic_visit(node)

    def detect_recursion(self, tree):
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            fn_name = node.name
            count = sum(
                1
                for child in ast.walk(node)
                if (
                    isinstance(child, ast.Call)
                    and isinstance(child.func, ast.Name)
                    and child.func.id == fn_name
                )
            )
            self.recursive_calls = max(self.recursive_calls, count)

    def sequential_loops(self):
        """Bucles que están en profundidad 1 (no anidados)."""
        return sum(1 for d in self._loop_depths if d == 1)


def extract_features(code: str) -> np.ndarray:
    """
    Recibe código Python como string y retorna un vector numpy de
    FEATURE_SIZE dimensiones normalizado en [0, 1].
    """
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return np.zeros(FEATURE_SIZE)

    extractor = FeatureExtractor()
    extractor.visit(tree)
    extractor.detect_recursion(tree)

    num_lines = sum(
        1 for line in code.splitlines()
        if line.strip() and not line.strip().startswith("#")
    )

    raw = np.array([
        extractor.for_loops,                      # 0
        extractor.while_loops,                    # 1
        extractor.max_depth,                      # 2
        float(extractor.recursive_calls > 0),     # 3
        extractor.recursive_calls,                # 4
        float(extractor.has_sort),                # 5
        float(extractor.has_binary_search),       # 6
        extractor.total_calls,                    # 7
        num_lines,                                # 8
        float(extractor.has_divide_by_2),         # 9
        extractor.sequential_loops(),             # 10
        float(extractor.has_hash_access),         # 11
    ], dtype=float)

    # Normalización simple: escalar features de conteo a [0,1]
    # usando máximos razonables para cada feature
    max_vals = np.array([
        10,   # for_loops
        10,   # while_loops
        5,    # max_depth
        1,    # has_recursion (ya es binaria)
        5,    # num_recursive_calls
        1,    # has_sort (binaria)
        1,    # has_binary_search (binaria)
        20,   # total_calls
        50,   # num_lines
        1,    # has_divide_by_2 (binaria)
        10,   # sequential_loops
        1,    # has_hash_access (binaria)
    ], dtype=float)

    normalized = np.clip(raw / max_vals, 0.0, 1.0)
    return normalized


if __name__ == "__main__":
    test_code = """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
"""
    features = extract_features(test_code)
    names = [
        "for_loops", "while_loops", "max_depth", "has_recursion",
        "recursive_calls", "has_sort", "has_binary_search",
        "total_calls", "num_lines", "has_divide_by_2",
        "sequential_loops", "has_hash_access"
    ]
    print("Feature vector (bubble_sort):")
    for name, val in zip(names, features):
        print(f"  {name:25s} = {val:.3f}")