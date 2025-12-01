import subprocess
import sys
from pathlib import Path


def run_case(q4_path: Path, input_path: Path, expected_path: Path) -> bool:
    """Run Q4 solution for a single test case and compare output."""
    result = subprocess.run(
        [sys.executable, str(q4_path)],
        input=input_path.read_text(),
        text=True,
        capture_output=True,
        check=False,
    )

    expected_output = expected_path.read_text()
    return result.stdout == expected_output


def main() -> None:
    data_dir = Path(__file__).resolve().parent
    q4_path = data_dir.parent / "Q4.py"

    input_files = sorted(data_dir.glob("*.in"))
    if not input_files:
        print("No input files found.")
        return

    all_passed = True
    for input_path in input_files:
        expected_path = input_path.with_suffix(".out")
        if not expected_path.exists():
            print(f"Missing expected output for {input_path.name}")
            all_passed = False
            continue

        passed = run_case(q4_path, input_path, expected_path)
        status = "PASS" if passed else "FAIL"
        print(f"{status} - {input_path.name}")
        all_passed = all_passed and passed

    if all_passed:
        print("All test cases passed.")
    else:
        print("Some test cases failed.")


if __name__ == "__main__":
    main()
