import time

from terminal_tools import tell, write_and_rem
from task import TRIALS, COLORS
from regarding import regard

def hello():
    tell("So you've decided to become a hero", end_of_article=False, color='red')
    tell("...", t_delta=0.5, color='red')
    time.sleep(2)
    tell("My name is EvGamer and this is my EvGame!\nYou'll solve some puzzles to complete.", color="yellow")
    write_and_rem("I would try to write in English but my English is capital of Great Britain, gj", 2, color="yellow")
    time.sleep(1.2)
    tell("поэтому дальше я буду писать на русском! \
В общем, у меня есть несколько испытаний, которые тебе нужно пройти! \
Для начала давай разберемся с форматом тасок. Я вывожу условие, ты вводишь ответ. В целом, всё :)", color="yellow")


def bogdasha():
    tell("Псссс", color='green')
    time.sleep(2)
    tell("ЭЙ! ЕвГеймер отвернулся, пойдем со мной, быстрее!", color='green')
    time.sleep(0.5)
    tell("Вы отошли вместе с неизвестной личностью")
    tell("Видимо ты как то заинтересовал ЕвГеймера.. ", color='green')
    time.sleep(1.2)
    tell("Ладно... Меня зовут Богдаша, я здесь, чтобы спасти тебя. Как ты мог заметить, цвет шрифта у ЕвГеймера - желтый.", color='green')
    tell("Это цвет предупреждений, и как ты мог догадаться, на самом деле, Евгеймер - ", end_of_article=False, color='green')
    time.sleep(0.7)
    tell("ВАЙБКОДЕР!!!!!", t_delta=0.08, color='green')
    tell("Но, как я сказал, я хочу тебе помочь. И мне ты можешь доверять, ведь у меня шрифт зеленого цвета, как у крутых хакеров.", color='green')
    tell("Пока что я только собираю данные, он хоть и вайбкодер, но и ГПТ нынче обучен достаточно сильно.", color='green')
    tell("Короче я появлюсь, когда всё будет готово, а пока - будь настороже. И помни", end_of_article=False, color='green')
    tell('...', t_delta=0.4, color='green')
    tell('СИНЯЯ МАТЧА - ЛОЖЬ! СИНЯЯ МАТЧА - ЛОЖЬ! СИНЯЯ МАТЧА - ЛОЖЬ!!!!!!!!', t_delta=0.04, color='green')
    time.sleep(0.5)
    tell("Богдаша убежал, а вы вернулись к ЕвГеймеру")


if __name__ == "__main__":
    time.sleep(2)
    hello()
    task_cnt = 1
    for t in TRIALS:
        if task_cnt == 3:
            bogdasha()
            pass
        print(COLORS['blue'] + "===================== Задача " + str(task_cnt) + "=====================" + COLORS['default'])
        t.run()
        regard(task_cnt)
        task_cnt += 1
    tell("На этом - всё :)", color='default')
    time.sleep(5)
