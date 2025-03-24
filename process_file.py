#!/usr/bin/python3

def process_file():
    # Ask user for the filename
    input_filename = input("Enter the filename to read from: ")
    output_filename = "modified_" + input_filename

    try:
        # Try to open and read the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify content (example: convert text to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"✅ Successfully created '{output_filename}' with the modified content.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"❌ Error: Could not read the file '{input_filename}'.")
    except Exception as e:
        print(f"❌ Unexpected error occurred: {e}")

# Run the function
process_file()
