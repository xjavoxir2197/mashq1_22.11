import random

task1 = random.randint(1, 100)
task2 = random.random()
sample_list = [10, 20, 30, 40, 50]
task3 = random.choice(sample_list)
even_nums = [i for i in range(1, 51) if i % 2 == 0]
task4 = random.choice(even_nums)
task5 = [random.randint(1, 100) for _ in range(5)]
shuffle_list = [1, 2, 3, 4, 5]
random.shuffle(shuffle_list)
task6 = shuffle_list
task7 = random.sample(range(1, 11), 3)
task8 = random.choice(["yutdingiz", "yutqazdingiz"])
div5_list = [i for i in range(100, 201) if i % 5 == 0]
task9 = random.choice(div5_list)
task10 = random.choice(["qizil", "yashil", "ko'k"])

print(task1)
print(task2)
print(task3)
print(task4)
print(task5)
print(task6)
print(task7)
print(task8)
print(task9)
print(task10)
