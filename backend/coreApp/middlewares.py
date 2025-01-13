import logging
import time
from django.db import connection

# Set up logging
request_logger = logging.getLogger("request_logger")
query_logger = logging.getLogger("query_logger")


def log_request(get_response):
    """
    The `log_request` function is a middleware in Python that logs details of incoming requests,
    including IP address, method, path, status code, and duration.

    :param get_response: The `get_response` parameter in the `log_request` function is a function that
    represents the view or middleware that will be called to process the incoming request. It is a
    reference to the next middleware or view in the Django middleware stack
    :return: The `log_request` function is returning a middleware function that logs details of incoming
    requests and their responses. This middleware function wraps around the `get_response` function,
    which processes the incoming request and returns a response. The middleware function calculates the
    duration of the request processing, logs various details of the request and response, and then
    returns the response.
    """

    def middleware(request):
        # Start time
        start_time = time.time()

        # Process the request
        response = get_response(request)

        # Calculate duration
        duration = time.time() - start_time

        # Log request details with context
        log_message = (
            f"{time.strftime('%Y-%m-%d %H:%M:%S')} | "
            f"IP: {get_client_ip(request)} | "
            f"Method: {request.method} | "
            f"Path: {request.get_full_path()} | "
            f"Status Code: {response.status_code} | "
            f"Duration: {duration:.2f}s"
        )

        if response.status_code >= 400:  # Check for error status codes
            request_logger.error(log_message)  # Log as error
        else:
            request_logger.info(log_message)  # Log as info

        return response

    return middleware


def log_queries(get_response):
    """
    The `log_queries` function is a middleware in Python that logs all database queries along with
    relevant request information.

    :param get_response: `get_response` is a function that represents the view function in Django
    middleware. It is responsible for processing the incoming request and returning a response. In the
    provided code snippet, the `middleware` function wraps around the `get_response` function to log
    queries before returning the response
    :return: The `log_queries` function is returning the `middleware` function, which is a Django
    middleware function that logs all database queries made during a request.
    """

    def middleware(request):
        # Process the request
        response = get_response(request)

        # Log all queries
        for query in connection.queries:
            query_logger.info(
                f"{time.strftime('%Y-%m-%d %H:%M:%S')} | "
                f"IP: {get_client_ip(request)} | "
                f"Path: {request.get_full_path()} | "
                f"{query['time']}s | {query['sql']}"
            )

        return response

    return middleware


def get_client_ip(request):
    """
    The function `get_client_ip` retrieves the client's IP address from the request object in a Django
    application, handling cases where the IP address is forwarded or directly available.

    :param request: The `request` parameter in the `get_client_ip` function is typically an object
    representing an HTTP request in a web application framework like Django or Flask. It contains
    information about the incoming request, such as headers, method, and client IP address
    :return: The function `get_client_ip` returns the client's IP address. It first checks if there is
    an "HTTP_X_FORWARDED_FOR" header in the request's META data. If present, it extracts the IP address
    from the header. If not, it falls back to retrieving the IP address from the "REMOTE_ADDR" field in
    the request's META data.
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
