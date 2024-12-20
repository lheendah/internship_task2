from fastapi import FastAPI # Import FastAPI framework
from fastapi.responses import PlainTextResponse  # Import PlainTextResponse

# Create an instance of the FastAPI class
app = FastAPI()

# Define a GET route at '/greet'
@app.get('/greet')

def greeting(greeting: str = "Hello", name: str = "Lheendah"):
     
    
    # return ({"greeting": f"{greeting}, {name}!"})
    return f"{greeting}, {name}! Congratulations, you have successfully completed the basic FastAPI task"

    # Return a JSON response with the greeting and name


