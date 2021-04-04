# https://cses.fi/problemset/task/1084

def appartmentCount(applicants, appartments, difference, applicantsCount, appartmentsCount):
    count = 0

    applicants = sorted(applicants)   # i
    appartments = sorted(appartments) # j

    i = 0
    j = 0

    while i < applicantsCount and j < appartmentsCount:

        appartment = appartments[j]
        applicant = applicants[i]

        if applicant - differnce > appartment:
            # appartment skip
            j += 1
            continue

        if applicant + differnce < appartment:
            # applicant skip
            i += 1
            continue


        count += 1
        j += 1
        i += 1

    return count


applicantsCount, appartmentsCount, differnce = map(int, input().split())
applicants = list(map(int, input("").split()))
appartments = list(map(int, input("").split()))
print(appartmentCount(applicants, appartments, differnce, applicantsCount, appartmentsCount))