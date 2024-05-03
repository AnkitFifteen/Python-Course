'''
If no answer found in oracle show M1

    #M1.Sorry, I didn’t quite understand that 😓. 
        Reach a librarian using following modes:
        (1) Call/WhatsApp at +91 8451905730 during operating
            hours(10 A.M. to 5 P.M.).
        (2) eMail at: care@porschelibrary.in
    
    #O1.Borrowing Books and Returns
    #R1.Interested in checking out books from the library? 
        All you need is your Aadhaar card! Loan periods are as follows: 
            Items are due 16 weeks from date of checkout, 5 renewals.
            
    #O2.Library Fine Policy
    #R2. There are no daily fines for Porsche library print materials, 
         but they will be considered lost at 14 days overdue and you will 
         be billed the replacement cost of ₹9177.80 per item.
         
    #O3.About Us!
    #R3. The library in the Tower Building was expanded in 1942, and the
        Library Annex was built in 1956.
        In a unique partnership, the Porsche Library houses both the old Varmora 
        Library Building and the new Varma Library branch. Together it stands for  
        “Por-shuh.” a.k.a. varma and varmora.
         
    #O4.Reserve a reading room
    #R4.Porsche library offers private and reservable reading rooms.
        Reading rooms are located on the 2nd, 3rd, 6th, 7th, and 8th floors 
        of the Porsche Library.
        You can reserve a room for a maximum of two hours per day and up to 4 
        days in advance. Feel free to enter the reading room you've reserved 
        directly—no check-in or key required.
        Follow link to book: https://booking.porschelibrary.in/reserve/reading
'''

oracle = [
    #Context Level 0 (Selection Phase)
    {"context": "", "question": "abcdefghijklmnopqrstuvwxyz", "answer": "which book", "new_context": ""},
    {"context": "", "question": "hello", "answer": "Hi!", "new_context": ""},
    {"context": "", "question": "life", "answer": "Yes, we have a life insurance!", "new_context": "life"},
    {"context": "", "question": "car", "answer": "Yes, we have an auto insurance!", "new_context": "car"},
    {"context": "", "question": "auto", "answer": "Yes, we have an auto insurance!", "new_context": "car"},
    {"context": "", "question": "vehicle", "answer": "Yes, we have an auto insurance!", "new_context": "car"},

    #Selection: Accident
    #Context Level 1 (Accident assets: Insurance, Accidents, Injuries)
    {"context": "", "question": "accident", "answer": "Oh, we are sorry! Is anyone injured?", "new_context": "accident_injured?"},
    {"context": "accident_injured?", "question": "yes", "answer": "Call 112! This is serious!", "new_context": "accident"},
    {"context": "accident_injured?", "question": "no", "answer": "Please give us the address...", "new_context": "accident_address"},
    {"context": "accident", "question": "help", "answer": "Please give us the address...", "new_context": "accident_address"},

    #Selection: Automobile
    #Context Level 2 (Automobile assets: Car, Car Model, Car Price)
    {"context": "car", "question": "how much", "answer": "What car do you have?", "new_context": "car_model"},
    {"context": "car_model", "question": "porsche", "answer": "Ah, that's expensive! It will cost you $31!", "new_context": "car"},
    {"context": "car_model", "question": "", "answer": "That's a simple car! It will cost you $28!", "new_context": "car"},

    #Selection: Life
    #Context Level 3 (Life assets: Insurance)
    {"context": "life", "question": "how much", "answer": "$10", "new_context": "life"},
]

context = "Enter `Menu` to get options."

while True:
    print("Current topic: ", context)
    question = input("You: ")
    got_answer = False
    
    if question == "Please end this chat.": 
        break;
        
    if question == "Menu":
        Options = input(" 1. Borrowing Books and Returns\n 2. Library Fine Policy\n 3. Reserve a reading room\n 4. About Us!\nEnter option number: ")
        match Options:
            case "1":
                print("Interested in checking out books from the library?\n\tAll you need is your Aadhaar card! Loan periods are as follows:\n\tItems are due 16 weeks from date of checkout, 5 renewals.\n")
            case "2":
                print("There are no daily fines for Porsche library print materials, but they will be considered lost at 14 days overdue and you will be billed the replacement cost of ₹9177.80 per item.\n")
            case "3":
                print("Porsche library offers private and reservable reading rooms.\nReading rooms are located on the 2nd, 3rd, 6th, 7th, and 8th floors of the Porsche Library.\nYou can reserve a room for a maximum of two hours per day and up to 4 days in advance.\nFeel free to enter the reading room you've reserved directly, no check-in or key required.\n\tFollow link to book: https://booking.porschelibrary.in/reserve/reading\n")
            case "4":
                print("The library in the Tower Building was expanded in 1942, and the Library Annex was built in 1956.\nIn a unique partnership, the Porsche Library houses both the old Varmora Library Building and the new Varma Library branch.\nTogether it stands for “Por-shuh.” a.k.a. Varma and Varmora.\n")
            case _:
                print("Sorry, I didn’t quite understand that.\nReach a librarian using following modes:\n\t(1) Call/WhatsApp at +91 8451905730 during operating hours(10 A.M. to 5 P.M.).\n\t(2) eMail at: care@porschelibrary.in\n")
    else:
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
            