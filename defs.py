
def who_wins(first, second):
    if first == second:
        answer = [f"({first.choice} vs {second.choice})", "Draw"]
    elif first > second:
        answer = [f"({first.choice} vs {second.choice})", "Bot win"]
        first.score = int(first.score) + 1
    else:
        answer = [f"({first.choice} vs {second.choice})", "User win"]
        second.score = int(second.score) + 1

    return answer
