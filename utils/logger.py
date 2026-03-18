import logging
import allure
import inspect
from functools import wraps

logger = logging.getLogger("swaglabs")


def log_step(message: str):
    """
    A unified decorator for logging steps to standard output and Allure simultaneously.
    Supports formatted string injection based on method arguments.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            # Format message with bound arguments safely
            try:
                formatted_message = message.format(**bound_args.arguments)
            except KeyError:
                formatted_message = message

            # 1. Log to standard console Output (Pytest CLI / log_file)
            logger.info(f"STEP: {formatted_message}")

            # 2. Attach step dynamically to Allure report
            with allure.step(formatted_message):
                return func(*args, **kwargs)

        return wrapper

    return decorator
