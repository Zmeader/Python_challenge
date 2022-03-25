#Pull in the CSV DAta
import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

#Establish the variables
total_votes = 0
voter_percent = []
candidates = []
total_votecount = []
percent_per_candidate = []
Winner_votes = 0


print("Election Results")
print("--------------------------------")


#create for loop to read through the data
with open(election_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csv_reader)

    for row in csv_reader:
        
        #Calculate the total number of votes
        total_votes += 1
        #add to the list of candidates
        if row[2] not in candidates:
            candidates.append(row[2])
            total_votecount.append(1)
        else:
            #caculate the total if it is the same individual
            candidateindex = candidates.index(row[2])
            total_votecount[candidateindex] += 1

#print the outputs you have so far
print("Total Votes: " + str(total_votes))
print("---------------------------------")


#create a loop to go through each vote to add to the percent totals
for i in range(len(total_votecount)):
    voter_percent.append(total_votecount[i]/total_votes)
    #
    if total_votecount[i] > Winner_votes:

        Winner_votes = total_votecount[i]

        Overall_winner = candidates[i]



#print each variable needed
print(candidates[0] + ": " + str(voter_percent[0])+ "% (" + str(total_votecount[0]) + ")" )
print(candidates[1] + ": " + str(voter_percent[1]) + "% (" + str(total_votecount[1]) + ")" )
print(candidates[2] + ": " + str(voter_percent[2]) + "% (" + str(total_votecount[2]) + ")" )
print("----------------------------------")
print("Winner: " + Overall_winner)        
print("----------------------------------")       

#export the information into a text file
pypoll_output = os.path.join("Analysis" , "pypoll_output.txt")
with open(pypoll_output, "w") as output:
    output.write("Election Results\n")
    output.write("--------------------------------\n")
    output.write("Total Votes: " + str(total_votes))
    output.write('\n')
    output.write("--------------------------------\n")
    output.write(candidates[0] + ": " + str(voter_percent[0]) + "% (" + str(total_votecount[0]) + ")" )
    output.write('\n')
    output.write(candidates[1] + ": " + str(voter_percent[1]) + "% (" + str(total_votecount[1]) + ")" )
    output.write('\n')
    output.write(candidates[2] + ": " + str(voter_percent[2]) + "% (" + str(total_votecount[2]) + ")" )
    output.write('\n')
    output.write("--------------------------------\n")
    output.write("Winner: " + Overall_winner)
    output.write('\n')
    output.write("--------------------------------\n")
