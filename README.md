# resume-formatter
### Extract necessary data as a structured response from the provided resume.

## Working 
#### 1. Takes a resume as input
#### 2. Gets the unstructured resume text using PdfReader
#### 3. Defines a pydantic model as the structure
#### 4. Uses Gemini LLM API to extract the necessary info and derive any additional info required.
#### 5. Returns the response as a json in the structure defined in step 3.

## How to run?
#### 1. Add env variable: GEMINI_API_KEY and set value as your API key
#### 2. Replace resume.pdf with your input resume
#### 3. Make changes to response_structure to change structure of the LLM API response
#### 4  Run the main.py script
