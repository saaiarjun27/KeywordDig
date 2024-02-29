# Install packages
from dotenv import load_dotenv
import os
import tkinter as tk

# Import Functions
from functions.Selenium_Search import google_search
from functions.Keyword_Count import keyword_count
from functions.Keyword_Chart import keyword_chart
from functions.OpenAI_Content import generate_content
from functions.Output_Path import open_file_dialog_box

# Execute the function to load the env from the .env file
load_dotenv()

# Main Function
if __name__ == "__main__":

    # for tkinter to open the file  explorer dialog box and close
    root = tk.Tk()
    root.withdraw()

    # for storing the generated words and it's count
    input_csv_path = 'output.csv' 

    # Input the keyword to search on Bing
    search_keyword = input("Enter the search keyword: ")

    # Input the output file name
    output_file_name = "SERP.csv"

    # Executing the search function
    google_search(search_keyword, output_file_name)

    # Executing the count function
    keyword_count(output_file_name)

    # Executing the Bokeh chart function
    keyword_chart()

    # Asking the user whether they'd like to generate AI content for the generated keywords
    user_input = input("Do you want an AI generated content for these generated keywords? (yes/no): ")

    # API key for OPENAI to generate the content
    open_ai_api_key = os.getenv('OPENAI_API_KEY')

    # If yes, the generate content function will execute, else nope!
    if user_input.lower() == "yes":
        # for storing the AI generated content using OPENAI
        output_txt_path = open_file_dialog_box(default_extension = ".docx")
    
        generate_content(open_ai_api_key, input_csv_path, output_txt_path)
    else:
        print("Quitting the program.")