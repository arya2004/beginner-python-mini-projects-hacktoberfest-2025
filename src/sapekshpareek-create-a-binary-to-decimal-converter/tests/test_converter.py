import importlib.util
from pathlib import Path


def _load_main_module():
    tests_dir = Path(__file__).parent
    project_dir = tests_dir.parent
    main_path = project_dir / "main.py"
    spec = importlib.util.spec_from_file_location("b2d_main", str(main_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore
    return mod


def test_integer_conversion():
    mod = _load_main_module()
    assert mod.binary_to_decimal("101") == 5


def test_fractional_conversion():
    mod = _load_main_module()
    assert abs(mod.binary_to_decimal("10.11") - 2.75) < 1e-9


def test_negative_conversion():
    mod = _load_main_module()
    assert mod.binary_to_decimal("-101") == -5


def test_zero():
    mod = _load_main_module()
    assert mod.binary_to_decimal("0") == 0


def test_invalid_input():
    mod = _load_main_module()
    try:
        mod.binary_to_decimal("10201")
        assert False, "Expected ValueError for invalid input"
    except ValueError:
        pass
