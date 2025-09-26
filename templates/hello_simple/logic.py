from datetime import datetime, timezone

def main(args, db):
    """
    args: dict from API
    db: MSSQLClient (pyodbc) context-managed by the app
    """
    name = args.get("name", "World")
    greeting = args.get("greeting", "Hello")

    # Example DB use (commented if you don't have MSSQL ready yet)
    # row = db.fetch_one("SELECT TOP 1 id, title FROM dbo.reports WHERE owner = ?", [name])
    # recent_title = row["title"] if row else "N/A"

    items = args.get("items") or ["alpha", "beta", "gamma"]
    return {
        "name": name,
        "greeting": greeting,
        "items": items,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        # "recent_title": recent_title,
    }
