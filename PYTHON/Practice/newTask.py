#SPACY:-- 
# import spacy

# nlp = spacy.blank("en")

# doc = nlp ("Hello world !")
# for token in doc:
#   print(token.text)      
  
# token = doc[1]
# print(token.text)

# #Span object:-
# # doc = nlp("Hello world!")  
# span = doc[1:3]
# print(span.text)
# # Lexical attributes:-
# doc = nlp("It costs $5.")

# print("Index: ", [token.i for token in doc]) 
# print("Text:  ", [token.text for token in doc])

# print("is_alpha:", [token.is_alpha for token in doc])
# print("is_punct:", [token.is_punct for token in doc])
# print("like_num:", [token.like_num for token in doc])

# # Getting Started:-
# # 1)
# # Import spaCy
# import spacy

# # Create the English nlp object
# nlp = spacy.blank("en")

# # Process a text
# doc = nlp("This is a sentence.")

# # Print the document text
# print(doc.text)
# # 2)
# # Import spaCy
# import spacy

# # Create the German nlp object
# nlp = spacy.blank("de")

# # Process a text (this is German for: "Kind regards!")
# doc = nlp("Liebe Grüße!")

# # Print the document text
# print(doc.text)
# # 3)
# # Import spaCy
# import spacy

# # Create the Spanish nlp object
# nlp = spacy.blank("es")

# # Process a text (this is Spanish for: "How are you?")
# doc = nlp("¿Cómo estás?")

# # Print the document text
# print(doc.text)
# # 4)
# # Import spaCy and create the English nlp object
# import spacy

# nlp = spacy.blank("en")

# # Process the text
# doc = nlp("I like tree kangaroos and narwhals.")

# # Select the first token
# first_token = doc[0]

# # Print the first token's text
# print(first_token.text)
# # 5)
# # Import spaCy and create the English nlp object
# import spacy

# nlp = spacy.blank("en")

# # Process the text
# doc = nlp("I like tree kangaroos and narwhals.")

# # A slice of the Doc for "tree kangaroos"
# tree_kangaroos = doc[2:4]
# print(tree_kangaroos.text)

# # A slice of the Doc for "tree kangaroos and narwhals" (without the ".")
# tree_kangaroos_and_narwhals = doc[2:6]
# print(tree_kangaroos_and_narwhals.text)
# # 6)
# import spacy

# nlp = spacy.blank("en")

# # Process the text
# doc = nlp(
#     "In 1990, more than 60% of people in East Asia were in extreme poverty. "
#     "Now less than 4% are."
# )

# # Iterate over the tokens in the doc
# for token in doc:
#     # Check if the token resembles a number
#     if token.like_num:
#         # Get the next token in the document
#         next_token = doc[token.i + 1]
#         # Check if the next token's text equals "%"
#         if next_token.text == "%":
#             print("Percentage found:", token.text)
            
# # 7)
# import spacy

# nlp = spacy.blank("en")

# # Process the text
# doc = nlp(
#     "In 1990, more than 60% of people in East Asia were in extreme poverty. "
#     "Now less than 4% are."
# )

# # Iterate over the tokens in the doc
# for token in doc:
#     # Check if the token resembles a number
#     if token.like_num:
#         # Get the next token in the document
#         next_token = doc[token.i + 1]
#         # Check if the next token's text equals "%"
#         if next_token.text == "%":
#             print("Percentage found:", token.text)
            
            
# # 8)
#              # Trained pipelines
# # # Trained pipelines
# # What are trained pipelines?
# # Models that enable spaCy to predict linguistic attributes in context
# # Part-of-speech tags
# # Syntactic dependencies
# # Named entities
# # Trained on labeled example texts
# # Can be updated with more examples to fin

# # #i)
# # Pipeline Packages:-

# # Q)A package with the label en_core_web_sm
# # $ python -m spacy download en_core_web_sm

# import spacy
# nlp = spacy.load("en_core_web_sm")

# # Binary weights
# # Vocabulary
# # Meta information
# # Configuration file

# # ii)Predicting Part-of-speech Tags:-

# import spacy

# # Load the small English pipeline
# nlp = spacy.load("en_core_web_sm")

# # Process a text
# doc = nlp("She eat the pizza")

# # Iterate over the tokens
# for token in doc:
#     # Print the text and the predicted part-of-speech tag
#     print(token.text, token.pos_)
  
# #   #2)Predicting Syntactic Dependencies:------------
# # for token in doc:
# #     print(token.text , token.pos_ ) 
    
      
import spacy

# Create the English nlp object
nlp = spacy.blank("en")

# Process a text
doc = nlp("This is a sentence.")

# Print the document text
print(doc.text)