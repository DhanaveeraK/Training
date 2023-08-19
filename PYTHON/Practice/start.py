# # def common_characters(str1, str2):
# #     common_chars = set(str1) & set(str2)
# #     return common_chars

# # def calculate_similarity(string1, string2):
# #     total_characters = set(string1) | set(string2)
# #     similarity = len(common_chars_set) / len(total_characters)
# #     return similarity

# # string1 = "hejfdjsakllo"
# # string2 = "hoamafkalkdlakla"

# # common_chars_set = common_characters(string1, string2)
# # print("Common characters:", common_chars_set)  

# # similarity = calculate_similarity(string1, string2)
# # print("Similarity:", similarity)
# #------------------------------------------------------
# #1)String Similarity:- using fuzzywuzzy
# from thefuzz import fuzz

# string1 = "apple"
# string2 = "appel"
# similarity_ratio = fuzz.ratio(string1, string2)
# print(similarity_ratio) 

# #----------------------------------------
# #2) numeric similarity:

# # from sklearn.metrics.pairwise import cosine_similarity
# # import numpy as np

# # vector1 = np.array([1, 2, 3])
# # vector2 = np.array([3, 4, 5])
# # similarity = cosine_similarity(vector1.reshape(1, -1), vector2.reshape(1, -1))
# # print(similarity)


# #----------------------------------------------------

# lst=[12,32,54,5,76]
# print(type(lst))

# T=(25,43,54,22,33,66)
# print(type(T))

# s={'kkk','ddd','ddaaa','swww'}
# print(type(s))

# str="kdnsk"
# print(type(str))

# range(12)
# print(list(range(0,12,3))) 

# print(list(range(12)))

# d={'dhana':'Mech','ome':'EEE','bharagav':"ECE",'irfan':'Mech'}
# print(d)
# print(d.values())
# print(d.keys())
# print(d['dhana'])

# #OPERATORS:--
#  #1)Arithmetic operators:-
# x=2
# y=3
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# #2)Assigement Operators:-
# a,b=5,6
# print(a+b)
# #3)unary Operator:-change to negative
# a =- a
# print(a)

# #4)Relatonal Operators:-

# a= 12
# b =12

# print(a== b)
# print(a<= b)
# print(a>= b)
# print(a!= b)

# # #5)Logical Operators:-

# D=5
# M=4   
# print(D<8 and M<5)
# print(D<8 or M<5)

# print(not M)

# # Binary :- converting Decimal to Binay
# # print(bin (25)) 
# # #//output:- 0b11001
# print(bin(42))

# print(0b110)

# # print(0b11001)

# # octal:-
# # print(oct(32))
# # # //output:-0o40

# print(oct(35))
# print(0o65)

# # # HEXA Decimal:-
# # print(hex(11))
# print(hex(15))

# print(0xf)
  
#swap two variable:-
# a=5
# b=6
# .1)
# temp=a
# a=b
# b=temp

# 2)
# a=a+b
# b=a-b
# a=a-b

# 3)xor:-not waste the extra bits
# a=a^b
# b=a^b
# a=a^b

# Bit Wise Operators:-
# print(~12)

# # bit wise in using "&,|"

# print(12&13)
# print(12|13)
# print(24&25)
# print(25^54)
# Imporant math functions:-

# import math
# print(math.floor(25))
# # //output:- low value 
# print (math.sqrt(32))
# print(math.ceil(23))
# # //outpt:-high value
# print(math.pow(3,2))
# print(math.pi)

# alives con:-
# import math as m
# print(m.sqrt(32))

# from math  import sqrt, log 

# print(log(12))
# print(sqrt(12))
# print(help('math'))

# if conditions:-


# #Coding:----------------------
# import random

# # List of team members
# team_members = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Isaac", "Jack"]

# # Initialize an empty dictionary to store member scores
# member_scores = {member: {"Python": 0, "React": 0, "MongoDB": 0} for member in team_members}

# # Function to assign random scores to a subject
# def assign_random_scores(scores_dict):
#     for member in scores_dict:
#         scores_dict[member]["Python"] = random.randint(0, 100)
#         scores_dict[member]["React"] = random.randint(0, 100)
#         scores_dict[member]["MongoDB"] = random.randint(0, 100)

# # Assign random scores for each subject to each member
# assign_random_scores(member_scores)

# # Function to calculate the total score for a member
# def calculate_total_score(scores):
#     return scores["Python"] + scores["React"] + scores["MongoDB"]

# # Calculate total scores for each member and store in a dictionary
# total_scores = {member: calculate_total_score(scores) for member, scores in member_scores.items()}

# # Find top and bottom 5 members based on total scores
# top_5 = sorted(total_scores.items(), key=lambda x: x[1], reverse=True)[:5]
# bottom_5 = sorted(total_scores.items(), key=lambda x: x[1])[:5]

# # Print the top and bottom 5 members
# print("Top 5 members:")
# for member, total_score in top_5:
#     print(f"{member}: {total_score}")

# print("\nBottom 5 members:")
# for member, total_score in bottom_5:
#     print(f"{member}: {total_score}")



Team_Members = [
    {
             'Name':'Dhanaveera',
             'Branch':'B.tech',
             'score':{'python':90, 'js':78 ,'MangoDB':66}
    },
    {
             'name':'Raju',
             'Branch':'B.com',
             'score':{'python':89, 'js':56 ,'MangoDB':90}
    },
    {          
             'name':'Malcha',
             'Branch':'B.Tech',
             'score':{'python':78, 'js':64 ,'MangoDB':66}
        
    },
    {        'name':'Nabi',
             'Branch':'Inter',
             'Score':{'python':70, 'js':93 ,'MangoDB':59}
        
    },
    {       
             'name':'vijaya',
             'Branch':'B.Tech',
             'Score':{'python':52, 'js':48 ,'MangoDB':86}
        
    },
    {           
              'name':'Sathish',
              'Branch':'B.ed',
              'Score': {'python':35, 'js':68 ,'MangoDB':56}
        
    },
    {         'name':'Durga',
               'Branch':'B.Tech',
               'Score':{'python':79, 'js':48 ,'MangoDB':49}
               
    },
    {          'name':'Bhargav',
                'Branch':'B.Tech',
                'Score':{'python':44, 'js':69 ,'MangoDB':80}
               
    },
    {           'name':'Siri',
                'Branch':'B.Tech',
                'Score':{'python':80, 'js':45 ,'MangoDB':79}
          
    },
    {
                 'name':'prabha',
                 'Branch':'B.Tech',
                 'Score':{'python':45, 'js':76 ,'MangoDB':56}
    }
]

previous_member = None

for member in Team_Members:
    if previous_member:
        # Assign a 'react' score to each member (assuming it's 70 for demonstration)
        react_score = 70
        member['score']['react'] = react_score

        # Add 'react' score to the previous member's 'js' score
        previous_member['score']['js'] += react_score

    previous_member = member

# Print the updated Team_Members list
for member in Team_Members:
    print(member)