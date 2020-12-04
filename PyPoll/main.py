#import modules
import os
import csv

#set path for csv file
csvpath = os.path.join("Desktop", "GitHub", "python_challenge", "PyPoll", "Resources", "election_data.csv")

#open csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)

    #lists
    total_votes = []
    list_candidates = []
    candidates = []
    
    #lists for each candidate
    khan_votes = []
    correy_votes = []
    li_votes = []
    otooley_votes = []

    csv_header = next(csvreader)
    print(csv_header)

    for row in csvreader:
        #total_votes list 
        total_votes.append(row[0])
    
        #list of candidates
        candidates.append(row[2])
    
    for candidate in candidates:
    #get unique values from candidates list
        if candidate not in list_candidates:
            list_candidates.append(candidate)
        #append each name from candidates list to new list 
        if candidate == "Khan":
            khan_votes.append(candidates)
            khan_total = (len(khan_votes))
        if candidate == "Correy":
            correy_votes.append(candidates)
            correy_total = (len(correy_votes))
        if candidate == "Li":
            li_votes.append(candidates)
            li_total = (len(li_votes))
        if candidate == "O'Tooley":
            otooley_votes.append(candidates)
            otooley_total = (len(otooley_votes))
        
        #percentage for each 
            khan_percent = "{:.2%}".format(khan_total / (len(total_votes)))
            correy_percent = "{:.2%}".format(correy_total / (len(total_votes))) 
            li_percent = "{:.2%}".format(li_total / (len(total_votes)))
            otooley_percent = "{:.2%}".format(otooley_total / (len(total_votes))) 
        
        #winner
            if khan_total > max(correy_total, li_total, otooley_total):
                winner = "Khan"
            if correy_total > max(khan_total, li_total, otooley_total):
                winner = "Correy"
            if li_total > max(correy_total, khan_total, otooley_total):
                winner = "Li"
            if otooley_total > max(correy_total, li_total, khan_total):
                winner = "O'Tooley"
    '''check values
    print(list_candidates)
    print(len(total_votes))

    print(khan_total)
    print(correy_total)
    print(li_total)
    print(otooley_total)

    print(khan_percent)
    print(correy_percent)
    print(li_percent)
    print(otooley_percent)

    print(winner)
    '''

    print("Election Results")
    print("-----------------------")
    print("Total Votes: ", (len(total_votes)))
    print("-----------------------")
    print((list_candidates[0]), ":", (khan_percent), (khan_total))
    print((list_candidates[1]), ":", (correy_percent), (correy_total))
    print((list_candidates[2]), ":", (li_percent), (li_total))
    print((list_candidates[3]), ":", (otooley_percent), (otooley_total))
    print("-----------------------")
    print("Winner: ", (winner))
    print("-----------------------")

    


