import datetime

from log import get_logger
from sqlalchemy.engine import ResultProxy

log = get_logger()


def resultproxy_to_dict(result: ResultProxy) -> dict:
    d, a = {}, []
    for rowproxy in result:
        for column, value in rowproxy.items():
            if isinstance(value, datetime.datetime):
                value = str(value)
            d = {**d, **{column: value}}
        a.append(d)
    return a
