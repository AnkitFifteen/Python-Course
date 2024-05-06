oracle = [
    {"context": "", "question": "hello", "answer": "Hi!", "new_context": ""},
    {"context": "", "question": "borrow book", "answer": "To borrow book you need a valid Aadhaar card.", "new_context": "Books"},
    {"context": "", "question": "book request", "answer": "Enter name of book for which you want to put request?", "new_context": "Requested_Book"},
    {"context": "", "question": "book genre", "answer": "Fiction, Science, Historical, Mathematics", "new_context": "Books"},
    {"context": "", "question": "format of book", "answer": "Yes we have books in both digital and physical format.", "new_context": "Books"},
    {"context": "", "question": "have digital book", "answer": "Yes we have books in digital format.", "new_context": "Digital_Books"},
    {"context": "", "question": "want digital book", "answer": "Please go to https://books.porschelibrary.in/buy/ebooks to search/buy.", "new_context": "Digital_Books"},
    {"context": "", "question": "want Alice in wonderland", "answer": "Okay.", "new_context": "AIW_Book"},
    {"context": "AIW_Book", "question": "how much cost", "answer": "Rs. 499", "new_context": "AIW_Book"},
    {"context": "AIW_Book", "question": "available hindi language", "answer": "No.", "new_context": "AIW_Book"},
    {"context": "AIW_Book", "question": "have digital copy", "answer": "No.", "new_context": "AIW_Book"},
   ]

BookRequests = list()
printMenuMsgOnce = True
context = ""

while True:
    if printMenuMsgOnce:
        print("Enter `Menu` to get options.")
        printMenuMsgOnce = False
    
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
        if context == "Requested_Book":
            BookRequests.append(question)      #Dumping book requests not found in oracle
            print(BookRequests)
    
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
    
        if not got_answer and context != "Requested_Book":
            print("Bot:", "Sorry, I didn't get it.")
        
        if context == "Requested_Book":
            print("Request submitted.")
        