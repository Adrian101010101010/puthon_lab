"""
s
"""
import logging


class RedundantExcessiveCargoWeight(Exception):
    """
    Exception raised when the weight of the cargo exceeds the maximum transport weight limit.

    Args:
        message (str, optional): Custom error message. Defaults to "Excessive weight of
        the cargo was detected.
            Reduce the weight to the maximum transport weight limit".
    """

    def __init__(self, message="Excessive weight of the cargo was"
                               " detected. Reduce the weight to the"
                               " maximum transport weight limit"):
        self.message = message
        super().__init__(self.message)


def logged(exception, mode="file"):
    """
    creates a decorator for exceptions
    :param exception: exception
    :param mode:format selection
    :return: mode
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            """

            :param args:
            :param kwargs:
            :return:
            """
            try:
                return func(*args, **kwargs)
            except exception as ex:
                logger = logging.getLogger(__name__)
                if mode == "console":
                    handler = logging.StreamHandler()
                    logger.addHandler(handler)
                    logger.error(str(ex))
                    logger.removeHandler(handler)
                    return None

                if mode == "file":
                    handler = logging.FileHandler("log.csv")
                    formatter = logging.Formatter("%(asctime)s,%(levelname)s,%(message)s",
                                                  "%Y-%m-%d %H:%M:%S")
                    handler.setFormatter(formatter)

                    logger.addHandler(handler)
                    logger.error(str(ex))
                    logger.removeHandler(handler)
                    return None

                raise ValueError("Invalid logging mode."
                                 " Supported modes are 'console' and 'file'.") from ex

        return wrapper

    return decorator
