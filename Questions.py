import csv
import openai

# Function to generate questions using GPT
def generate_questions(blog_text):
    prompt = (
        f"Read this text [Blog] and come up with insightful, thought-provoking questions "
        f"for a Podcast interview with Rob May - 4x Founder. Multi-Stage Tech Investor. "
        f"100+ AI investments, Started Backupify, Talla, Dianthus, and BrandGuard. "
        f"Some big wins and some big failures. University of Kentucky grad and huge Wildcats fan. "
        f"GP at PJC for a while, now a Partner at Half Court Ventures, a fund that focuses on AI. "
        f"Co-Founder at the AI Innovators Community https://ai-innovators.com/. "
        f"I also write the Investing In AI newsletter at investinginai.substack.com and am an angel in 100+ early-stage companies, mostly AI companies. "
        f"Please don't contact me about anything crypto or blockchain.\n\n"
        f"Blog: {blog_text}\n\nQuestions:"
    )
    
    # Call to GPT to generate questions using the latest API format
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    
    questions = response.choices[0].message["content"]
    return questions.strip()

# Function to save blogs and questions to a new CSV file
def save_blogs_and_questions_to_csv(input_csv, output_csv="blogs_with_questions.csv"):
    with open(input_csv, 'r', encoding='utf-8') as infile, open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Read headers from the input file and add a new "Questions" column
        headers = next(reader)
        headers.append("Questions")
        writer.writerow(headers)
        
        # Iterate over each row in the input CSV, generate questions, and write to the output CSV
        for row in reader:
            url, content = row[0], row[1]
            print(f"Generating questions for {url}...")
            questions = generate_questions(content)
            writer.writerow([url, content, questions])
    
    print(f"Blogs and questions saved to {output_csv}")

# Main function
def main():
    """Main function"""
    # Set your OpenAI API key here
    openai.api_key = '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'
    
    # Path to the input CSV file with blogs
    input_csv = "blogs.csv"
    
    # Call the function to process the blogs and save the questions
    save_blogs_and_questions_to_csv(input_csv)

if __name__ == "__main__":
    main()
