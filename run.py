from speckle_automate import execute_automate_function
import sys
from pathlib import Path

# Add src to the sys.path
src_path = Path(__file__).resolve().parent / 'src'
sys.path.append(str(src_path))

from src.main import automate_function, FunctionInputs

if __name__ == "__main__":
    # Entry point: Execute the automate function with defined inputs.
    execute_automate_function(automate_function, FunctionInputs)
