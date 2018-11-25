# Given an array of the numbers of votes given to each of the candidates so far, and an integer k equal to the number of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win the election.


def elections_winners(votes, k):
    current = max(votes)
    runners = 0
    if k == 0:
        if votes.count(current) > 1:
            return 0
        else:
            return 1

    for cand in votes:
        if cand + k > current:
            runners += 1

    return runners 



print(elections_winners([5, 1, 3, 4, 1],0)) #,1)