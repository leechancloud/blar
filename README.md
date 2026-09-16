# blar
import random

answer = random.randint(1, 10)

while True:
    guess = int(input("1부터 10까지 숫자를 맞혀보세요: "))

    if guess == answer:
        print("정답입니다! 🎉")
        break
    elif guess < answer:
        print("더 큰 숫자예요.")
    else:
        print("더 작은 숫자예요.")
