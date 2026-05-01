import random
import typing as tp
import math
import importlib
import sys

from terminal_tools import tell, COLORS, write_and_rem


CONGRATS = [
    "Урааа, красава",
    "Точно в цель!",
    "Y Z гордится тобой",
    "Нуууу, норм да, пойдет",
    "А моя бабушка быстрее сделала бебебе",
    "Как ты догадался, что Ev в названии игры это отсылка на Евангелион??! Ответ кстати правильный",
    "Правильно",
    "Замечательно",
    "Я доложу о твоих успехах (но премии не будет)"
]

ABUSE = [
    "Nope",
    "Неа",
    "ВУХАХАХАХЪАХ неправильно",
    "Ну ты чееее, думай еще",
    "Я вот сейчас обижусь и пойду в доту играть, а не с тобой возиться. Неправильно!",
    "Иииии... нет",
    "Если бы я не был таким крутым, я бы подумал, что я тут неправ. Но нет, ответы плохие у тебя!"
]

class Task:
    def __init__(self, mess: str, passcode: str, *, materials: tp.Optional[str] = None):
        self.message = mess
        self.passcode = passcode
        self.materials = materials

    def run(self):
        tell(self.message, color='yellow')
        if self.materials is not None:
            print(COLORS['default'] + self.materials + '\n')
        while True:
            user_ans = str(input()).strip()
            if user_ans == self.passcode:
                break
            else:
                tell(random.choice(ABUSE))
        tell(random.choice(CONGRATS))


class FinalTask:
    def __init__(self, mess: str, time_limit: int, filename: str, materials: str, func_name: str = 'disturb'):
        self.message = mess
        self.time_limit = time_limit
        self.filename = filename
        self.materials = materials
        self.func_name = func_name


    def run(self) -> bool:
        tell(self.message, color='green')
        with open(self.filename + '.py', "w") as file:
            file.write(self.materials)
        for seconds in range(self.time_limit, 0, -1):
            if check_call(self.filename, self.func_name) == 0:
                tell("ВАААААААААААА ТУДА ЕГО КРАСАВАААА!!!!!!!", color='green')
                return True
            write_and_rem(f"{seconds}", math.floor(math.log10(abs(seconds))) + 1, color='blue')
        return False


def check_call(filename: str, func_name: str):
    if filename in sys.modules:
        importlib.reload(sys.modules[filename])
    else:
        importlib.import_module(filename)
    module = sys.modules.get(filename)
    method = getattr(module, func_name)
    return method()


task1_m = """  4           RESUME                   0

  5           LOAD_BUILD_CLASS
              PUSH_NULL
              LOAD_CONST               1 (<code object Ubub at 0x00000275A3CB8D50, line 5>)
              MAKE_FUNCTION
              LOAD_CONST               2 ('Ubub')
              CALL                     2
              STORE_FAST               0 (Ubub)
              RETURN_CONST             0 (None)

Disassembly of <code object Ubub at 0x00000275A3CB8D50, line 5>:
  5           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('code.<locals>.Ubub')
              STORE_NAME               2 (__qualname__)
              LOAD_CONST               1 (5)
              STORE_NAME               3 (__firstlineno__)

  6           LOAD_CONST               2 (<code object __enter__ at 0x00000275A3A8BE10, line 6>)
              MAKE_FUNCTION
              STORE_NAME               4 (__enter__)

 10           LOAD_CONST               3 (<code object __exit__ at 0x00000275A3A8BB40, line 10>)
              MAKE_FUNCTION
              STORE_NAME               5 (__exit__)
              LOAD_CONST               4 (())
              STORE_NAME               6 (__static_attributes__)
              RETURN_CONST             5 (None)"""

final_task_EvGamer = '''
evil_root = 666
def disturb():
    return evil_root
'''

TRIALS = [
    Task("""Тебе нужно прочитать байткод питона. Первая домашка, дада! \n
Мне было лень придумывать интересный код, поэтому я написал тебе чето непонятное, но верю, что ты разберешься! \n
Пароль для прохода дальше - ключевое слово с которым используется основное тело кода\n""", "with", materials=task1_m),
    Task("задача 2", "2"),
    Task("задача 3", "3"),
    Task("задача 4", "4"),
    FinalTask("Я откопал внутренний код ЕвГеймера! Скорее поменяй его, чтобы вылечить его! ОБНУЛИ ЕГО КОРЕНЬ ЗЛА!", 20,
              'EvGamer', final_task_EvGamer)
]
