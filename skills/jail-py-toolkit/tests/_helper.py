"""Shared helpers for jail-py-toolkit tests (stdlib only)."""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(os.path.dirname(HERE), "scripts")
FIXTURES = os.path.join(HERE, "fixtures")
sys.path.insert(0, SCRIPTS)


def fixture(name):
    return os.path.join(FIXTURES, name)


def run(script, *args, stdin=None):
    """Run scripts/<script> -> (returncode, stdout, stderr)."""
    p = subprocess.run([sys.executable, os.path.join(SCRIPTS, script), *args],
                       input=stdin, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def load(script):
    """Import scripts/<script> (hyphenated name) as a module by path."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        script.replace("-", "_").replace(".py", ""), os.path.join(SCRIPTS, script))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
