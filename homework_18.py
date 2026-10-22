import sys

from loguru import logger


logger.remove()
logger.add(sys.stderr, level="INFO", format="{level} | {message}")
logger.add("homework.log", level="DEBUG", format="{level} | {message}", encoding="utf-8")


def divide(a, b):
    logger.debug("divide викликано з a={}, b={}", a, b)
    try:
        result = a / b
        logger.info("Результат ділення: {}", result)
        return result
    except ZeroDivisionError:
        logger.error("Ділення на нуль: a={}, b={}", a, b)
        return None


if __name__ == "__main__":
    divide(10, 2)
    divide(10, 0)