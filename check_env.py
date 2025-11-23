import sys
import os

print(f"Python Executable: {sys.executable}")
print(f"CWD: {os.getcwd()}")

try:
    import manim
    print(f"Manim Version: {manim.__version__}")
    print(f"Manim Location: {manim.__file__}")
except ImportError:
    print("❌ Manim NOT installed!")
