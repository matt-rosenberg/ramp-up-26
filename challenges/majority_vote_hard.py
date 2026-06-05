def majority_vote(votes):
    candidates = set(votes)
    for x in candidates:
        if votes.count(x) > len(votes) / 2:
            return x
    return None

def main():
    print(majority_vote(['a', 'a', 'a', 'a', 'b', 'c', 'd']))

if __name__ == "__main__":
    main()