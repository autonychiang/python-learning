import random
import os

def guess_number():
    target = random.randint(1, 100)
    while True:
        try:
            guess = int(input("请输入你猜测的数字(1-100):"))
            if guess < 1 or guess > 100:
                print("请输入1到100之间的数字！")
            elif guess < target:
                print("猜小了！")
            elif guess > target:
                print("猜大了！")
            else:
                print("恭喜你猜对了！")
                break
        except ValueError:
            print("请输入一个整数！")

if __name__ == "__main__":
    guess_number()
    os.system("pause")