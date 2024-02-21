import sys
import re
import random

# 回答制限
LIMIT_VAL = 5

# 標準出力メソッド
def normal_stream(word):
    sys.stdout.buffer.write(word.encode('utf-8'))
    sys.stdout.buffer.flush()


# 数値に変換可能か判定する関数
def isInt(value):
    pattern = '[-+]?\d+'
    return True if re.fullmatch(pattern, value) else False

# ゲームの核となる処理
# 数値が当てられるまで終わらない
def guess_number(answer, guess, current_turn=0):
    if current_turn > LIMIT_VAL:
        normal_stream("sorry, you've reached the limit...")
    elif isInt(guess) and answer == int(guess):
        normal_stream(f'great! { guess } is correct!')
    else:
        normal_stream("try again: ")
        new_guess = sys.stdin.readline().strip()
        guess_number(answer, new_guess, current_turn+1)

# 開始位置
normal_stream('Enter min number and max number\n')

min_value = sys.stdin.readline().strip()
max_value = sys.stdin.readline().strip()

if isInt(min_value) and isInt(max_value):
    min = int(min_value)
    max = int(max_value)

    if max > min:
        normal_stream('Enter your guess number\n')
        guess = sys.stdin.readline().strip()
        ans = random.randint(min, max)
        guess_number(ans, guess)

    else:
        normal_stream('The minimum must be smaller than maximum.') 

else:
    normal_stream("Those values you entered aren't numbers.")




