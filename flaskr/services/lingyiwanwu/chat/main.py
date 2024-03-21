# This is a sample Python script.
from typing import List

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import openai_exec

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    msg: List[openai_exec.PerMessage] = [openai_exec.PerMessage(role="user", content="你好")]
    openai_exec.excute(msg)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
