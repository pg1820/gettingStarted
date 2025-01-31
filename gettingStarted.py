#!/usr/bin/env python3

def welcome_assignment_answers(question):
    """
    welcome_assignment_answers
    Input  - A question (string) exactly matching one of the nine prompts.
    Output - The correct answer (string or integer).
    """
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        # Using your newly mentioned hash:
        answer = "7e2f99ca5204528b75fd2ce67ada696b8b40d19722c7edfa162adbe8e8e903b3"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        # 5-layer model => DNS is Application => 5
        answer = 5
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        # 5-layer model => ICMP is Network => 3
        answer = 3
    else:
        # If there's a mismatch in question text
        answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"

    return answer


if __name__ == "__main__":
    # Quick test—prints each question and the corresponding answer.
    questions = [
        "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?",
        "Are encoding and encryption the same? - Yes/No",
        "Is it possible to decrypt a message without a key? - Yes/No",
        "Is it possible to decode a message without a key? - Yes/No",
        "Is a hashed message supposed to be un-hashed? - Yes/No",
        "What is the SHA256 hashing value of your NYU email and use the answer in your code - ",
        "Is MD5 a secured hashing algorithm? - Yes/No",
        "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number",
        "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"
    ]

    for q in questions:
        print(f"Q: {q}")
        print(f"A: {welcome_assignment_answers(q)}\n")
