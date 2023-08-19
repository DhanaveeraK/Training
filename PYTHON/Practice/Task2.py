from thefuzz import fuzz

string1 = "apple"
string2 = "appel"
similarity_ratio = fuzz.ratio(string1, string2)
print(similarity_ratio) 

#output:-80