import sys


def ft_score_analytics():
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3"
              "ft_score_analytics.py <score1> <score2> ...")
    else:
        players = len(sys.argv) - 1
        try:
            args = [int(arg) for arg in sys.argv[1:]]
        except ValueError as err:
            print(f"Error: {err}")
            return
        _sum_ = sum(args)
        _max_ = max(args)
        _min_ = min(args)
        print(f"Scores processed: {args}")
        print(f"Total players: {players}")
        print(f"Total score: {sum(args)}")
        print(f"Average score: {_sum_ / players}")
        print(f"High score: {_max_}")
        print(f"Low score: {_min_}")
        print(f"Score range: {_max_ - _min_}")


ft_score_analytics()
