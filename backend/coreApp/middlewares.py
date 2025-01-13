import logging
import time
from django.db import connection

# Set up logging
request_logger = logging.getLogger("request_logger")
query_logger = logging.getLogger("query_logger")


def log_request(get_response):
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
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
