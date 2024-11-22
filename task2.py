from fastapi import FastAPI # Import FastAPI framework
from fastapi.responses import PlainTextResponse  # Import PlainTextResponse

# Create an instance of the FastAPI class
app = FastAPI()

# Define a GET route at '/greet'
@app.get('/greet')

def greeting(greeting: str = "Hello", name: str = "Lheendah"):
     
    
    # return ({"greeting": f"{greeting}, {name}!"})
    return f"{greeting}, {name}! Congratulations, you have successfully completed the basic FastAPI task"

"""
    A simple endpoint to generate a dynamic greeting message.

    Query Parameters:
    - greeting (str): The greeting text (e.g., "Hi", "Welcome").
    - name (str): The name to greet.

    Returns:
    - JSON: A dictionary with the personalized greeting message.
"""
     
    # Return a JSON response with the greeting and name


