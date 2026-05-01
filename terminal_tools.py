import random
import sys
import time

from typing import Optional

COLORS =  {'red' : '\033[31m',
'green' : '\033[32m',
'yellow' : '\033[33m',
'default' : '\033[0m',
'blue' : '\033[94m'}


def tell(s: str, *, t_delta: Optional[float] = None, end_of_article: bool = True, color : str = 'default') -> None:
    for i in s:
        print(f"{COLORS[color]}{i}", end="", flush=True)
        time.sleep(t_delta or random.uniform(0.05, 0.15))
    if end_of_article:
        print('\n')

def write_and_rem(s: str, n: int, *, color : str = 'default') -> None:
    tell(s, end_of_article=False, color=color)
    time.sleep(1)
    for i in range(len(s) - 1, len(s) - n - 1, -1):
        sys.stdout.write("\r" + " " * len(s))
        sys.stdout.write(f"\r{COLORS[color]}{s[:i]}")
        sys.stdout.flush()
        time.sleep(0.1)
