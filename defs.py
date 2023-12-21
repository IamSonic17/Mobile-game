from variants import Variants


def ask_user():
    var = ""
    try:
        variants = list(Variants)
        number = 1
        for variant in variants:
            print(str(number) + ") " + variant.value)
            number = number + 1
        user_choice = int(input("What is in your hand? (choose the number): "))
        print()
        while user_choice not in [1, 2, 3]:
            user_choice = int(input("Error. Choose in 1 to 3: "))
            print()
    except ValueError:
        print("Error. Choose in 1 to 3: ")
        user_choice = int(input("What is in your hand? (choose the number): "))
        print()
        while user_choice not in [1, 2, 3]:
            user_choice = int(input("Error. Choose in 1 to 3: "))
            print()
    if user_choice == 1:
        var = Variants.SCISSORS
    elif user_choice == 2:
        var = Variants.PAPER
    elif user_choice == 3:
        var = Variants.ROCK

    return var


# Function of winner's definition
def who_wins(first, second):
    if first == second:
        print(f"Draw (Bot had {first.choice.value} and {second.name} had {second.choice.value})")
        print()
    elif first > second:
        first.score = first.score + 1
        print(f"Bot won ({first.choice.value})")
        print()
    else:
        second.score = second.score + 1
        print(f"The winner is {second.name} ({second.choice.value})")
        print()
