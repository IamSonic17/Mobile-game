
def who_wins(first, second):
    if first == second:
        answer = f"Draw ({first.choice} vs {second.choice})"
        print(first.score)
    elif first > second:
        answer = f"Bot win ({first.choice})"
        first.score = int(first.score) + 1
    else:
        answer = f"{second.name} win ({second.choice})"
        second.score = int(second.score) + 1

    return answer


