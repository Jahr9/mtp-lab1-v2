def average_score(scores):
    if not scores:
        raise ValueError("Scores must not be empty")
    return sum(scores) / len(scores)


def main():
    scores = [5, 4, 3, 5]
    result = average_score(scores)
    print(f"Average score: {result:.2f}")


if __name__ == "__main__":
    main()
