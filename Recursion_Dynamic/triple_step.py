import sys

def CountSteps(n):
    n = int(n)
    memo = [-1] * (n+1)
    return CountStepsH(n, memo)
    


def CountStepsH(n, memo):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = CountStepsH(n-1, memo) + CountStepsH(n-2, memo) + CountStepsH(n-3, memo)
    return memo[n]


def main():
    print(CountSteps(sys.argv[1]))


if __name__ == "__main__":
    main()