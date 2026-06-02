import ast
from dataclasses import dataclass


# ── Resultado ────────────────────────────────────────────────────────────────

@dataclass
class ComplexityResult:
    complexity: str          # e.g. "O(n²)"
    reason: str              # explicación legible
    confidence: str          # "high" | "medium" | "low"
    details: list[str]       # observaciones adicionales


# ── Visitor principal ─────────────────────────────────────────────────────────

class ComplexityVisitor(ast.NodeVisitor):

    def __init__(self):
        self.max_loop_depth: int = 0
        self._current_depth: int = 0
        self.has_sort: bool = False
        self.has_binary_search: bool = False
        self.recursive_calls: int = 0
        self.function_names: set[str] = set()
        self.has_hash_access: bool = False
        self.details: list[str] = []

    # ── Recolectar nombres de funciones definidas ────────────────────────────

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.function_names.add(node.name)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        self.function_names.add(node.name)
        self.generic_visit(node)

    # ── Detectar bucles anidados ─────────────────────────────────────────────

    def _visit_loop(self, node):
        self._current_depth += 1
        if self._current_depth > self.max_loop_depth:
            self.max_loop_depth = self._current_depth
        self.generic_visit(node)
        self._current_depth -= 1

    def visit_For(self, node):
        self._visit_loop(node)

    def visit_While(self, node):
        self._check_binary_search_pattern(node)
        self._visit_loop(node)

    # ── Detectar sort / sorted ───────────────────────────────────────────────

    def visit_Call(self, node: ast.Call):
        # .sort() o sorted()
        if isinstance(node.func, ast.Attribute):
            if node.func.attr in ("sort", "sorted"):
                self.has_sort = True
                self.details.append("Llamada a .sort() / sorted() detectada → O(n log n)")

        if isinstance(node.func, ast.Name):
            if node.func.id == "sorted":
                self.has_sort = True
                self.details.append("Llamada a sorted() detectada → O(n log n)")

        self.generic_visit(node)

    # ── Detectar recursión ───────────────────────────────────────────────────

    def detect_recursion(self, tree: ast.AST):
        """
        Cuenta cuántas veces cada función se llama a sí misma
        directamente dentro de su propio cuerpo.
        """
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            fn_name = node.name
            call_count = 0
            for child in ast.walk(node):
                if (
                    isinstance(child, ast.Call)
                    and isinstance(child.func, ast.Name)
                    and child.func.id == fn_name
                ):
                    call_count += 1
            if call_count >= 2:
                self.recursive_calls = max(
                    self.recursive_calls, call_count
                )
                self.details.append(
                    f"Función '{fn_name}' se llama a sí misma "
                    f"{call_count} veces → posible O(2^n) o superior"
                )
            elif call_count == 1:
                self.recursive_calls = max(self.recursive_calls, 1)
                self.details.append(
                    f"Función '{fn_name}' es recursiva (1 llamada)"
                )

    # ── Detectar patrón búsqueda binaria ─────────────────────────────────────

    def _check_binary_search_pattern(self, node: ast.While):
        """
        Heurística: while lo <= hi / while left < right
        con asignación mid = (lo + hi) // 2
        """
        src = ast.unparse(node)
        keywords = ("mid", "lo", "hi", "left", "right", "low", "high")
        if sum(k in src for k in keywords) >= 3 and "//" in src:
            self.has_binary_search = True
            self.details.append(
                "Patrón while + mid = (lo+hi)//2 detectado → O(log n)"
            )

    # ── Detectar acceso O(1) a dict/set ──────────────────────────────────────

    def visit_Subscript(self, node: ast.Subscript):
        self.has_hash_access = True
        self.generic_visit(node)


# ── Función pública ───────────────────────────────────────────────────────────

def analyze_complexity(code: str) -> ComplexityResult:
    """
    Recibe un string con código Python y devuelve un ComplexityResult.
    """
    # 1. Parsear
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return ComplexityResult(
            complexity="Error",
            reason=f"Sintaxis inválida: {e}",
            confidence="high",
            details=[]
        )

    # 2. Visitar
    visitor = ComplexityVisitor()
    visitor.visit(tree)
    visitor.detect_recursion(tree)

    details = visitor.details
    loops = visitor.max_loop_depth

    # 3. Clasificar por precedencia (de mayor a menor complejidad)

    # O(n!) — recursión con ≥ 3 llamadas propias (factorial)
    if visitor.recursive_calls >= 3:
        return ComplexityResult(
            complexity="O(n!)",
            reason=(
                "Se detectó recursión con múltiples llamadas propias "
                "(≥3), patrón típico de fuerza bruta factorial."
            ),
            confidence="medium",
            details=details
        )

    # O(2^n) — recursión con exactamente 2 llamadas propias
    if visitor.recursive_calls == 2:
        return ComplexityResult(
            complexity="O(2^n)",
            reason=(
                "Función recursiva con 2 llamadas a sí misma "
                "en cada invocación (ej: Fibonacci naive)."
            ),
            confidence="high",
            details=details
        )

    # O(n³) — 3 bucles anidados
    if loops >= 3:
        return ComplexityResult(
            complexity="O(n³)",
            reason=f"{loops} bucles anidados detectados.",
            confidence="high",
            details=details
        )

    # O(n²) — 2 bucles anidados
    if loops == 2:
        return ComplexityResult(
            complexity="O(n²)",
            reason="2 bucles anidados detectados (ej: Bubble Sort, fuerza bruta).",
            confidence="high",
            details=details
        )

    # O(n log n) — sort/sorted o mergesort detectado
    if visitor.has_sort and loops == 1:
        return ComplexityResult(
            complexity="O(n log n)",
            reason="Bucle + llamada a sort() / sorted() detectados.",
            confidence="high",
            details=details
        )

    if visitor.has_sort:
        return ComplexityResult(
            complexity="O(n log n)",
            reason="Llamada a sort() / sorted() detectada.",
            confidence="high",
            details=details
        )

    # O(log n) — búsqueda binaria
    if visitor.has_binary_search:
        return ComplexityResult(
            complexity="O(log n)",
            reason="Patrón de búsqueda binaria detectado (while + mid).",
            confidence="high",
            details=details
        )

    # O(n) — recursión lineal (1 llamada propia) o 1 bucle simple
    if visitor.recursive_calls == 1:
        return ComplexityResult(
            complexity="O(n)",
            reason="Recursión lineal detectada (1 llamada recursiva por frame).",
            confidence="medium",
            details=details
        )

    if loops == 1:
        return ComplexityResult(
            complexity="O(n)",
            reason="Un bucle simple detectado.",
            confidence="high",
            details=details
        )

    # O(1) — sin bucles, sin recursión
    return ComplexityResult(
        complexity="O(1)",
        reason=(
            "Sin bucles ni recursión detectados. "
            "Acceso directo o operaciones constantes."
            + (" Acceso a estructura hash/lista por índice." if visitor.has_hash_access else "")
        ),
        confidence="high",
        details=details
    )


# ── Formato de respuesta para Telegram ───────────────────────────────────────

def format_response(result: ComplexityResult) -> str:
    lines = [
        "🔍 *Análisis de Complejidad Algorítmica*",
        "",
        f"📊 *Complejidad:* `{result.complexity}`",
        f"💡 *Razón:* {result.reason}",
        f"🎯 *Confianza:* {result.confidence}",
    ]
    if result.details:
        lines.append("")
        lines.append("📝 *Detalles detectados:*")
        for d in result.details:
            lines.append(f"  • {d}")
    return "\n".join(lines)