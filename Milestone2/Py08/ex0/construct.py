import sys, os, site

def check_matrix_status() -> None:
    is_venv: bool = sys.prefix != sys.base_prefix


if is_venv:
    