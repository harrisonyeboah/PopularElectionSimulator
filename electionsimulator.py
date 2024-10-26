import matplotlib.pyplot as pyplot
import random

'''
This program will run a simulation through 
all 50 States starting from Alabama to Wyoming 
through randomization of probabilities in each state.

Author: Harrison Kromoh Yeboah
'''

def officialSimulation(probsEachState, statePopulation):
    totalVotes = 0 
    TrumpVotes = 0 
    KamalaVotes = 0
    listOfTrumpVotes = []
    listOfKamalVotes = []

    for state in range(len(probsEachState)):
        populationInState = statePopulation[state]
        probInState = probsEachState[state]

        for _ in range(populationInState):
            randomProcess = random.random()
            if randomProcess <= probInState:
                TrumpVotes += 1
                listOfTrumpVotes.append(TrumpVotes)
                listOfKamalVotes.append(KamalaVotes)  # KamalaVotes stays the same
            else:
                KamalaVotes += 1
                listOfKamalVotes.append(KamalaVotes)
                listOfTrumpVotes.append(TrumpVotes)  # TrumpVotes stays the same

        totalVotes += populationInState

    # Plot results after all states are processed
    pyplot.plot(range(len(listOfTrumpVotes)), listOfTrumpVotes, label='Trump Votes')
    pyplot.plot(range(len(listOfKamalVotes)), listOfKamalVotes, label='Kamala Votes')

    pyplot.xlabel("Total Votes (Cumulative)")
    pyplot.ylabel("Number of Votes * 100")
    pyplot.title("Vote Distribution from Alabama to Wyoming")
    pyplot.legend()
    pyplot.show()
   
    # Output results
    print(f"Total Trump Votes: {TrumpVotes}")
    print(f"Total Kamala Votes: {KamalaVotes}")
    print(f"Total Votes: {totalVotes}")

def main():
    stateNames = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut',
                  'Delaware','District of Columbia','Florida','Georgia','Hawaii','Idaho',
                  'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine',
                  'Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri',
                  'Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico',
                  'New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon',
                  'Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee',
                  'Texas','Utah','Vermont','Virginia','Washington','West Virginia',
                  'Wisconsin','Wyoming']

    stateRepublicanProb = [.585, .535, .505, .54, .405, .495, .41, .375, .185, .465,
                            .50, .38, .585, .425, .52, .505, .575, .505, .49, .445, 
                            .38, .355, .435, .465, .51, .5, .595, .555, .46, .45, 
                            .395, .445, .375, .495, .59, .51, .525, .425, .465, .41, 
                            .52, .58, .555, .495, .62, .36, .52, .445, .51, .5, 
                            .66]

    statePopulation = [5024, 733, 7151, 3011, 39538, 5773, 3606, 990, 690, 21538, 
                       10711, 1455, 1839, 12812, 6785, 3190, 2937, 4506, 4658, 1362,
                       6177, 7030, 10077, 5706, 2961, 6154, 1084, 1961, 3104, 1378, 
                       9289, 2117, 20201, 10439, 779, 11799, 3959, 4237, 13002, 1097, 
                       5118, 886, 6910, 29145, 3271, 643, 8631, 7705, 1794, 5894, 
                       577]
        
    officialSimulation(stateRepublicanProb, statePopulation)

main()
