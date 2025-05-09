def format_response_with_headers(data: list, model_cls):
    headers = [
        {
            "title": col.name.replace("_", " ").title(),
            "key": col.name,
            "align":  "start"
            #"end" if col.type.python_type in [int, float] else start
        }
        for col in model_cls.__table__.columns
    ]

    rows = [r.__dict__ | {} for r in data] if data else []

    return {
        "headers": headers,
        "rows": rows
    }
