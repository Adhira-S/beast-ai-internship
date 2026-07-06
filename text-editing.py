def edit_text(input_file_path, output_file_path, old_string, new_string):
    """
    This function reads the content of a file, modifies it by replacing certain words,
    and saves the modified content to a new file.
    """
    # Opens the input file
    with open(input_file_path, "r") as file:
        text = file.read()

    # Checks if the old string exists
    if old_string not in text:
        print(
            f'"{old_string}" not found in the file. Please provide a valid string that exists in the file.'
        )
        return

    # Replaces the old string with the new string
    new_text = text.replace(old_string, new_string)

    # Adds extra text
    new_text = f"{new_text} I am learning programming languages."

    # Saves the modified content to the output file
    with open(output_file_path, "w") as file:
        file.write(new_text)

    print(f"{output_file_path} created!")


# Main program
if __name__ == "__main__":
    old_word = input("Enter the word you want to replace: ")
    new_word = input("Enter the new word: ")

    edit_text("input.txt", "output.txt", old_word, new_word)
