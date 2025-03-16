# Cold-Email-Generator-Gen-AI
Generates emails based on the job profile extracted from the given link. A working app using Streamlit is an end product where a user can provide a link as input and will get an email as an output.

The project uses Langchain, Chromadb, and Llama-3.3-70b-versatile models for carrying out this project.

A simple overview of what is happening in this project is :
I extracted the Job description using Langchain which uses the Llama-3.3-70b-versatile model to extract the job role, description, and skills in JSON using "JsonOutputParser" by the Langchain community.
I use a dummy CSV file with skills and links consisting of links to projects related to those skills.
Chromadb(Vector database): stored skills and portfolio related to those skills
Used the LLm model to generate the cold email.
