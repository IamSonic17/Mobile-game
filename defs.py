
def who_wins(first, second):
    if first == second:
        answer = f"Draw (Bot had {first.choice} and {second.name} had {second.choice})"
    elif first > second:
        answer = f"Bot won ({first.choice})"
        first.score = int(first.score) + 1
    else:
        answer = f"The winner is {second.name} ({second.choice})"
        second.score = int(second.score) + 1

    print(answer)

