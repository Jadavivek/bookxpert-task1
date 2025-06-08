from app.matcher import NameMatcher

def main():
    # Load names from file
    with open("data/names.txt", "r", encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]

    # Create matcher
    matcher = NameMatcher(names)

    # Ask user for input
    input_name = input("Enter a name to match: ")

    # Get best match
    best_match = matcher.get_best_match(input_name)
    print(f"\n✅ Best Match: {best_match[0]} - Score: {round(best_match[1], 4)}")

    # Get top 5 matches
    print("\n📋 Top 5 Matches:")
    top_matches = matcher.get_matches(input_name, top_k=5)
    for name, score in top_matches:
        print(f"- {name} (Score: {round(score, 4)})")

if __name__ == "__main__":
    main()
