import logging
import sys
from datetime import datetime
from logging import config

from fastapi import FastAPI
from pythonjsonlogger import jsonlogger

# from logmiddleware import RouterLoggingMiddleware
#
#
# class CustomJsonFormatter(jsonlogger.JsonFormatter):
#     def add_fields(self, log_record, record, message_dict):
#         super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
#         if not log_record.get('timestamp'):
#             # this doesn't use record.created, so it is slightly off
#             now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
#             log_record['timestamp'] = now
#         if log_record.get('level'):
#             log_record['level'] = log_record['level'].upper()
#         else:
#             log_record['level'] = record.levelname
#
#
# # formatter = CustomJsonFormatter('%(timestamp)s %(level)s %(name)s %(message)s')
# logging_config = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "json": {
#             "class": "main.CustomJsonFormatter",
#             # "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
#             "format": "%(asctime)s %(process)s %(levelname)s %(name)s %(module)s %(funcName)s %(lineno)s"
#         }
#     },
#     "handlers": {
#         "console": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#             "formatter": "json",
#             "stream": sys.stderr,
#         },
#         "file": {
#             "level": "DEBUG",
#             "class": "logging.handlers.RotatingFileHandler",
#             "formatter": "json",
#             "filename": "log1.log"
#         }
#     },
#     "root": {
#         "level": "DEBUG",
#         "handlers": [
#             "console", "file"
#         ],
#         "propagate": True
#     }
# }
#
# config.dictConfig(logging_config)
# # logger = logging.getLogger(__name__)
# #
# # file_handler = logging.FileHandler("logs.txt")
# # handler = logging.StreamHandler()
# #
# # format_str = '%(message)%(levelname)%(name)%(asctime)'
# #
# # formatter = jsonlogger.JsonFormatter(format_str)
# #
# # handler.setFormatter(formatter)
# # file_handler.setFormatter(formatter)
# #
# # logger.addHandler(handler)
# # logger.addHandler(file_handler)
# #
# # logger.propagate = False
app = FastAPI()


# app.add_middleware(
#     RouterLoggingMiddleware,
#     logger=logging.getLogger(__name__)
# )


@app.get("/")
async def root():
    # logger.error('msg clalled end', extra={'url': 'dfdf'})
    x = 1 / 0;
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    # logger.error("the api call end ", extra={"url": "https://example.com/", "payload": "{}", "method": "GET"})
    # logger.debug("The API call end successfully", extra={"url" = "https://example.com/", "payload" = "{}", "method" = "GET" })
    return {"message": f"Hello {name}"}
