# Install packages
import csv
from openai import OpenAI

# Function for generating the content
def generate_content(api_key, input_csv_path, output_txt_path):

    # API KEY for accessing the OPENAI model
    client = OpenAI(api_key=api_key)

    # creating an empty dictionary to store the word and count value from the csv
    word_count_dict = {}
    with open(input_csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            word_count_dict[row[0]] = int(row[1])

    # asking the user for the type of content that needs to be generated
    user_input = input("Enter the type of content you want to generate: ")

    # combining the prompt with the user input and the word, count dictionary
    prompt = f"Generate {user_input} based on the following words and counts:\n"
    for word, count in word_count_dict.items():
        prompt += f"{word} ({count}), "
    
    # passing the prompt to the chat completion model to generate the respone
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="gpt-3.5-turbo",
    )

    # storing the message content alone from the API response
    generated_content = response.choices[0].message.content

    # writing the generated content in a new ".txt" file
    with open(output_txt_path, 'w', encoding='utf-8') as output_file:
        output_file.write(generated_content)

    print(f"Content generated and written to '{output_txt_path}'")