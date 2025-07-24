from uvicorn.workers import UvicornWorker


class NoLifespanUvicornWorker(UvicornWorker):
    CONFIG_KWARGS = {"loop": "uvloop", "http": "httptools", "lifespan": "off"}
