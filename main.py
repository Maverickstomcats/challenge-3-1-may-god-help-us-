# fork this challenge to your own repl
#share this challenge with another person in the room.
# Jesus, Janette, Melanie, Monica 
#"Dread from it, Run from it, destiny still arrives the same - Thanos "
#Day 3 Python Challenge

# The task is as follows: You are going to create a program that first asks the user to enter text. It can be any text, an entire article, a paragraph, a sentence, a poem, whatever you want. Then the program will ask the user to enter three random letters. From that moment on, our code is going to process that information and result in five different types of analysis:
text= input("Enter a text:") 
randomLetter = input("choose a random letter:")
randomLetter2= input("choose second random letter:")
randomLetter3= input("choose one more random letter:")
list=[randomLetter, randomLetter2, randomLetter3]
#do upper and lower - J.C
print(len(text)) #answer to no.2 

# 1. How many times each of those letters they have chosen appears. To achieve this, I advise you to store those letters in a list, and then use a method of strings that allows you to count how many times a substring appears within the string. One thing to keep in mind is that when searching for letters, there can be upper and lower case and this will affect the result. So, to make sure that absolutely all letters are counted, you should pass both the original text and the letters to be searched to lowercase.
print(text.count(randomLetter))
print(text.count(randomLetter2))
print(text.count(randomLetter3))
print(text.lower()) #built in method thingy
print(text.upper())
# 2. How many words are in the whole text? To achieve this part, remember that there is a string method that allows us to transform it into a list. And then there is a function that allows us to find out the length of a list. 
list2= (text.split(" "))  
print(list2) #it works :) 
print(len(list2))
# 3. What are the first and last letters of the text? Here, we will clearly use indexing.
print(text[-1]) #do we want to include characters or letters? 
print(text[0]) #this should be good don't worry too much about that :) 
# 4. The system will show us how the text would look like if we inverted the order of the words. Is there any method that allows us to invert the order of a list? And another one that allows us to join these elements with spaces in between?
text_reversed = text[::-1]
print(text_reversed)
list.reverse() #my bad on that part 
print(list)
# 5. The system will tell us if the word “python” is inside the text. This part can be a bit complicated to imagine, but I'll give you a hint: you can use Booleans to make your enquiry and a dictionary to find ways to express your answer.
special_word = "python"
word_insentence = special_word in text
print(word_insentence)

