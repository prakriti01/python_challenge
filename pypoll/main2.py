import os
import csv 


election_data = os.path.join("Resources", "election_data.csv") 
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    Total_vote=[]
    percentage_vote=[]
    candidate=["Khan","Correy","Li", "O'Tooley"]
    candidate_vote=[]
    Total= dict()
    winner= dict()
    x=[]

# The total number of votes cast
    for row in csvreader:
        Total_vote.append(row)
        candidate_vote.append(row[2])

    for id in Total:
      y = len(Total(i))

def per_vote(candidate):
    Total = int(candidate[1]) + int(candidate[2]) + int(candidate[3]) + int(candidate(4))

#The percentage of votes each candidate won
    khan = (int(candidate[1]) / Total ) * 100 
    correy = (int(candidate[2]) / Total ) * 100
    Li = (int(candidate[3]) / Total ) * 100
    Tooley = (int(candidate[4]) / Total )* 100

#for i in candidate_vote.append(row[2]):
#print(i)
       
#List of candidate who receive total vote percentage 
#for i in range(len(candidate_vote)):
        #percentage_vote.append(candidate_vote[i + 1]) 

    #candidate_vote = {"khan"}
    #candidate_vote = {"Correy"}
    #candidate_vote = {"li"}
    #candidate_vote = {"O'Tooley"} 
    #percentage_vote = len(row[2]) / Total_vote)

print("Election Result :")
print ("----------------------------")
#Total number of Votes :
print("Total Votes:" + str(len(Total_vote)))
print ("----------------------------")
print(str(k) + ":  %0.3f"% (y * 100.00/Total_vote) + (" +(x)+"))

#print(f"khan: {str(khan)}"+ str(len(candidate[1])))
#print("Khan:" + str(len(candidate[1])))
#print("Correy:" + str(len(candidate[2])))
#print("li:" + str(len(candidate[3])))
#print("O'Tooley:"+ str(len(candidate[4])))

#print("Khan:" + str(len(row[2])))
#print("Correy:" + str(len(row[2])))
#print("Li :" + str(len(row[2])))
#print("O'Tooley :" + str(len(row[2])))

#print(str(len(candidate_vote)))

 #if row[2] == candidate_vote:
    #print(row[2])  

#The winner of the election based on popular vote
print ("----------------------------")
print("WINNER :"+ str(max(candidate_vote)))
print ("----------------------------")
#print( Total_vote(row[2]))


        