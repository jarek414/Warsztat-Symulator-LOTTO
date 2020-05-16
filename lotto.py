import random


def lotto():
    your_number_list = []
    while len(your_number_list) < 6:
        while True:
            try:
                your_number = int(input("Please input your number: "))
                break
            except ValueError:
                print("It\'s not a number!")
        if your_number not in range(1, 50):
            print("your number is out of range")
        elif your_number not in your_number_list:
            your_number_list.append(your_number)
        elif your_number in your_number_list:
            print("your already input this number")

    your_number_list.sort()
    computer_list = list(range(1, 50))
    random.shuffle(computer_list)
    random_list = computer_list[:6]
    random_list.sort()
    your_score = 0
    for element in your_number_list:
        if element in random_list:
            your_score += 1

    return f"your list is {your_number_list}, random list is {random_list}, your score is {your_score}"


if __name__ == '__main__':
    print(lotto())
