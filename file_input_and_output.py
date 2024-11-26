def modify_file():
    # Ask user for input file and output file names
    input_filename = input("Enter the name of the input file: ")
    output_filename = input("Enter the name of the output file: ")

    try:
        # Open the input file for reading
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        # Modify the content (example: convert all text to uppercase)
        modified_content = content.upper()  # You can modify it as needed

        # Write the modified content to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"Modified content has been written to {output_filename}.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read or written to.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Call the function to run the program
modify_file()
