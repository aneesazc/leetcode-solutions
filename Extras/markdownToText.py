def markdown_to_text(doc_content):
    # Step 1: Split the content into individual lines
    lines = doc_content.split("\n")
    
    # Step 2: Remove heading markers and asterisks from words
    # 'map' applies the lambda function to each line, removing leading '#' and cleaning words
    new_lines = map(lambda line: remove_asterisks_from_words(line.lstrip("#")), lines)
    
    # Step 3: Rejoin the cleaned lines into a single text output
    return "\n".join(new_lines)  # Join the cleaned lines with newline characters


def remove_asterisks_from_words(line):
    # Step 1: Split the line into individual words
    words = line.split()  # Splitting into words to process each separately
    
    # Step 2: Define a function to clean asterisks from the start and end of words
    def clean_word(word):
        # If the word has single/double asterisks at both ends, strip them
        return word.strip("*") if len(word) > 1 else word
    
    # Step 3: Apply the cleaning function to all words and filter out empty results
    cleaned_words = filter(lambda word: len(word) > 0, map(clean_word, words))
    
    # Step 4: Rejoin the cleaned words into a single line
    return " ".join(cleaned_words)  # Rejoin the words with a space separator
