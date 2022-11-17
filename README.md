# Probability Calculator with a Deck of Cards
## Description
This is a probability calculator that calculates the probability that a certain configuration of cards will be picked from a full deck.

The program asks for input from user with regards to the card configuration. The configuration takes the form of a string

*example*: 3H 4S C 8 9D

*meaning*: 3 of Hearts, 4 of Spades, any face of the Club suit, 8 of any suit, 9 of Diamonds

If the length of the configuration is greater than 1, we ask the user if the order that the cards are picked matters.

If the order matters, we calculate the probability using the permutation formula: **nPr**

If the order does not matter, we calculate the probability using the combination formula: **nCr** 

*where **n** is the *total number of outcomes* and **r** is the *total number of desired outcomes*
## Usage
To use this program, clone the repository:
``
Run it on your terminal:
`python probability_calculator.py`
## Testing
To test the program on your terminal, use the command:
`pytest -v`

### ENJOY :)
