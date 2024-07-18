def count_words(text):
    """
    This function takes a string input and returns the number of words in the input.
    Words are considered as sequences of characters separated by whitespace.
    """
    # Splitting the input text by whitespace to get a list of words
    words = text.split()
    # Returning the length of the list which is the word count
    return len(words)

def main():
    """
    Main function to prompt user for input and display the word count.
    Includes error handling for empty input.
    """
    # Prompting the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ")
    
    # Checking if the input is empty
    if not user_input.strip():
        print("Error: You entered an empty input. Please try again.")
    else:
        # Counting the words in the input
        word_count = count_words(user_input)
        # Displaying the word count to the console
        print(f"Word Count: {word_count}")

# Running the main function
if _name_ == "_main_":
    main()
