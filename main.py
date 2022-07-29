def reciprocal_sum(a: int, b: int) -> float:
    sum = 0
    for i in range(a, b+1):
        sum += 1/i
    return sum

def prob_of_successful_episode(n: int) -> float:
    prob_of_failed_episode = reciprocal_sum(n // 2 + 1, n)
    return 1 - prob_of_failed_episode

def limit_for_prob_of_successful_episode(a=2, b=8, limit_threshold=0.000001) -> float:
    n_values = [10 ** i for i in range(a, b)]
    final_probs = []
    for number_of_prisoners in n_values:
        final_probs.append(prob_of_successful_episode(number_of_prisoners))
    print(f"n = {n_values}")
    print(f"probs = {final_probs}")
    for i in range(1, len(final_probs)):
        if abs(final_probs[i] - final_probs[i - 1]) < limit_threshold:
            print(f"limit for probability as n tends to infinity is approx. {final_probs[-1]}")
            return final_probs[-1]
        if i == len(final_probs) - 1:
            print("Try larger n or smaller threshold to increase accuracy of limit")
    return -1.0

if __name__ == '__main__':
    n = 1000  # number of prisoners, boxes, and slips
    print(reciprocal_sum(1,10000000))
