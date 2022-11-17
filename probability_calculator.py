import sys, math, time

suits = ['H', 'D', 'S', 'C']
faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J', 'A']
choice = "N"

def probability_calc(config):
    global suits
    global faces
    global choice
    numOfOutcomes = 52
    numOfDesiredOutcomes = 0

    #evaluate the configuration list
    config_len = len(config)
    if config_len > 0:
        for value in config:
            if len(value) > 1:
                numOfDesiredOutcomes += 1
            else:
                if value in suits:
                    numOfDesiredOutcomes += 13
                else:
                    numOfDesiredOutcomes += 4
        #ask user if order of cards matter if config_len is greater than 1
        if config_len > 1:
            choice = input("Does order of the cards matter? Type Y for yes or N for no: ").capitalize()
            if choice != "Y":
                #Combination
                print("Order does not matter...")
                time.sleep(1)
                print("Computing...")
                time.sleep(2)
                probability = math.factorial(numOfOutcomes) / (math.factorial(numOfOutcomes - numOfDesiredOutcomes) * math.factorial(numOfDesiredOutcomes))
            else:
                #Permutation
                print("Order matters...")
                time.sleep(1)
                print("Computing...")
                time.sleep(2)
                probability = math.factorial(numOfOutcomes) / math.factorial(numOfOutcomes - numOfDesiredOutcomes)
        else:
            probability = numOfDesiredOutcomes / numOfOutcomes
    return round(probability, 4)

def checker(config):
    #checks if each card value and suit exists
    global suits
    global faces
    error_msg = "Wrong Usage!\nPlease input a valid configuration or click CTRL-C to exit program"
    config_len = len(config)
    for idx in range(config_len):
        if len(config[idx]) == 2:
            letters = list(config[idx])
            for letter in letters:
                if letter in suits or letter in faces:
                    return True
        elif len(config[idx]) == 1:
            if config[idx] in suits or config[idx] in faces:
                return True
    print(error_msg)
    return False
        
def main():
    print("Welcome to Probability Calculation with a Deck of Cards!")
    time.sleep(2)
    print("Card configuration may look like: 3H KS 4 C 7D")
    time.sleep(2)
    print("These represent: 3 of Hearts, King of Spades, 4 of any suit, any value of Clubs, 7 of Diamonds")
    time.sleep(2)
    while True:
        config = None
        try:
            user_config = str(input("Enter the configuration of cards to find the probablity of them being picked: "))
            config = user_config.split(' ')
            response = checker(config)
            if response == True:
                result = probability_calc(config)
                break
            else:
                continue
        except KeyboardInterrupt:
            sys.exit()
    print("Probability of picking the card configuration {} is {}".format(config, result))    

if __name__ == "__main__":
    main()