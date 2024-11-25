# Import necessary modules
import os
from dotenv import load_dotenv
from pr_agent import cli
from pr_agent.config_loader import get_settings

# Load the .env file
load_dotenv()  # This will automatically load variables from the .env file into the environment

print("Hello, World!")
name = input("Joel Test: ")
print(f"Hello, {name}!")

def main():
    print("Starting main function...")  # Debugging line
    
    # Get the values from environment variables
    provider = os.getenv("GIT_PLATFORM")  # github/gitlab/bitbucket/azure_devops
    user_token = os.getenv("GIT_TOKEN")  # User token
    openai_key = os.getenv("OPENAI_API_KEY")  # OpenAI key
    pr_url = "https://github.com/ajfizzle/hello-world-python/pull/1"  # PR URL
    command = "/review", "/describe", "/improvee"  # Commands to run

    print("Setting configurations...")  # Debugging line
    # Setting the configurations
    get_settings().set("CONFIG.git_provider", provider)
    get_settings().set("openai.key", openai_key)

    print("Finished setting configurations.")  # Debugging line

if __name__ == '__main__':
    print("Running the script...")  # Debugging line
    main()
