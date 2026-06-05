def cricket_balls_to_overs(balls):
    overs = balls // 6
    balls = balls % 6
    return overs + (balls / 10)

def main():
    print(cricket_balls_to_overs(428))

if __name__ == "__main__":
    main()