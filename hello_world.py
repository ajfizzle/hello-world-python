import os
from dotenv import load_dotenv
from pr_agent import cli
from pr_agent.config_loader import get_settings

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
print(f"Attempting to load .env file from: {dotenv_path}")
dotenv_loaded = load_dotenv(dotenv_path=dotenv_path)
print(f"Dotenv loaded: {dotenv_loaded}")

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
    
    # Debugging prints to confirm environment variables are loaded
    print(f"Loaded GIT_PLATFORM: {provider}")
    print(f"Loaded GIT_TOKEN: {user_token}")
    print(f"Loaded OPENAI_API_KEY: {openai_key}")
    
    # Fix the command format by joining the commands into a single string
    command = " ".join(["/review", "/describe", "/improve"])  # Commands as a single string
    print(f"Command to run: {command}")

    print("Setting configurations...")  # Debugging line
    try:
        # Setting the configurations
        get_settings().set("CONFIG.git_provider", provider)
        get_settings().set("openai.key", openai_key)
        get_settings().set("github.user_token", user_token)

        print(f"Configuration set: GIT_PROVIDER={provider}")
        print("Finished setting configurations.")  # Debugging line

        # Check the current settings
        current_settings = get_settings()
        print(f"Current settings: {current_settings}")

        # Run the command
        print(f"Running command: {command}")
        cli.run_command(pr_url, command)
    except Exception as e:
        print(f"Error during command execution: {str(e)}")

if __name__ == '__main__':
    print("Starting script...")
    main()
