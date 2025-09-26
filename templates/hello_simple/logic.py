from datetime import datetime, timezone

def run(args: dict) -> dict:
    """
    Return placeholders for the HTML template.
    No external calls here; just shape the data from args.
    """
    name = args.get("name", "World")
    greeting = args.get("greeting", "Hello")
    items = args.get("items", ["alpha", "beta", "gamma"])
    return {
        "name": name,
        "greeting": greeting,
        "items": items,
        "generated_at": datetime.now(timezone.utc).isoformat()
    }
