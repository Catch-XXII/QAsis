class BaseResponse:
    def parse(self, response_data: dict) -> None:
        """Abstract method to parse response data into an object."""
        raise NotImplementedError("Subclasses should implement this method.")
