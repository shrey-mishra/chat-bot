import openai
from dotenv import load_dotenv
import time
import logging
from datetime import datetime
from keys import thread_id, assistant_id


load_dotenv()

client = openai.OpenAI()
model = "gpt-3.5-turbo-0125"
chat_history_file = "chat_history.txt"  # File to store conversation


def save_to_chat_history(message, response):
    """
    Saves the conversation between user and assistant to a text file.

    Args:
        message (str): User's message.
        response (str): Assistant's response.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(chat_history_file, "a") as f:
        f.write(f"\n** {timestamp} User: {message} \n")
        f.write(f"Assistant: {response} \n")


def send_message_and_get_response(message):
    """
    Sends a message to the assistant via OpenAI API and retrieves the response.

    Args:
        message (str): The message to be sent to the assistant.

    Returns:
        str: The assistant's response to the message.
    """

    num_dots = 0  # Track number of dots printed for waiting animation

    def print_waiting_message():
        nonlocal num_dots
        print("Waiting for response...", end="")
        for _ in range(num_dots):
            print(".", end="", flush=True)
        num_dots += 1  # Increment dots for next iteration

    print_waiting_message()  # Initial waiting message

    # Send the message to the thread
    message = client.beta.threads.messages.create(
        thread_id=thread_id, role="user", content=message
    )

    # Start a run of the assistant
    # dataset directions
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
        instructions="Your desired prompt",
    )

    # Wait for the run to complete and retrieve the response
    response = wait_for_run_completion(client, thread_id, run.id)

    # Clear waiting message and newline after receiving response
    print("\r" + (" " * len("Waiting for response...")), end="", flush=True)

    # Save conversation to chat history
    save_to_chat_history(message.content, response)

    return response


def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
    """
    Wait for a run to complete and print the elapsed time.
    Args:
        client: OpenAI client instance
        thread_id: The ID of the thread whose run is associated with model
        run_id: The ID of the run
        sleep_interval: The time in seconds to wait between checks

    Returns:
        str: The assistant's response to the message
    """

    while True:
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            if run.completed_at:
                elapsed_time = run.completed_at - run.created_at
                formatted_elapsed_time = time.strftime(
                    "%H:%M:%S", time.gmtime(elapsed_time)
                )
                logging.info(f"Run completed in {formatted_elapsed_time}")

                # Get messages and return the assistant's response
                messages = client.beta.threads.messages.list(thread_id=thread_id)
                last_message = messages.data[0]
                response = last_message.content[0].text.value
                return response

        except Exception as e:
            logging.error(
                f"An error occurred while retrieving data from the server: {e}"
            )

        print("", end="", flush=True)  # Print a dot for continuous waiting
        time.sleep(sleep_interval)


# loop for continuous conversation, type 'quit' to exit
while True:
    message = input("\nEnter your message (or type 'quit' to exit): ")
    trimmed_message = message.lower().strip()
    if trimmed_message == "quit":
        break

    response = send_message_and_get_response(message)
    print(f"\nAssistant Response: {response}")
