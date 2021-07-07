import os
import csv

csv_path = os.path.join('PyPoll','election_data.csv')

with open(csv_path, 'r') as csv_file:

    # Split the data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')

    header = next(csv_reader)
    vote_counter = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    o_tooley_votes = 0
    khan_pct = 0
    correy_pct = 0
    li_pct = 0
    o_tooley_pct = 0
    for row in csv_reader:
        vote_counter +=1
        candidate=str(row[2])
        if (candidate) == "O'Tooley":
            o_tooley_votes +=1
        if (candidate) == "Khan":
            khan_votes +=1
        if (candidate) == "Li":
            li_votes +=1
        if (candidate) == "Correy":
            correy_votes +=1


    correy_pct = round((correy_votes/vote_counter)*100)
    li_pct = round((li_votes/vote_counter)*100,3)
    o_tooley_pct = round((o_tooley_votes/vote_counter)*100,3)
    khan_pct = round((khan_votes/vote_counter*100),3)




print("Election Results")
print('-----------------------------')
print(f"Total Votes: {vote_counter}")
print("------------------------------")
print(f"Khan: {khan_pct,khan_votes}")
print(f"Correy: {correy_pct, correy_votes}")
print(f"Li: {li_pct, li_votes}")
print(f"O'Tooley: {o_tooley_pct, o_tooley_votes}")
print('-----------------------------')
print('Winner:Khan')


#Output Results
output= os.path.join('Results.txt')
with open(output, 'w') as text:

    text.write("Election Results"  +'\n')
    text.write('-----------------------------' +'\n')
    text.write(f"Total Votes: {vote_counter}" +'\n')
    text.write("------------------------------" +'\n')
    text.write(f"Khan: {khan_pct,khan_votes}" +'\n')
    text.write(f"Correy: {correy_pct, correy_votes}" +'\n')
    text.write(f"Li: {li_pct, li_votes}")
    text.write(f"O'Tooley: {o_tooley_pct, o_tooley_votes}" +'\n')
    text.write('-----------------------------' +'\n')
    text.write('Winner:Khan' +'\n')
