import random

guess = ''
while guess not in ('表', '裏'):
    print('コインの表裏を当ててください。表か裏を入力してください:')
    guess = input()

toss = random.randint(0, 1)
toss_result = '表' if toss == 0 else '裏'

if toss_result == guess:
    print('当たり!')
else:
    print('はずれ!もう一回当てて!')
    guess = input()
    if toss_result == guess:
        print('当たり！')
    else:
        print('はずれ。このゲームは苦手ですね。')


