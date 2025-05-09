class TableHeaderMixin:
    @classmethod
    def get_column_names(cls) -> list[str]:
        return [col.name for col in cls.__table__.columns]
