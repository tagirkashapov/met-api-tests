import logging

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
logger.propagate = False

formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

file_handler = logging.FileHandler("app.log", encoding="utf-8")
stream_handler = logging.StreamHandler()

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


async def log_request(request):
    logger.info(
        "REQUEST  | %-3s | %-3s | %s",
        request.method,
        "",
        request.url
    )


async def log_response(response):
    if response.status_code >= 500:
        log_level = logger.error
    elif response.status_code >= 400:
        log_level = logger.warning
    else:
        log_level = logger.info

    log_level(
        "RESPONSE | %-3s | %-3s | %s",
        response.request.method,
        response.status_code,
        response.request.url
    )
