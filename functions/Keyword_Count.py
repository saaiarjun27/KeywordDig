# Install packages
import pandas as pd
from collections import Counter
import re
from nltk.corpus import stopwords

# Executing the function to count the words in the SERP for SEO
def keyword_count(output_file_name):

    # Reading the csv using pandas
    df = pd.read_csv(output_file_name, encoding='latin1')
    df.columns = df.columns.str.strip()

    # Combining all the columns present in the data frame
    combined_text = ''
    for column in df.columns:
        if column.lower() != 'links':
            combined_text += ' '.join(df[column].astype(str)) + ' '

    # cleaning the text by removing the links and stopwords (such as and, is, the, was and etc)
    cleaned_text = re.sub(r'\b(?:http|\.com)\S*\b', '', combined_text)

    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', cleaned_text).lower()

    words = cleaned_text.split()

    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]

    # counting the words
    word_counts = Counter(filtered_words)

    # sorting the words in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # storing the words and counnt as two separate columns
    result_df = pd.DataFrame(sorted_word_counts, columns=['word', 'count'])

    # storing the result in the 'output.csv' file
    result_df.to_csv("output.csv", index=False)