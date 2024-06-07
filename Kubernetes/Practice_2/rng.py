from random import randint

min_number = int(input('please enter the min number'))
max_number = int(input('please enter the max number'))

if max_number < min_number:
    print("invalid input - shuttting down")
else:
    rnd_number = randint(min_number, max_number)
    print(rnd_number)

# docker run은 attach모드로 실행되는데, 컨테이너로 실행중인 app과는 상호작용을 할 수 없음