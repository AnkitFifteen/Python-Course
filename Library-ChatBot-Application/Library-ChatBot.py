oracle = [
    {"context": "", "question": "book", "answer": "which book", "new_context": ""},
    {"context": "", "question": "hello", "answer": "Hi!", "new_context": ""},
    {"context": "", "question": "life", "answer": "Yes, we have a life insurance!", "new_context": "life"},
    {"context": "", "question": "car", "answer": "Yes, we have an auto insurance!", "new_context": "car"},
    {"context": "", "question": "auto", "answer": "Yes, we have an auto insurance!", "new_context": "car"},
    {"context": "", "question": "vehicle", "answer": "Yes, we have an auto insurance!", "new_context": "car"},

    {"context": "", "question": "accident", "answer": "Oh, we are sorry! Is anyone injured?", "new_context": "accident_injured?"},
    {"context": "accident_injured?", "question": "yes", "answer": "Call 112! This is serious!", "new_context": "accident"},
    {"context": "accident_injured?", "question": "no", "answer": "Please give us the address...", "new_context": "accident_address"},
    {"context": "accident", "question": "help", "answer": "Please give us the address...", "new_context": "accident_address"},

    {"context": "car", "question": "how much", "answer": "What car do you have?", "new_context": "car_model"},
    {"context": "car_model", "question": "porsche", "answer": "Ah, that's expensive! It will cost you $31!", "new_context": "car"},
    {"context": "car_model", "question": "", "answer": "That's a simple car! It will cost you $28!", "new_context": "car"},

    {"context": "life", "question": "how much", "answer": "$10", "new_context": "life"},
]

context = ""
while True:
    print("Current topic: ", context)
    question = input("You: ")
    got_answer = False

    if context == "accident_address":
        address = question

    for el in oracle:
        if el["context"] == context or el["context"] == "":
            match = True
            for word in el["question"].split():
                if word not in question.lower():
                    match = False
            if match:
                print("Bot:", el["answer"])
                got_answer = True
                context = el["new_context"]
                break

    if not got_answer:
        print("Bot:", "Sorry, I didn't get it.")