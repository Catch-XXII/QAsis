from typing import TypeVar, Union, Type, Optional
from locust import SequentialTaskSet
from backend.performance.models import BaseResponse
import json

T = TypeVar("T", bound=BaseResponse)


class ApiClient(SequentialTaskSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _request(
        self,
        method: str,
        url: str,
        name: str,
        headers: dict,
        payload: Optional[str],
        response_model: Type[T],
    ) -> Union[T, None]:
        method = method.upper()

        method_map = {
            "GET": self.client.get,
            "POST": self.client.post,
            "PUT": self.client.put,
            "PATCH": self.client.patch,
            "DELETE": self.client.delete,
            "HEAD": self.client.head,
            "OPTIONS": self.client.options,
        }

        if method not in method_map:
            raise ValueError(f"Unsupported HTTP method: {method}")

        try:
            with method_map[method](
                url, name=name, headers=headers, data=payload, catch_response=True
            ) as response:
                return self._handle_response(response, response_model, method)
        except Exception as e:
            if "response" in locals():
                response.failure(f"Exception occurred: {e}")
            return None

    def _handle_response(
        self, response, response_model: Type[T], method: Optional[str] = None
    ) -> Union[T, None]:
        try:
            response_data = response.json()
        except Exception:
            response.failure("Failed to parse JSON response")
            return None

        status = response.status_code
        if status in {200, 201} and isinstance(response_data, dict):
            print(f"{method or ''}: {json.dumps(response_data, indent=2)}")
            try:
                model_instance = response_model.model_validate(response_data)
                response.success()
                return model_instance
            except Exception as e:
                response.failure(f"Validation failed: {e}")
                return None

        error_message = {
            400: "Invalid request body format",
            401: "Authentication failed",
            403: "Forbidden",
            404: "Not found",
            429: "Too many requests",
            500: "Internal server error",
        }.get(status, f"Unhandled status code: {status}")

        print(f"{status}: {error_message} → {json.dumps(response_data, indent=2)}")
        response.failure(error_message)
        return None

    def make_request(
        self,
        url: str,
        name: str,
        method: str,
        headers: dict,
        payload: Optional[str],
        response_model: Type[T],
    ) -> Union[T, None]:
        return self._request(method, url, name, headers, payload, response_model)
