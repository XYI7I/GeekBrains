# Python 3.10.4

# Домашнее задание:
# Задача с двумя друзьями и собакой – попробовать дома написать код, разбор будет на семинаре.

count = 0
distance = 10000

first_friend_speed = 1
second_friend_speed = 2
dog_speed = 5

friend = 2
while distance > 10:
    if friend == 1:
        time = distance / (first_friend_speed + dog_speed)
        friend = 2
    else:
        time = distance / (second_friend_speed + dog_speed)
        friend = 1
    distance = distance - (first_friend_speed + second_friend_speed) * time
    count += 1
    
print(count)
