import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    number = len(sys.argv)
    list_Scores = []
    flag = 0
    for i in range(1, number):
        try:
            nbr = int(sys.argv[i])
            list_Scores.append(nbr)
        except ValueError:
            flag = 1
            print("Error: Invalid score  All scores must be integers.")
    if number == 1:
        print("No scores provided. Usage: python3 ", end="")
        print("ft_score_analytics.py <score1> <score2> ...")
    elif flag == 0:
        print("Scores processed: [", end="")
        for score in range(0, len(list_Scores)):
            print(f"{list_Scores[score]}", end="")
            if score < number - 2:
                print(", ", end="")
        print("]")
        print(f"Total players: {number - 1}")
        print(f"Total score: {sum(list_Scores)}")
        avg = sum(list_Scores) / len(list_Scores)
        print(f"Average score: {avg:.1f}")
        print(f"High score: {max(list_Scores)}")
        print(f"Low score: {min(list_Scores)}")
        print(f"Score range: {max(list_Scores) - min(list_Scores)}")
