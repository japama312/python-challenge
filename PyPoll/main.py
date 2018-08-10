import os
import csv



electiondataCSV = os.path.join("Resources", "election_data.csv")



votes = 0
candidate_list = []
candidate_votes = {}


with open(electiondataCSV) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:
        votes = votes + 1
              

        if row["Candidate"] not in candidate_list:
            
            candidate_list.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1
            
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1
    

    
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")
#results
    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    

#winner = 

