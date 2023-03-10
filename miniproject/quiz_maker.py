from random import choice
import random

print("**********welcome to the quiz*********")
x=str(input("****type your name here*****\n"))
print("#######################")
print("hello",x)
print("#######################")

class Question:
     def __init__(self,prompt,answer):
            self.prompt = prompt
            self.answer = answer
         
            
            
question_prompts =open ("andy.txt", "r") 
content = question_prompts.read()


questions = [
    Question(content[1:355],"a"),
    Question(content[355:684],"b"),
    Question(content[684:1019],"c"),
    Question(content[1019:1259],"a"),
    Question(content[1259:1541],"a"),
    Question(content[1541:2008],"b"),
    Question(content[2008:2355],"a"),
    Question(content[2355:2679],"c"),
    Question(content[2679:2891],"c"),
    Question(content[2891:3289],"b"), 
]                          
random.shuffle(questions)
             

def run_quiz(questions):
    score=0
    for question in questions:
        answer= input(question.prompt)
        if answer == question.answer:
             score += 1
    print(x,"you got", score, "out of", len(questions))
run_quiz(questions) 

# OUTPUT
# **********welcome to the quiz*********
# ****type your name here*****
# jiban 
# #######################
# hello jiban
# #######################
# Define: Monoybrids
#     a) the trait that appears in the offspring of pure-breeding parental strains with antagonistic phenotypes
#     b) the science of heredity
#     c) individuals having two different alleles for a single trait
#     d) the way genes transmit physiological and behavioural traits from parents to offspring

# Q. c
# Define: Genotype
#     a) traits which show intermediary forms
#     b) the actual alleles present in an individual
#     c) the probability of two or more independent events occuring together is the product of their probabilities
#     d) "either-or" traits with no intermediary forms

# Q. b
# Define: Genetics
#     a) traits which show intermediary forms
#     b) offspring of genetically dissimilar parents
#     c) the science of heredity
#     d) the way genes transmit physiological and behavioural traits from parents to offspring

# Q. a
# Define: Continuous traits
#     a) "either-or" traits with no intermediary forms
#     b) the basic units of biological information
#     c) traits which show intermediary forms
#     d) an observable characteristic

# Q. d
# . Define: Discrete traits
#     a) the trait that remains hidden in the offspring of pure-breeding parental strains with antagonistic phenotypes
#     b) traits which show intermediary forms
#     c) "either-or" traits with no intermediary forms
#     d) the trait that appears in the offspring of pure-breeding parental strains with antagonistic phenotypes

# Q. c
# Define: Dominant trait
#     a) two alleles for a trait separate during gamete formation then reunite randomly at fertilization
#     b) the trait that remains hidden in the offspring of pure-breeding parental strains with antagonistic phenotypes
#     c) the trait that appears in the offspring of pure-breeding parental strains with antagonistic phenotypes
#     d) families producing offspring carrying specific parental traits that remain constant across generations

# Q. b
# Define: Phenotype
#     a) the trait that remains hidden in the offspring of pure-breeding parental strains with antagonistic phenotypes
#     b) the trait that appears in the offspring of pure-breeding parental strains with antagonistic phenotypes
#     c) the probability of two or more independent events occuring together is the product of their probabilities
#     d) an observable characteristica
# Define: Heredity
#     a) the way genes transmit physiological and behavioural traits from parents to offspring
#     b) individuals having two different alleles for a single trait
#     c) cross between parents differing only in one trait
#     d) the probability of either of two mutually exclusive events occuring is the sum of their probabilities

# Q. d
# Define: Pure-breeding lines
#     a) an observable characteristic
#     b) families producing offspring carrying specific parental traits that remain constant across generations
#     c) the probability of two or more independent events occuring together is the product of their probabilities
#     d) traits which show intermediary forms

# Q. c
# Define: Sum rule
#     a) the probability of either of two mutually exclusive events occuring is the sum of their probabilities
#     b) the trait that remains hidden in the offspring of pure-breeding parental strains with antagonistic phenotypes
#     c) offspring of genetically dissimilar parents
#     d) the science of heredity

# Q. b
# jiban you got 5 out of 10