"""Excel processing utilities."""

from typing import Dict


def parse_file1(content: bytes) -> None:
    """Placeholder parser for osint."""
    # Implement actual logic here
    pass


def parse_file2(content: bytes) -> None:
    """Placeholder parser for excel."""
    # Implement actual logic here
    pass


def parse_file3_excel_new_mode(content: bytes) -> None:
    """Placeholder parser for cards in the new mode."""
    # Implement actual logic here
    pass


def process_and_send_excel(files: Dict[str, bytes]) -> None:
    """Process uploaded Excel-related files and send them somewhere."""
    required_keys = ["osint", "excel", "cards"]
    missing = [key for key in required_keys if files.get(key) is None]
    if missing:
        missing_list = ", ".join(missing)
        raise ValueError(f"Missing required file(s): {missing_list}")

    parse_file1(files["osint"])
    parse_file2(files["excel"])
    parse_file3_excel_new_mode(files["cards"])
