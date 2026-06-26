# colors.py

RESET = "\033[0m"

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"


def black_print(*args, **kwargs):
    print(BLACK, end="")
    print(*args, **kwargs)
    print(RESET, end="")


def red_print(*args, **kwargs):
    print(RED, end="")
    print(*args, **kwargs)
    print(RESET, end="")


def green_print(*args, **kwargs):
    print(GREEN, end="")
    print(*args, **kwargs)
    print(RESET, end="")


def yellow_print(*args, **kwargs):
    print(YELLOW, end="")
    print(*args, **kwargs)
    print(RESET, end="")


def blue_print(*args, **kwargs):
    print(BLUE, end="")
    print(*args, **kwargs)
    print(RESET, end="")


def magenta_print(*args, **kwargs):
    print(MAGENTA, end="")
    print(*args, **kwargs)
    print(RESET, end="")


def cyan_print(*args, **kwargs):
    print(CYAN, end="")
    print(*args, **kwargs)
    print(RESET, end="")


def white_print(*args, **kwargs):
    print(WHITE, end="")
    print(*args, **kwargs)
    print(RESET, end="")


def bright_red_print(*args, **kwargs):
    print(BRIGHT_RED, end="")
    print(*args, **kwargs)
    print(RESET, end="")


def bright_green_print(*args, **kwargs):
    print(BRIGHT_GREEN, end="")
    print(*args, **kwargs)
    print(RESET, end="")


def bright_yellow_print(*args, **kwargs):
    print(BRIGHT_YELLOW, end="")
    print(*args, **kwargs)
    print(RESET, end="")


def bright_blue_print(*args, **kwargs):
    print(BRIGHT_BLUE, end="")
    print(*args, **kwargs)
    print(RESET, end="")


def bright_magenta_print(*args, **kwargs):
    print(BRIGHT_MAGENTA, end="")
    print(*args, **kwargs)
    print(RESET, end="")


def bright_cyan_print(*args, **kwargs):
    print(BRIGHT_CYAN, end="")
    print(*args, **kwargs)
    print(RESET, end="")


def bright_white_print(*args, **kwargs):
    print(BRIGHT_WHITE, end="")
    print(*args, **kwargs)
    print(RESET, end="")