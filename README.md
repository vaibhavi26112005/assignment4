# assignment4
assignmemt 4 in python course

Task 1 – Read a File and Handle Errors
Objective:
This program attempts to open and read a file named sample.txt line by line, displaying each line with its line number. It also gracefully handles situations where the file does not exist or another unexpected error occurs.

Functionality:

File Reading:

Uses with open("sample.txt", "r") to safely open the file in read mode.

The with statement ensures the file is automatically closed after reading.

Line-by-Line Reading:

Uses enumerate(file, start=1) to get both the line number and the line text.

Uses .strip() to remove extra whitespace or newline characters before printing.

Error Handling:

FileNotFoundError: If sample.txt does not exist, it prints an error message instead of crashing.

Generic Exception: Any other unexpected error (e.g., permission issues) is caught and displayed.

Expected Behavior:

If sample.txt exists, it shows each line with a line number.

If sample.txt does not exist, it displays:
Error: The file 'sample.txt' was not found.
.............................................................................................................................................................

Task 2 – Write and Append Data to a File
Objective:
This program collects input from the user, writes it to a file named output.txt, appends additional user input, and finally displays the entire content of the file.

Functionality:

Write Data to File:

Asks the user for initial input (input() function).

Opens output.txt in write mode ("w"), which overwrites any existing content.

Writes the entered text to the file, adding a newline at the end ("\n").

Prints confirmation: "Data successfully written to output.txt."

Append Data to File:

Prompts the user for more text to add.

Opens output.txt in append mode ("a") so the new content is added without deleting existing data.

Writes the appended text with a newline.

Prints confirmation: "Data successfully appended."

Read Final Content:

Opens the file in read mode ("r") to view the updated file contents.

Prints everything to the screen exactly as stored in the file.

Expected Behavior:

First input replaces the existing file content.

Second input is added to the file without removing previous data.

Finally, the file’s complete content is displayed.
