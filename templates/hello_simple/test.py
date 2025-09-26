def check_exists(args: dict) -> bool:
    """
    Stub for existence checks later (e.g., query report DB).
    For now, just require 'name' to be present.
    """
    return bool(args.get("name"))
