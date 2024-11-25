print("Hello, World!")
name = input("Joel Test: ")
print(f"Hello, {name}!")

from pr_agent import cli
from pr_agent.config_loader import get_settings

def main():
    print("Starting main function...")  # Debugging line
    
    # Fill in the following values
    provider = "github"  # github/gitlab/bitbucket/azure_devops
    user_token = "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"  # User token
    openai_key = "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"  # OpenAI key
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
