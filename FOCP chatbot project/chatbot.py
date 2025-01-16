import random
import json

def responses_loder():
    with open("responses.json", "r") as file:
        data = json.load(file)
    return data

def chat():
    responses = responses_loder()
    keywords = responses["keywords"]
    random_responses = responses["random_responses"]

    user_name = input("stranger! What's your name? ")
    print(f"Hello {user_name}! I'm here to help .")
    

    agent_name = random.choice(["Alex", "shubham", "pimbal baba", "prasun", "prasanna"])
    print(f"You are now chatting with {agent_name}.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["bye", "quit", "exit","Sayonara"]:
            print(f"{agent_name}: Sayonara, {user_name}! Have a great day!")
            break
        if random.random()< 0.3:
            print("error you are annoying..............  :(")
            break
        
        response_found = False
        for keyword, response in keywords.items():
            if keyword in user_input:
                print(f"{agent_name}: {response.format(user_name=user_name)}")
                response_found = True
                break

        if not response_found:
            print(f"{agent_name}: {random.choice(random_responses).format(user_name=user_name)}")

if __name__ == "__main__":
    chat()