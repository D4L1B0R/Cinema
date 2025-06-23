def responde(): # Reasuring that answers are matching the previous question
    print("Please responde with yes/no.")

def responde1():
    print("Please responde with one of the answers above.")

def input_data(): # Entering data for every role 
    global first_name 
    global last_name 
    global user_name
    global password
    print("Enter first name:")
    first_name = input()
    print("Enter last name:")
    last_name = input()
    print("Enter user name:")
    user_name = input()
    print("Enter password:")
    password = input()

def input_worker():
    global worker
    print("Enter worker's job (seller or manager):")
    worker = input()

def change_info(): #Changing user's informations 
    for element in main_list:
            if user_n == element[0]:
                print("This is your user name before the change: ")
                print(element[0])
                print("This is your password before the change: ")
                print(element[1])
                print("This is your first name before the change: ")
                print(element[2])
                print("This is your last name before the change: ")
                print(element[3]+"\n")
                print("Please enter your new first name: ")
                first_name = input()
                print("Please enter your new last name: ")
                last_name = input()
                print("Please enter your new password: ")
                password = input()
                main_list.remove(element)
                if element[4] == "manager":
                    main_list.append([user_n, password, first_name, last_name, "manager"])
                    print("Done! What do you want to do next? \n[0] change your informations \n[1] employ \n[2] add movies \n[3] delete movies \n[4] replace movies \n[5] add projection appointments \n[6] delete projection appoinments \n[7] replace projection appointments \n[8] sign out")
                    option_manager = input()
                    manager(option_manager)
                elif element[4] == "seller":
                    main_list.append([user_n, password, first_name, last_name, "seller"])
                    print("Done! What do you want to do next? \n[0] change your informations \n[1] sign out")
                    option_seller = input()
                    seller(option_seller)
                else:
                    main_list.append([user_n, password, first_name, last_name, "user"])
                    print("Done! What do you want to do next? \n[1] see movie options \n[2] change your information \n[3] sign out")
                    option_user = input()
                    user(option_user)

def movies():
    print(f"{'Index' : ^5}{'Movie name' : ^30}{'Genre' : ^8}{'Duration (min)' : ^14}{'Director' : ^22}{'Main actors' : ^43}{'Origin country' : ^18}{'Release year' : ^13}"+"\n")
    for element in movie_list:
        print(f"{element[0] : ^5}{element[1] : ^29}{element[2] : ^10}{element[3] : ^12}{element[4] : ^25}{element[5] : ^40}{element[6] : ^20}{element[7] : ^11}") 

def delete_movie():
    global movie_index
    global movie_name_change
    print("Do you want to see all movies? \n[y] yes \n[n] no")
    see_all_movies = input()
    if see_all_movies == "y":
        movies()
    elif see_all_movies == "n":
        pass
    else:
        responde()
        delete_movie()
    print("Enter movie index:")
    movie_index = input()
    i = 0
    for element in movie_list:
        if movie_index == element[0]:
            movie_name_change = element[1]
            movie_list.remove(element)
            i += 1
    if i == 0:
        print("Invalid input. Please enter a valid index.")
        do_again_action()
        if loop is False:
            choose_option_manager()
        else:
            delete_movie()

def delete_all_data_movie(): # Deleting the movie, brings deleting all information in tickets, projections and appointments about that movie
    global movie_index
    global movie_name_change
    print("Do you want to see all movies? \n[y] yes \n[n] no")
    see_all_movies = input()
    if see_all_movies == "y":
        movies()
    elif see_all_movies == "n":
        pass
    else:
        responde()
        delete_all_data_movie()
    print("Enter movie index:")
    movie_index = input()
    i = 0
    for element1 in movie_list:
        for element2 in projections_list:
            for element3 in appointment_list:
                if movie_index == element1[0] and element1[1] == element2[5] and element2[0] in element3[0]:
                    appointment_list.remove(element3)
    for element1 in movie_list:
        for element2 in projections_list:
            for element3 in ticket_list:
                if movie_index == element1[0] and element1[1] == element2[5] and element2[0] in element3[1]:
                    ticket_list.remove(element3)
    for element1 in movie_list:
        for element2 in projections_list:
            if movie_index == element1[0] and element1[1] == element2[5]:
                projections_list.remove(element2)
    for element in movie_list:
        if movie_index == element[0]:
            movie_name_change = element[1]
            movie_list.remove(element)
            i += 1
    if i == 0:
        print("Invalid input. Please enter a valid index.")
        do_again_action()
        if loop is False:
            choose_option_manager()
        else:
            delete_all_data_movie()

def do_again_action(): # Enabeling to exit in functions that can lead to loop
    global loop
    loop = False
    print("Do you want to perform action again? \n[1] do again \n[2] go back")
    answer = input()
    if answer == "1":
        loop = True
    elif answer == "2":
        pass
    else:
        responde1()
        do_again_action()

def change_movie():
    global movie_name
    global genre
    global duration
    global director
    global main_actors
    global origin_country
    global release_year
    print("Enter movie name:")
    movie_name = input()
    for element in main_list:
        if movie_name == element[1]:
            print("That movie name already exists, please choose another.")
            change_movie()
    print("Enter movie genre:")
    genre = input()
    print("Enter duration of the movie:")
    duration = input()
    duration_valid(duration)
    print("Enter director's name and last name:")
    director = input()
    print("Enter name and last name of main actors:")
    main_actors = input()
    print("Enter the country of origin of the movie:")
    origin_country = input()
    release_year_valid()

def duration_valid(duration): #Checking if variable is positive integer
    try:
        duration = int(duration)
        duration > 0
    except ValueError:
        print("Enter a valid number!")
        duration = input()
        duration_valid(duration)
        
def release_year_valid():
    global release_year
    print("Enter release year of the movie:")
    release_year = input()
    if not valid_year_format(release_year):
        print("\nInvalid year format! \nTry again:")
        release_year_valid()

def choose_option_manager(): # Second manager's menu (when returning)
    print("\nWhat you want to do next? \n[1] change your informations \n[1] employ \n[2] add movies \n[3] delete movies \n[4] replace movies \n[5] add projection appointments \n[6] delete projection appoinments \n[7] replace projection appointments \n[8] generate projection appointments \n[9] reports \n[10] sign out")
    option_manager = input()
    manager(option_manager)

def movies_choose(): 
    print("\nWhat you want to do? \n[0] see movie list again \n[1] view movie's info \n[2] multiple search \n[3] movie projections appointments \n[4] back to main menu")
    movie_options = input()
    movie_option(movie_options)

def register_user_choose(): # Second register user's menu (when returning)
    print("\nWhat you want to do? \n[1] movie review \n[2] change informations \n[3] book a ticket \n[4] back to main menu")
    user_option = input()
    user(user_option)

def seller_menu(): # Second seller's menu (when returning)
    print("What you want to do next? \n[0] change your informations \n[1] reserve or buy new tickets \n[2] review tickets \n[3] cancel tickets \n[4] search tickets \n[5] change tickets \n[6] change reserved tickets to bought \n[7] cancel reservations 30 min before projeciton \n[8] sign out")
    option_seller = input()
    seller(option_seller)

def projections_manager():
    print(f"{'Index' : ^10}{'Movie name' : ^30}{'Hall' : ^10}{'Starting time' : ^20}{'Ending time' : ^20}{'Days in the week' : ^48}{'Date' : ^23}{'Ticket price (RSD)' : ^18}" + "\n")
    for element in combined_list:
        print(f"{element[0] : ^10}{element[6] : ^30}{element[2] : ^10}{element[3] : ^20}{element[4] : ^20}{element[5] : ^50}{element[1] : ^20}{element[7] : ^18}")

def ticket_user():
    print(f"{'Index' : ^10}{'Movie name' : ^30}{'Hall' : ^10}{'Starting time' : ^20}{'Ending time' : ^20}{'Days in the week' : ^48}{'Date' : ^23}{'Ticket price (RSD)' : ^18}" + "\n")
    for element in combined_list:
        projection_time =  element[1] + " " + element[3]
        checking_time_past_30_min(projection_time)
        if projection_late == False:
            discount(user_n)
            if discount_valid == True:
                element[7] = 90*float(element[7])/100
                print(f"{element[0] : ^10}{element[6] : ^30}{element[2] : ^10}{element[3] : ^20}{element[4] : ^20}{element[5] : ^50}{element[1] : ^20}{element[7] : ^18}")
            else:
                print(f"{element[0] : ^10}{element[6] : ^30}{element[2] : ^10}{element[3] : ^20}{element[4] : ^20}{element[5] : ^50}{element[1] : ^20}{element[7] : ^18}")

def projections_users():
    print(f"{'Movie name' : ^30}{'Hall' : ^10}{'Starting time' : ^20}{'Ending time' : ^20}{'Days in the week' : ^48}{'Date' : ^23}{'Ticket price (RSD)' : ^18}" + "\n")
    for element in combined_list:
        print(f"{element[6] : ^30}{element[2] : ^10}{element[3] : ^20}{element[4] : ^20}{element[5] : ^50}{element[1] : ^20}{element[7] : ^18}")

def generate_random_letters(start='AA'): # For appointments, always making next 2 pairs of letters from alphabet begining from 'AA'
    alphabet = string.ascii_uppercase  
    found_start = False
    for first_letter in alphabet:
        for second_letter in alphabet:
            current_pair = first_letter + second_letter
            if not found_start:
                if current_pair == start:
                    found_start = True
            else:
                yield current_pair

def projection_random_letters():
    last_pair = 'AA'  # Default start pair
    if appointment_list:
        last_pair = appointment_list[-1][0][-2:]
    letter_pair_generator = generate_random_letters(last_pair)
    return next(letter_pair_generator)

def valid_time_format(variable): # Cheking time, date and year format for input variable (is it valid)
    pattern = re.compile(r'^([01]\d|2[0-3]):[0-5]\d$')
    return bool(pattern.match(variable))

def valid_date_format(variable):
    pattern = re.compile(r'^\d{2}\.\d{2}\.\d{4}\.$')
    return bool(pattern.match(variable))

def valid_year_format(variable):
    pattern = re.compile(r'^\d{4}$')
    return bool(pattern.match(variable))

def add_projections():
    global number_of_days
    global projection_date
    global projection_hall
    global projection_starting_time
    global projection_ending_time
    global projection_days_of_week
    global projection_movie_name
    global projection_price
    print("Enter the days of the week (with first letter capitalized) when the movie is projecting:")
    projection_days_of_week = input()
    if "Monday" not in projection_days_of_week and "Tuesday" not in projection_days_of_week and "Wednesday" not in projection_days_of_week and "Thursday" not in projection_days_of_week and "Friday" not in projection_days_of_week and "Saturday" not in projection_days_of_week and "Sunday" not in projection_days_of_week:
        print("Enter the valid day of the week!")
        add_projections()
    add_projection_valid_date()
    projection_hall_check()
    add_projection_valid_starting_time()
    add_projection_valid_ending_time()
    projection_movie_name_check()
    add_projection_valid_price()

def projection_movie_name_check():
    global projection_movie_name
    print("Enter name of the movie:")
    projection_movie_name = input()
    for element in movie_list:
        if projection_movie_name == element[1]:
            break
    else:
        print("Invalid name, there is no movie with that name!")
        do_again_action()
        if loop is False:
            choose_option_manager()
        else:
            projection_movie_name_check()  

def projection_hall_check():
    global projection_hall
    print("Enter the hall of the movie projection:")
    projection_hall = input()
    for element in hall_list:
        if projection_hall == element[0]:
            break
    else:
        print("Invalid hall, there is no hall with that name!")
        do_again_action()
        if loop is False:
            choose_option_manager()
        else:
            projection_hall_check()

def add_projection_valid_date(): #Cheking validation for date of projection
    print("Enter date of the movie projection (in format DD.MM.YYYY., for example 12.12.2012.):")
    projection_date = input()
    if not valid_date_format(projection_date):
        print("Invalid date format.")
        add_projection_valid_date()

def add_projection_valid_starting_time(): #Cheking validation for time of projection
    print("Enter starting time of the projection (in format HH:MM, for example 12:00):")
    projection_starting_time = input()
    if not valid_time_format(projection_starting_time):
        print("Invalid time format.")
        add_projection_valid_starting_time()

def add_projection_valid_ending_time():
    print("Enter ending time of the projection (in format HH:MM, for example 12:00):")
    projection_ending_time = input()
    if not valid_time_format(projection_ending_time):
        print("Invalid time format.")
        add_projection_valid_ending_time()

def add_projection_valid_price(): # Checking if the price (variable) is float
    print("Enter ticket price for the movie (for example 450):")
    projection_price = input()
    try:
        projection_price = float(projection_price)
    except ValueError:
        print("Enter a valid number!")
        add_projection_valid_price()
    
def delete_projections():
    global index_delete_projection 
    print("Enter the index of the projection you want to erase:")
    index_delete_projection = input()
    for element in projections_list:
        if index_delete_projection == element[0]:
            projections_list.remove(element)
            break
    else:
        print("Invalid index.")
        do_again_action()
        if loop is False:
            choose_option_manager()
        else:
            delete_projections()
    for element in ticket_list:
        if index_delete_projection in element[1]:
            ticket_list.remove(element)
    for element in appointment_list:
        if index_delete_projection in element[0]:
            appointment_list.remove(element)

def generate_days(day_of_week): # Getting dates based on day of the week (as variable) that represent nearest 2 dates of that day
    today = datetime.today()
    days_until_day = (day_of_week - today.weekday()) % 7
    first_date = today + timedelta(days=days_until_day)
    second_date = first_date + timedelta(days=7)
    global first_date_str
    global second_date_str
    first_date_str = first_date.strftime('%d.%m.%Y.')
    second_date_str = second_date.strftime('%d.%m.%Y.')
    return first_date_str, second_date_str

def generate_movie_appointments(): # Making new appointments based on previous, cutting ones that already exists
    for element1 in projections_list:
        if "Monday" in element1[4]:
            day_of_week = 0
            generate_days(day_of_week)
            letters = projection_random_letters()
            appointment_list.append([element1[0] + letters, first_date_str])
            letters = projection_random_letters()
            appointment_list.append([element1[0] + letters, second_date_str])
        if "Tuesday" in element1[4]:
            day_of_week = 1
            generate_days(day_of_week)
            letters = projection_random_letters()
            appointment_list.append([element1[0] + letters, first_date_str])
            letters = projection_random_letters()
            appointment_list.append([element1[0] + letters, second_date_str])
        if "Wednesday" in element1[4]:
            day_of_week = 2
            generate_days(day_of_week)
            letters = projection_random_letters()
            appointment_list.append([element1[0] + letters, first_date_str])
            letters = projection_random_letters()
            appointment_list.append([element1[0] + letters, second_date_str])
        if "Thursday" in element1[4]:
            day_of_week = 3
            generate_days(day_of_week)
            letters = projection_random_letters()
            appointment_list.append([element1[0] + letters, first_date_str])
            letters = projection_random_letters()
            appointment_list.append([element1[0] + letters, second_date_str])
        if "Friday" in element1[4]:
            day_of_week = 4
            generate_days(day_of_week)
            letters = projection_random_letters()
            appointment_list.append([element1[0] + letters, first_date_str])
            letters = projection_random_letters()
            appointment_list.append([element1[0] + letters, second_date_str])
        if "Saturday" in element1[4]:
            day_of_week = 5
            generate_days(day_of_week)
            letters = projection_random_letters()
            appointment_list.append([element1[0] + letters, first_date_str])
            letters = projection_random_letters()
            appointment_list.append([element1[0] + letters, second_date_str])
        if "Sunday" in element1[4]:
            day_of_week = 6
            generate_days(day_of_week)
            letters = projection_random_letters()
            appointment_list.append([element1[0] + letters, first_date_str])
            letters = projection_random_letters()
            appointment_list.append([element1[0] + letters, second_date_str])
    combined_list = []
    for elem2 in projections_list:
            for elem1 in appointment_list:
                if elem2[0] in elem1[0]:
                    combined_list.append(elem1 + elem2[1:])
    seen = {}
    i = 0
    while i < len(appointment_list):
        sublist = appointment_list[i]
        key = (sublist[0][:4], sublist[1])
        if key in seen:
            appointment_list.pop(i)
        else:
            seen[key] = True
            i += 1

def book_ticket(): # Option of booking (reservating) tickets for user
    print("What option you choose? \n[1] book a ticket \n[2] see all reserved tickets \n[3] cancel reservation \n[4] go back")
    ticket_option = input()
    ticket_options(ticket_option)

def ticket_options(ticket_option):
    if ticket_option == "1":
        booking_ticket()
        book_ticket()
    if ticket_option == "2":
        review_tickets()
        book_ticket()
    if ticket_option == "3":
        review_tickets()
        canceling_ticket()
        book_ticket()
    if ticket_option == "4":
        register_user_choose()
    else:
        responde1()
        ticket_option = input()
        ticket_options(ticket_option)

def discount(name): # Registered user that have already spent 5000 RDS in previous year gets 90% discount for every new ticket
    global discount_valid
    discount_valid = False
    sold_price = 0 
    for element1 in ticket_seller_list:
        for element2 in projections_list:
            discount_date(element1[3])
            if name == element1[0] and element2[0] in element1[1] and discount_late == True:
                sold_price += float(element2[6])
    if sold_price > 5000:
        discount_valid = True

def discount_date(target_time): # Determining if date of buying ticket is  in the past 1 year for every ticket of resistered user
    global discount_late
    discount_late = False
    projection_time = datetime.strptime(target_time, "%d.%m.%Y.")
    current_time = datetime.now()
    time_difference = current_time - projection_time
    if time_difference < timedelta(days = 365):
        discount_late = True
    else:
        pass

def booking_ticket(): # Booking (registering) tickets for registered user
    print("Do you want to see all appointments? \n[y] yes \n[n] no")
    see_all_appointments = input()
    if see_all_appointments == "y":
        ticket_user()
    elif see_all_appointments == "n":
        pass
    else:
        responde()
        booking_ticket()
    print("Choose apppointment that you want to book:")
    global appointment
    appointment = input()
    appointment_found = False
    for element in combined_list:
        projection_time =  element[1] + " " + element[3]
        checking_time_past_30_min(projection_time)
        if appointment == element[0] and projection_late == False:
            hall = element[2]
            appointment_found = True
            break
    if appointment_found == True:  
        for element in hall_list:
            if hall == element[0]:
                rows = int(element[2])
                cols = len(element[3])
        alphabet = string.ascii_uppercase
        matrix = [[alphabet[i % len(alphabet)] for i in range(cols)] for _ in range(rows)]
        positions_to_mark = []
        for element in ticket_list:
            if appointment == element[1]:
                positions_to_mark.append([int(element[2][0])-1, ord(element[2][1].upper()) - ord('A')])
        for row, col in positions_to_mark:
            matrix[row][col] = 'X'
        for row in matrix:
            print(" ".join(str(cell) for cell in row))
        choosing_valid_seat()
    else:
        print("Invalid appointment!")
        do_again_action()
        if loop is False:
            return
        else:
            booking_ticket()

def choosing_valid_seat():
    print("Choose the seats you want to book:")
    seat = input()
    try:
        for element1 in projections_list:
            for element2 in hall_list:
                if element1[0] in appointment and element1[1] == element2[0] and int(seat[0]) <= int(element2[2]) and int(seat[0]) > 0 and seat[1] in element2[3] and len(seat) == 2:
                    for element in main_list:
                        if user_n == element[0] and element[4] == "user":
                            seats_booking(seat)
                    else:
                        seats_booking_seller(seat)
    except ValueError:
        print("Enter a valid seat!")
        choosing_valid_seat()
    except IndexError:
        print("Enter a valid seat!")
        choosing_valid_seat()
    else:
        print("Enter a valid seat!")
        choosing_valid_seat()
    
def seats_booking(seat):
    formatted_date = date.today().strftime("%d.%m.%Y.")
    for element in ticket_list:
        if appointment == str(element[1]) and seat == str(element[2]):
            print("This seat is already taken! Pick another!")
            do_again_action()
            if loop is False:
                book_ticket()
            else:
                choosing_valid_seat()
    else:
        ticket_list.append([user_n, appointment, seat, formatted_date, "reserved"])
        print("What you want do to next? Do you want to pick another seat or go back? \n[1] reserve another ticket with same appointment \n[2] resevre another ticket \n[3] go back")
        what_to_do = input()
        what_to_do_seats(what_to_do) 

def seats_booking_seller(seat):
    formatted_date = date.today().strftime("%d.%m.%Y.")
    checking_booking_type()
    for element in ticket_list:
        if appointment == str(element[1]) and seat == str(element[2]):
            print("This seat is already taken! Pick another!")
            do_again_action()
            if loop is False:
                seller_menu()
            else:
                choosing_valid_seat()
    else:
        ticket_list.append([name_for_booking, appointment, seat, formatted_date, booking])
        if booking == "bought":
            ticket_seller_list.append([name_for_booking, appointment, seat, formatted_date, user_n])
        print("What you want do to next? Do you want to pick another seat or go back? \n[1] reserve or buy another ticket with same appointment \n[2] reserve or buy another ticket with other appointment \n[3] go back")
        what_to_do = input()
        what_to_do_seats_seller(what_to_do)

def checking_booking_type():
    global booking
    print("Ticket is reserved or bought? \n[r] reserved \n[b] bought")
    b_or_r = input()
    if b_or_r == "r":
        booking = "reserved"
    elif b_or_r == "b":
        booking = "bought"
    else:
        responde1()
        checking_booking_type()

def what_to_do_seats(what_to_do):
    if what_to_do == "1":
        choosing_valid_seat()
    elif what_to_do == "2":
        booking_ticket()
    elif what_to_do == "3":
        book_ticket()
    else:
        responde1()
        what_to_do = input()
        what_to_do_seats(what_to_do)

def what_to_do_seats_seller(what_to_do):
    if what_to_do == "1":
        choosing_valid_seat()
    elif what_to_do == "2":
        book_tickets_valid_appointment()
    elif what_to_do == "3":
        seller_menu()
    else:
        responde1()
        what_to_do = input()
        what_to_do_seats_seller(what_to_do)

def review_tickets():
    print("This is the list of your ticket reservations:")
    user_ticket_list = []
    for element1 in ticket_list:
        if user_n == element1[0]:
            appointment = element1[1]
            for element2 in projections_list:
                if element2[0] in appointment and element1[4] == "reserved":
                    user_ticket_list.append([element1[1], element2[5], element1[3], element2[2], element2[3], element1[2]])
    print(f"{'Ticket appointment' : ^28}{'Movie name' : ^30}{'Date' : ^21}{'Starting time' : ^23}{'Ending time' : ^23}{'Seat' : ^4}" + "\n")
    for element in user_ticket_list:
        print(f"{element[0] : ^28}{element[1] : ^30}{element[2] : ^21}{element[3] : ^23}{element[4] : ^23}{element[5] : ^4}")

def canceling_ticket():
    canceling_valid_appointment()
    canceling_valid_seat()
    for element in ticket_list:
        if user_n == element[0] and canceling_appointment == element[1] and seat_cancel == element[2] and element[4] == "reserved":
            ticket_list.remove(element)
            print("Do you want to cancel another ticket? \n[y] yes \n[n] no")
            yes_no = input()
            canceling_another_ticket(yes_no) 
    else:
        print("That ticket is not reserved by you!")
        do_again_action()
        if loop is False:
            return
        else:
            canceling_ticket()

def canceling_all_tickets():
    canceling_valid_appointment()
    canceling_valid_seat()
    for element1 in ticket_list:
        if canceling_appointment == element1[1] and seat_cancel == element1[2]:
            ticket_list.remove(element1)
            for element2 in ticket_seller_list:
                if canceling_appointment == element2[1] and seat_cancel == element2[2]:
                    ticket_seller_list.remove(element2)
            print("Do you want to cancel another ticket? \n[y] yes \n[n] no")
            yes_no = input()
            canceling_another_all_ticket(yes_no) 
    else:
        print("That ticket is invalid!")
        canceling_all_tickets()

def canceling_valid_appointment():
    global canceling_appointment
    print("Pick the appointment of ticket you want to cancel:")
    canceling_appointment = input()
    appointment_for_canceling_valid = False
    for element in appointment_list:
        for item in projections_list:
            if canceling_appointment == element[0] and item[0] in element[0]:
                projection_time =  element[1] + " " + item[2]
                checking_time_past_30_min(projection_time)
                if projection_late == False:
                    appointment_for_canceling_valid = True
                    break
    if appointment_for_canceling_valid == True:
        return
    else:
        print("Invalid appontment! Do you want to go back? \n[1] try again \n[2] go back")
        try_again = input()
        if try_again == "1":
            canceling_valid_appointment()
        elif try_again == "2":
            for element in main_list:
                if user_n == element[0] and element[4] == "user":
                    book_ticket()
            else:
                seller_menu()
        else:
            responde1()
            canceling_valid_appointment()

def canceling_valid_seat():
    global seat_cancel
    print("Choose the seats for ticket you want to work with:")
    seat_cancel = input()
    try:
        for element1 in projections_list:
            for element2 in hall_list:
                if element1[0] in canceling_appointment and element1[1] == element2[0] and int(seat_cancel[0]) <= int(element2[2]) and int(seat_cancel[0]) > 0 and seat_cancel[1] in element2[3] and len(seat_cancel) == 2:
                    return
    except ValueError:
        print("Enter a valid seat!")
        canceling_valid_seat()
    except IndexError:
        print("Enter a valid seat!")
        canceling_valid_seat()
    else:
        print("Enter a valid seat!")
        canceling_valid_seat()

def canceling_another_ticket(yes_no):
    if yes_no == "y":
        canceling_ticket()
    elif yes_no == "n":
        book_ticket()
    else:
        responde 
        canceling_another_ticket()

def canceling_another_all_ticket(yes_no):
    if yes_no == "y":
        canceling_all_tickets()
    elif yes_no == "n":
        seller_menu()
    else:
        responde 
        canceling_another_all_ticket()

def login(user_name, password):
    global user_n
    user_n = user_name
    for element in main_list:
        if user_name == element[0] and password == element[1]:
            identification()
            return
    print("If you can't remember your password or username, we can return you to the main menu.\nDo you have that problem? \n[y] yes \n[n] no")
    yes_no = input()
    cant_login(yes_no)

def sign(first_name, last_name, user_name, password): # Making a new account
   for element in main_list:
    if  user_name == element[0]:
        print("That user name has been already taken. Try again.")
        input_data()
        sign(first_name, last_name, user_name, password)
    file.close()
    if not any(char.isdigit() for char in user_name):
        print("You need to make user name with at least one digit. Try again.")
        input_data()
        sign(first_name, last_name, user_name, password)
    if len(user_name)<=6:
        print("You need to make user name with minimum seven characters. Try again.")
        input_data()
        sign(first_name, last_name, user_name, password)
    else:
        main_list.append([user_name, password, first_name, last_name, "user"])
        print("Now you can log in to your account. \n")
        print("Enter your user name: ")
        user_name = input()
        print("Enter your password: ")
        password = input()
        login(user_name, password)

def cant_login(yes_no): # User can't remember informations about his account (has option to go back to the main menu)
    if yes_no == "n":
        print("Try again.")
        print("Enter your user name: ")
        user_name = input()
        print("Enter your password: ")
        password = input()
        login(user_name, password)
    elif yes_no == "y":
        go_back()
    else:
        responde()
        yes_no = input()
        cant_login(yes_no)

def sign_up(want_to_sign):
    if want_to_sign == "y":
        print("Insert your first name, last name, user name (make sure it has minimum seven characters and at least one digit) and password. ")
        input_data()
        sign(first_name, last_name, user_name, password)
    elif want_to_sign == "n":
        go_back()
    else:   
        responde()
        yes_no = input()
        sign_up(yes_no)

def log_in(want_to_login):
    if want_to_login == "y":
        print("Enter your user name: ")
        user_name = input()
        print("Enter your password: ")
        password = input()
        login(user_name, password)
    elif want_to_login == "n":
        go_back()
    else:   
        responde()
        yes_no = input()
        log_in(yes_no)

def identification(): # Menu for every role
    for element in main_list:
        if user_n == element[0] and element[4] == "manager":
            print("Welcome back, manager! What you want to do today? \n[0] change your informations \n[1] employ \n[2] add movies \n[3] delete movies \n[4] replace movies \n[5] add movie projection \n[6] delete movie projection \n[7] replace movie projection \n[8] generate movie appointments \n[9] see reports \n[10] sign out")
            option_manager = input()
            manager(option_manager)
        elif user_n == element[0] and element[4] == "seller":
            print("Welcome back, seller! Currently there are no tasks for you. \n[0] change your informations \n[1] reserve or buy new tickets \n[2] review tickets \n[3] cancel tickets \n[4] search tickets \n[5] change tickets \n[6] change reserved tickets to bought \n[7] cancel reservation for tickets 30 min before projection \n[8] sign out")
            option_seller = input()
            seller(option_seller)
    else:
        print("Welcome back! We are glad that you are using our website. What would you like to do today? \n[1] see movie options \n[2] change your information \n[3] book a ticket \n[4] sign out")
        option_user = input()
        user(option_user)

def manager(option_manager): # Manager menu options
    list_max = []
    if option_manager == "0":
        change_info()
    elif option_manager == "1":
        print("Insert worker's first name, last name, user name (make sure it has minimum seven characters and at least one digit), password and his job (seller or manager). ")
        input_data()
        input_worker()
        manager_employ(first_name, last_name, user_name, password, worker)
    elif option_manager == "10":
        go_back()
    elif option_manager == "2":
        movies()
        change_movie()
        for element in movie_list:
            list_max.append(int(element[0]))
        index = max(list_max)+1
        movie_list.append([index, movie_name, genre, duration, director, main_actors, origin_country, release_year])
        print("Enter movie description:")
        description_of_movie = input()
        movie_description_list.append([index, description_of_movie])
        choose_option_manager()
    elif option_manager == "3":
        movies()
        delete_all_data_movie()
        for element in movie_description_list:
            if movie_index == element[0]:
                movie_description_list.remove(element)
        choose_option_manager()
    elif option_manager == "4":
        movies()
        delete_movie()
        change_movie()
        movie_list.append([movie_index, movie_name, genre, duration, director, main_actors, origin_country, release_year])
        for element in movie_description_list:
            if movie_index == element[0]:
                movie_description_list.remove(element)
        for element in projections_list:
            if movie_name_change == element[5]:
                index_change = element[0]
                hall_change = element[1]
                starting_time_change = element[2]
                ending_time_change = element[3]
                weekday_change = element[4]
                price_change = element[6]
                projections_list.remove(element)
                projections_list.append([index_change, hall_change, starting_time_change, ending_time_change, weekday_change, movie_name, price_change])
        print("Enter movie description:")
        description_of_movie = input()
        movie_description_list.append([movie_index, description_of_movie])
        choose_option_manager()
    elif option_manager == "5":
        add_projections()
        for element in projections_list:
            list_max.append(int(element[0]))
        projection_index = max(list_max)+1
        projections_list.append([projection_index, projection_hall, projection_starting_time, projection_ending_time, projection_days_of_week, projection_movie_name, projection_price])
        choose_option_manager()
    elif option_manager == "6":
        projections_manager()
        delete_projections()
        choose_option_manager()
    elif option_manager == "7":
        projections_manager()
        delete_projections()
        add_projections()
        projections_list.append([index_delete_projection, projection_hall, projection_starting_time, projection_ending_time, projection_days_of_week, projection_movie_name, projection_price])
        choose_option_manager()
    elif option_manager == "8":
        generate_movie_appointments()
        choose_option_manager()
    elif option_manager == "9":
        reports()
    else:
        responde1()
        option_manager = input()
        manager(option_manager)

def reports():
    print("Choose the report you want to see:" 
            "\n[a] list of sold tickets for the selected sale date"
            "\n[b] list of sold tickets for the selected date of the cinema screening"
            "\n[c] list of sold tickets for the selected sale date and the selected seller" 
            "\n[d] total number and total price of tickets sold for the selected day (of the week)" 
            "\n[e] total number and total price of tickets sold for the selected day (of the week) holding the projection" 
            "\n[f] the total price of tickets sold for a given film in all screenings" 
            "\n[g] total number and total price of tickets sold for the selected day of sale and selected seller" 
            "\n[h] total number and total price of sold tickets by sellers (for each seller) in the last 30 days" 
            "\n[0] go back ")
    report_option = input()
    if report_option == "a":
        report_a()
    elif report_option == "b":
        report_b()
    elif report_option == "c":
        report_c()
    elif report_option == "d":
        report_d()
    elif report_option == "e":
        report_e()
    elif report_option == "f":
        report_f()
    elif report_option == "g":
        report_g()
    elif report_option == "h":
        report_h()
    elif report_option == "0":
        choose_option_manager()
    else:
        responde1()
        reports()

def report_a():
    global report_a_valid
    date_validation()
    print(f"{'Customer name':^30}{'Appointment':^17}{'Seat':^10}{'Date':^17}{'Seller':^30}")
    for element in ticket_seller_list:
        element_date = datetime.strptime(element[3], "%d.%m.%Y.")
        if date_report_str.date() == element_date.date():
            print(f"{element[0]:^30}{element[1]:^17}{element[2]:^10}{element[3]:^17}{element[4]:^30}")
            report_a_list.append(element)
    if not report_a_list:
        print("\nThere is no data for that date.")
        do_again_action()
        if loop is False:
            reports()
        else:
            report_a()
    else:
        print("Do you want to save the list in text file? \n[y] yes \n[n] no")
        yes_no = input()
        if yes_no == "y":
            report_a_valid = True
            reports()
        elif yes_no == "n":
            reports()
        else:
            responde()
            report_a()

def date_validation():
    global date_report_str
    print("Enter the date (format 12.12.2012.) for list that you want to see:")
    date_report = input()
    try:
        date_report_str = datetime.strptime(date_report, "%d.%m.%Y.")
    except ValueError:
        print("Invalid date format.")
        date_validation()

def report_b():
    global report_b_valid
    print("Enter the appointment for list that you want to see:")
    appointment_report = input()
    print(f"{'Customer name' : ^30}{'Appointment' : ^17}{'Seat' : ^10}{'Date' : ^17}{'Seller' : ^30}")
    for element in ticket_seller_list:
        if appointment_report == element[1]:
            print(f"{element[0] : ^30}{element[1]: ^17}{element[2] : ^10}{element[3] : ^17}{element[4] : ^30}")
            report_b_list.append(element)
    if not report_b_list:
        print("\nInvalid information!")
        do_again_action()
        if loop is False:
            reports()
        else:
            report_b()
    else:
        print("Do you want to save the list in text file? \n[y] yes \n[n] no")
        yes_no = input()
        if yes_no == "y":
            report_b_valid = True
            reports()
        elif yes_no == "n":
            reports()
        else:
            responde()
            report_b()

def report_c():
    global report_c_valid
    date_validation()
    print("Enter seller's name:")
    seller_name = input()
    print(f"{'Customer name' : ^30}{'Appointment' : ^17}{'Seat' : ^10}{'Date' : ^17}{'Seller' : ^30}")
    for element in ticket_seller_list:
        element_date = datetime.strptime(element[3], "%d.%m.%Y.")
        if date_report_str.date() == element_date.date() and seller_name == element[4]:
            print(f"{element[0] : ^30}{element[1]: ^17}{element[2] : ^10}{element[3] : ^17}{element[4] : ^30}")
            report_c_list.append(element)
    if not report_c_list:
        print("\nInvalid information!")
        do_again_action()
        if loop is False:
            reports()
        else:
            report_c()
    else:
        print("Do you want to save the list in text file? \n[y] yes \n[n] no")
        yes_no = input()
        if yes_no == "y":
            report_c_valid = True
            reports()
        elif yes_no == "n":
            reports()
        else:
            responde()
            report_c()

def date_checking(input_date): # Getting the day of the week
    global day_of_week
    date_object = datetime.strptime(input_date, "%d.%m.%Y.")
    day_of_week = date_object.weekday()
    return day_of_week

def report_d():
    global report_d_valid
    print("Enter the day of the week of buying ticket for list that you want to see: \n[0] Monday \n[1] Tuesday \n[2] Wednesday \n[3] Thursday \n[4] Friday \n[5] Saturday \n[6] Sunday")
    week_report = input()
    if week_report == "0":
        week_report = 0
    elif week_report == "1":
        week_report = 1
    elif week_report == "2":
        week_report = 2
    elif week_report == "3":
        week_report = 3
    elif week_report == "4":
        week_report = 4
    elif week_report == "5":
        week_report = 5
    elif week_report == "6":
        week_report = 6
    else:
        responde1()
        report_d()
    number_of_tickets = 0
    total_price = 0
    print(f"{'Number of sold tickets' : ^26}{'Total ticket sale (RSD)' : ^26}")
    for element in ticket_seller_list:
        day_of_week = date_checking(element[3])
        if week_report == day_of_week:
            number_of_tickets += 1
            for item in projections_list:
                if item[0] in element[1]:
                    discount(element[0])
                    if discount_valid == True:
                        total_price += 90*float(item[6])/100
                    else:
                        total_price += float(item[6])
    if not number_of_tickets == 0:
        print(f"{number_of_tickets : ^26}{total_price : ^26}")
        report_d_list.append([number_of_tickets, total_price])
        print("Do you want to save the list in text file? \n[y] yes \n[n] no")
        yes_no = input()
        if yes_no == "y":
            report_d_valid = True
            reports()
        elif yes_no == "n":
            reports()
        else:
            responde()
            report_d()
    else:
        print("\nInvalid information!")
        do_again_action()
        if loop is False:
            reports()
        else:
            report_d()

def report_e():
    global report_e_valid
    print("Enter the day of the week of appointment for list that you want to see: \n[0] Monday \n[1] Tuesday \n[2] Wednesday \n[3] Thursday \n[4] Friday \n[5] Saturday \n[6] Sunday")
    week_report = input()
    if week_report == "0":
        week_report = 0
    elif week_report == "1":
        week_report = 1
    elif week_report == "2":
        week_report = 2
    elif week_report == "3":
        week_report = 3
    elif week_report == "4":
        week_report = 4
    elif week_report == "5":
        week_report = 5
    elif week_report == "6":
        week_report = 6
    else:
        responde1()
        report_e()
    number_of_tickets = 0
    total_price = 0
    print(f"{'Number of sold tickets' : ^26}{'Total ticket sale (RSD)' : ^26}")
    for element1 in ticket_seller_list:
        for element2 in appointment_list:
            if element1[1] == element2[0]:
                day_of_week = date_checking(element2[1])
                if week_report == day_of_week:
                    number_of_tickets += 1
                    for item in projections_list:
                        if item[0] in element1[1]:
                            discount(element1[0])
                            if discount_valid == True:
                                total_price += 90*float(item[6])/100
                            else:
                                total_price += float(item[6])   
    if not number_of_tickets == 0:
        print(f"{number_of_tickets : ^26}{total_price : ^26}")
        report_e_list.append([number_of_tickets, total_price])
        print("Do you want to save the list in text file? \n[y] yes \n[n] no")
        yes_no = input()
        if yes_no == "y":
            report_e_valid = True
            reports()
        elif yes_no == "n":
            reports()
        else:
            responde()
            report_e()
    else:
        print("\nInvalid information!")
        do_again_action()
        if loop is False:
            reports()
        else:
            report_e()

def report_f():
    global report_f_valid
    print("Enter the movie name for tickets you want to see:")
    movie_name_report = input()
    total_price = 0
    print(f"{'Total ticket sale (RSD)' : ^26}")
    for element1 in ticket_seller_list:
        for element2 in appointment_list:
            for element3 in projections_list:
                if element1[1] == element2[0] and element3[0] in element1[1] and movie_name_report in element3[5]:
                    discount(element1[0])
                    if discount_valid == True:
                        total_price += 90*float(element3[6])/100
                    else:
                          total_price += float(element3[6])
    if not total_price == 0:
        print(f"{total_price : ^26}")
        report_f_list.append([total_price])
        print("Do you want to save the list in text file? \n[y] yes \n[n] no")
        yes_no = input()
        if yes_no == "y":
            report_f_valid = True
            reports()
        elif yes_no == "n":
            reports()
        else:
            responde()
            report_f()
    else:
        print("\nInvalid information!")
        do_again_action()
        if loop is False:
            reports()
        else:
            report_f()

def report_g():
    global report_g_valid
    print("Enter the day of the week of appointmnt for list that you want to see: \n[0] Monday \n[1] Tuesday \n[2] Wednesday \n[3] Thursday \n[4] Friday \n[5] Saturday \n[6] Sunday")
    week_report = input()
    print("Choose the seller:")
    seller_name = input()
    if week_report == "0":
        week_report = 0
    elif week_report == "1":
        week_report = 1
    elif week_report == "2":
        week_report = 2
    elif week_report == "3":
        week_report = 3
    elif week_report == "4":
        week_report = 4
    elif week_report == "5":
        week_report = 5
    elif week_report == "6":
        week_report = 6
    else:
        responde1()
        report_g()
    number_of_tickets = 0
    total_price = 0
    print(f"{'Number of sold tickets' : ^26}{'Total ticket sale (RSD)' : ^26}")
    for element1 in ticket_seller_list:
        for element2 in appointment_list:
            if element1[1] == element2[0]:
                day_of_week = date_checking(element1[3])
                if week_report == day_of_week and seller_name == element1[4]:
                    number_of_tickets += 1
                    for item in projections_list:
                        if item[0] in element1[1]:
                            discount(element1[0])
                            if discount_valid == True:
                                total_price += 90*float(item[6])/100
                            else:
                                total_price += float(item[6])
    if not number_of_tickets == 0:
        print(f"{number_of_tickets : ^26}{total_price : ^26}")
        report_g_list.append([number_of_tickets, total_price])
        print("Do you want to save the list in text file? \n[y] yes \n[n] no")
        yes_no = input()
        if yes_no == "y":
            report_g_valid = True
            reports()
        elif yes_no == "n":
            reports()
        else:
            responde()
            report_g()
    else:
        print("\nInvalid information!")
        do_again_action()
        if loop is False:
            reports()
        else:
            report_g()

def report_h():
    global report_h_valid
    print("Choose the seller:")
    seller_name = input()
    number_of_tickets = 0
    total_price = 0
    print(f"{'Number of sold tickets' : ^26}{'Total ticket sale (RSD)' : ^26}")
    for element in ticket_seller_list:
        date_checking_report(element[3])
        if seller_name == element[4] and date_valid == True:
            number_of_tickets += 1
            for item in projections_list:
                if item[0] in element[1]:
                    discount(element[0])
                    if discount_valid == True:
                        total_price += 90*float(item[6])/100
                    else:
                        total_price += float(item[6])
    if not number_of_tickets == 0:
        print(f"{number_of_tickets : ^26}{total_price : ^26}")
        report_h_list.append([number_of_tickets, total_price])
        print("Do you want to save the list in text file? \n[y] yes \n[n] no")
        yes_no = input()
        if yes_no == "y":
            report_h_valid = True
            reports()
        elif yes_no == "n":
            reports()
        else:
            responde()
            report_h()
    else:
        print("\nInvalid information!")
        do_again_action()
        if loop is False:
            reports()
        else:
            report_h()

def date_checking_report(target_time): # Cheking if input date as variable in this function is in the past 30 days
    global date_valid
    date_valid = False
    ticket_time = datetime.strptime(target_time, "%d.%m.%Y.")
    current_time = datetime.now()
    time_difference = current_time - ticket_time 
    if time_difference < timedelta(days = 30):
        date_valid = True
    else:
        pass

def manager_employ(first_name, last_name, user_name, password, worker):
    for element in main_list:
        if  user_name == element[0]:
            print("That user name has been already taken. Try again.")
            input_data()
            input_worker()
            manager_employ(first_name, last_name, user_name, password, worker)
    file.close()
    if not any(char.isdigit() for char in user_name):
        print("You need to make user name with at least one digit. Try again.")
        input_data()
        input_worker()
        manager_employ(first_name, last_name, user_name, password, worker)
    if len(user_name)<=6:
        print("You need to make user name with minimum seven characters. Try again.")
        input_data()
        input_worker()
        manager_employ(first_name, last_name, user_name, password, worker)
    if worker == "seller":
        main_list.append([user_name, password, first_name, last_name, worker])
        print("You have successfully hired an employee. \n")
        choose_option_manager()
    elif worker == "manager":
        main_list.append([user_name, password, first_name, last_name, worker])
        print("You have successfully hired an employee. \n")
        choose_option_manager()
    else:
        print("Please enter manager or seller as a job for worker.")
        input_data()
        input_worker()
        manager_employ(first_name, last_name, user_name, password, worker)

def seller(option_seller): # Seller's options from menu
    if option_seller == "0":
        change_info()
    elif option_seller == "1":
        book_tickets()
        seller_menu()
    elif option_seller == "2":
        review__all_tickets()
        seller_menu()
    elif option_seller == "3":
        review__all_tickets()
        canceling_all_tickets()
    elif option_seller == "4":
        search_tickets()
        seller_menu()
    elif option_seller == "5":
        change_all_tickets()
        seller_menu()
    elif option_seller == "6":
        buying_tickets()
        seller_menu()
    elif option_seller == "7":
        change_reservations()
        seller_menu()
    elif option_seller == "8":
        go_back()
    else:
        responde1()
        option_seller = input()
        seller(option_seller)

def buying_tickets(): # Changing reserved tickets to bought
    global canceling_appointment
    print("Do you want to se all reserved tickets? \n[y] yes \n[n] no")
    yes_no = input()
    if yes_no == "y":
        print(f"{'Customer name' : ^30}{'Appointment' : ^17}{'Seat' : ^10}{'Date' : ^17}")
        for element in ticket_list:
            if element[4] == "reserved":
                print(f"{element[0] : ^30}{element[1]: ^17}{element[2] : ^10}{element[3] : ^17}")
    elif yes_no == "n":
        pass
    else:
        responde()
        buying_tickets()
    print("Enter the appointment of ticket you want to buy:")
    canceling_appointment = input()
    change_tickets_valid_appointment(canceling_appointment)
    canceling_valid_seat()
    for element in ticket_list:
        if canceling_appointment == element[1] and seat_cancel == element[2] and element[4] == "reserved":
            ticket_list.remove(element)
            date_today = datetime.today().strftime("%d.%m.%Y.")
            ticket_list.append([element[0], element[1], element[2], date_today, "bought"])
            ticket_seller_list.append([element[0], element[1], element[2], date_today, user_n])
            print("Ticket have been changed!")
            do_again_action()
            if loop is False:
                seller_menu()
            else:
                buying_tickets()
    else:
        print("Invalid ticket data!")
        do_again_action()
        if loop is False:
            seller_menu()
        else:
            buying_tickets()

def checking_time_past_30_min(target_time):
    global projection_late
    projection_late = False
    projection_time = datetime.strptime(target_time, "%d.%m.%Y. %H:%M")
    current_time = datetime.now()
    time_difference = projection_time - current_time 
    if time_difference < timedelta(minutes=30):
        projection_late = True
    else:
        pass

def change_reservations(): # Canceling resevations that are less than 30 min before the projection time
    for element1 in projections_list:
        for element2 in ticket_list:
            if element1[0] in element2[1] and element2[4] == "reserved":
                projection_time = element2[3] + " " + element1[2]
                checking_time_past_30_min(projection_time)
                if projection_late == True:
                    ticket_list.remove(element2)

def book_tickets(): # Booking (bought or reserved) tickets
    global name_for_booking
    global appointment_for_booking
    print("Do you want to see all appointments? \n[y] yes \n[n] no")
    see_all_appointments = input()
    if see_all_appointments == "y":
        ticket_user()
    elif see_all_appointments == "n":
        pass
    else:
        responde()
        book_tickets()
    print("Insert the first and last name of not registered user or user name of registered user:")
    name_for_booking = input()
    book_tickets_valid_appointment()

def book_tickets_valid_appointment():
    global appointment
    print("Pick the appointment for ticket:")
    appointment = input()
    appointment_for_booking_valid = False
    for element in combined_list:
        projection_time =  element[1] + " " + element[3]
        checking_time_past_30_min(projection_time)
        if appointment == element[0] and projection_late == False:
            hall = element[2]
            appointment_for_booking_valid = True
            break
    if appointment_for_booking_valid == True:  
        for element in hall_list:
            if hall == element[0]:
                rows = int(element[2])
                cols = len(element[3])
        alphabet = string.ascii_uppercase
        matrix = [[alphabet[i % len(alphabet)] for i in range(cols)] for _ in range(rows)]
        positions_to_mark = []
        for element in ticket_list:
            if appointment == element[1]:
                positions_to_mark.append([int(element[2][0])-1, ord(element[2][1].upper()) - ord('A')])
        for row, col in positions_to_mark:
            matrix[row][col] = 'X'
        for row in matrix:
            print(" ".join(str(cell) for cell in row))
        choosing_valid_seat()
    else:
        print("Invalid appontment!")
        do_again_action()
        if loop is False:
            seller_menu()
        else:
            book_tickets_valid_appointment()

def review__all_tickets():
    print(f"{'Appointment' : ^21}{'Customer' : ^30}{'Movie name' : ^30}{'Date' : ^17}{'Starting time' : ^19}{'Ending time' : ^19}{'Seat' : ^10}{'Booking' : ^17}"+"\n")
    for element1 in ticket_list:
        for element2 in projections_list:
            if element2[0] in element1[1]:
                print(f"{element1[1] : ^21}{element1[0] : ^30}{element2[5] : ^30}{element1[3] : ^17}{element2[2] : ^19}{element2[3] : ^19}{element1[2] : ^10}{element1[4] : ^17}") 

def search_tickets():
    global booking_type
    global date_search
    global starting_time
    global ending_time
    global projection_date
    booking_list = []
    print("[1] Appointemnt \n[2] First name or user name \n[3] Last name or user name \n[4] Date \n[5] Starting time \n[6] Ending time \n[7] Type of booking (reserved or bought)")
    print("Enter numbers of criteria you want to explore: ")
    criteria = input()
    if "1" in criteria:
        print("Enter appointment:")
        appointment_search = input()
    else:
        appointment_search = ""
    if "2" in criteria:
        print("Enter first name or user name:")
        first_name_search = input()
    else: 
        first_name_search = ""
    if "3" in criteria:
        print("Enter last name or user name:")
        last_name_search = input()
    else:
        last_name_search = ""
    if "4" in criteria:
        projection_date_validation()
    else:
        projection_date = ""
    if "5" in criteria:
        projection_starting_time_validation()
    else: 
        starting_time = "00:00"
    if "6" in criteria:
        projection_ending_time_validation()
    else:
        ending_time = "24:00"
    if "7" in criteria:   
        validation_booking_type()
    else:
        booking_type = ""
    if "1" not in criteria and "2" not in criteria and "3" not in criteria and "4" not in criteria and "5" not in criteria and "6" not in criteria and "7" not in criteria:
        print("You need to insert one of the numbers above.")
        movies_search()
    for element1 in projections_list:
        for element2 in ticket_list:
            if element1[0] in element2[1] and (appointment_search in element2[1].lower() or appointment_search in element2[1].upper()) and (first_name_search in element2[0].lower() or first_name_search in element2[0].upper()) and (last_name_search in element2[0].lower() or last_name_search in element2[0].upper()) and starting_time <= element1[2] and ending_time >= element1[3] and projection_date in element2[3] and booking_type in element2[4]:
                booking_list.append([element2[1], element2[0], element2[3], element1[2], element1[3], element2[4]])
    print(f"{'Appointment' : ^17}{'Customer' : ^30}{'Date' : ^17}{'Starting time' : ^19}{'Ending time' : ^19}{'Booking type' : ^19}"+"\n")
    for element in booking_list:
        print(f"{element[0] : ^17}{element[1] : ^30}{element[2] : ^17}{element[3] : ^19}{element[4] : ^19}{element[5] : ^19}")

def validation_booking_type():
    global booking_type
    print("Choose type of booking: \n [r] reserved \n [b] bought")  
    booking_type = input()
    if booking_type == "r":
        booking_type = "reserved"
    elif booking_type == "b":
        booking_type = "bought"
    else:
        responde1()
        validation_booking_type()

def change_all_tickets():
    global canceling_appointment
    global current_appointment
    global seat_cancel
    print("Choose the appointment of ticket you want to change:")
    canceling_appointment = input()
    change_tickets_valid_appointment(canceling_appointment)
    canceling_valid_seat()
    name_change_tickets()
    for element in ticket_list:
        if canceling_appointment == element[1] and seat_cancel == element[2] and name_change == element[0]:
            current_appointment = element[1]
            current_name = element[0]
            current_date = element[3]
            seat_cancel = element[2]
            current_booking = element[4]
            ticket_list.remove(element)
            print("What details you want to change? \n[1] appointment \n[2] seat \n[3] customer name")
            pick_option = input()
            if "1" in pick_option:
                print("Enter new appointment:") 
                current_appointment = input()
                change_tickets_valid_appointment(current_appointment)
            if "2" in pick_option:
                new_ticket()
            if "3" in pick_option:
                print("Enter new customer name or user name:")
                current_name = input()
            ticket_list.append([current_name, current_appointment, seat_cancel, current_date, current_booking])
            if current_booking == "bought":
                ticket_seller_list.append([current_name, current_appointment, seat_cancel, current_date, user_n])
            print("Your ticket have been changed.")
            do_again_action()
            if loop is False:
                seller_menu()
            else:
                change_all_tickets()
    else:
        print("That ticket is invalid!")
        do_again_action()
        if loop is False:
            seller_menu()
        else:
            change_all_tickets()

def new_ticket(): # Checking if ticket based on input data exists
    global current_appointment
    canceling_valid_seat()
    for element in ticket_list:
        if current_appointment == element[1] and seat_cancel == element[2]:
            print("This ticket is not available.")
            do_again_action()
            if loop is False:
                seller_menu()
            else:
                new_ticket()

def change_tickets_valid_appointment(appointment):
    global canceling_appointment
    appointment_change_valid = False
    for element in appointment_list:
        for item in projections_list:
            if appointment == element[0] and item[0] in element[0]:
                projection_time =  element[1] + " " + item[2]
                checking_time_past_30_min(projection_time)
                if projection_late == False:
                    appointment_change_valid = True
                    break
    if appointment_change_valid == True:
        return
    else:
        print("Invalid appontment!")
        do_again_action()
        if loop is False:
            seller_menu()
        else:
            canceling_appointment = input()
            change_tickets_valid_appointment(canceling_appointment)

def name_change_tickets(): # Cheking if that name exists on the list of tickets
    global name_change
    print("Enter name of the customer:")
    name_change = input()
    for element in ticket_list:
        if element[0] == name_change:
            return
    else:
        print("There isn't that name in data. Do you want to try again? \n[1] try again \n[2] go back")
        try_again = input()
        if try_again == "1":
            name_change_tickets()
        elif try_again == "2":
            seller_menu()
        else:
            responde1()
            name_change_tickets()

def user(option_user): # Registered user's options from menu
    if option_user == "1":
        review_movie_list()
    elif option_user == "2":
        change_info()
    elif option_user == "3":
        book_ticket()
    elif option_user == "4":
        go_back()
    else:
        responde1()
        option_user = input()
        user(option_user)

def review_movie_list(): # Movies in cinema
    file_path = "Movies.txt"
    print(f"{'Welcome to our wonderland of movies!' : ^152}"+"\n"+f"{'This is the list of movies that are currently available in our cinema:' : ^152}"+"\n")
    movies()
    movies_choose()

def movie_option(movie_options):
    if movie_options == "0":
        movies()
        movies_choose()
    elif movie_options == "1":
        view_movie_info()
    elif movie_options == "2":
        movies_search()
        movies_choose()
    elif movie_options == "3":
        movies_projections()
        movies_choose()
    elif movie_options == "4":
        for element in main_list:
            if user_n == element[0]:
                register_user_choose()
        else:
            beginning()
    else:
        responde1()
        movie_options = input()
        movie_option(movie_options)

def view_movie_info():
    print("Enter movie index:")
    movie_index = input()
    for element in movie_list:
        if movie_index == element[0]:
            print("Movie name: " + element[1])
            print("Genre: " + element[2])
            print("Duration: " + element[3])
            print("Director: " + element[4])
            print("Main actors: " + element[5])
            print("Country of origin: " + element[6])
            print("Year of release: " + element[7])
    for element in movie_description_list:
        if movie_index == element[0]:
            second_code_line = element[1]
            print("Movie description:" + "\n")
            for i in range(0, len(second_code_line), 80):
                print(second_code_line[i:i+80])
    movies_choose()    

def movies_search():
    global movie_year
    global max_duration
    global min_duration
    second_movie_list = []
    print("[1] Movie name \n[2] Genre \n[3] Duration \n[4] Director \n[5] Main actors \n[6] Country of origin \n[7] Year of release")
    print("Enter numbers of criteria you want to explore: ")
    criteria = input()
    if "1" in criteria:
        print("Enter movie name:")
        movie_names = input()
    else:
        movie_names = ""
    if "2" in criteria:
        print("Enter movie genre:")
        movie_genre = input()
    else: 
        movie_genre = ""
    if "3" in criteria:
        print("Enter maximum duration of the movie:")
        max_duration = input()
        duration_valid(max_duration)
        print("Enter minimum duration of the movie:")
        min_duration = input()
        duration_valid(min_duration)
    else:
        min_duration = 0
        max_duration = 1000000
    if "4" in criteria:
        print("Enter director's name and lastname:")
        director_of_movie = input()
    else:
        director_of_movie = ""
    if "5" in criteria:
        print("Enter main actors:")
        main_actor = input()
    else: 
        main_actor = ""
    if "6" in criteria:
        print("Enter country of origin:")
        country = input()
    else:
        country = ""
    if "7" in criteria:   
        movie_year_validation()
    else:
        movie_year = ""
    if "1" not in criteria and "2" not in criteria and "3" not in criteria and "4" not in criteria and "5" not in criteria and "6" not in criteria and "7" not in criteria:
        print("You need to insert one of the numbers above.")
        movies_search()
    for element in movie_list:
        if (movie_names in element[1].lower() or movie_names in element[1].upper()) and (movie_genre in element[2].lower() or movie_genre in element[2].upper()) and element[3] <= max_duration and element[3] >= min_duration and (director_of_movie in element[4].lower() or director_of_movie in element[4].upper()) and (main_actor in element[5].lower() or main_actor in element[5].upper()) and (country in element[6].lower() or country in element[6].upper()) and (movie_year in element[7].lower() or movie_year in element[7].upper()):
            second_movie_list.append(element)
    print(f"{'Index' : ^5}{'Movie name' : ^30}{'Genre' : ^8}{'Duration (min)' : ^14}{'Director' : ^22}{'Main actors' : ^43}{'Origin country' : ^18}{'Release year' : ^13}"+"\n")
    for element in second_movie_list:
        print(f"{element[0] : ^5}{element[1] : ^29}{element[2] : ^10}{element[3] : ^12}{element[4] : ^25}{element[5] : ^40}{element[6] : ^20}{element[7] : ^11}")
    choosing_to_see_index()

def movie_year_validation():
        global movie_year
        print("Enter release year of the movie:")  
        movie_year = input()
        if not valid_year_format(movie_year):
            print("\nInvalid year format! \nTry again:")
            movie_year_validation()

def choosing_to_see_index():
    print("Did you find your movie, if you did, you can insert index of it. \nDo you want to? \n[y] yes \n[n] no")
    yes_or_no = input()
    if yes_or_no == "y":
        view_movie_info()
    elif yes_or_no == "n":
        movies_choose()
    else:
        responde()
        choosing_to_see_index()

def movies_projections():
    print("\nSearch projection appointments by: \n[0] see all projection appointments \n[1] movie name \n[2] hall \n[3] date \n[4] starting time \n[5] ending time ")
    projection_options = input()
    projection_option(projection_options)

def projection_option(projection_options):
    global projection_date
    global starting_time
    global ending_time
    search_projection_list = []
    if "1" in projection_options:
        print("Enter movie name:")
        movie_name_projection = input()
    else:
        movie_name_projection = ""
    if "2" in projection_options:
        print("Enter hall you wanted to search:")
        hall = input()
    else:
        hall = ""
    if "3" in projection_options:
        projection_date_validation()
    else:
        projection_date = ""
    if "4" in projection_options:
        projection_starting_time_validation()
    else:
        starting_time = "00:00"
    if "5" in projection_options:
        projection_ending_time_validation()
    else:
        ending_time = "24:00"
    if "0" not in projection_options and "1" not in projection_options and "2" not in projection_options and "3" not in projection_options and "4" not in projection_options and "5" not in projection_options:
        responde1()
        projection_options = input()
        projection_option(projection_options)
    elif "0" in projection_options:
        projections_users()
    else:
        for element in combined_list:
            if (movie_name_projection in element[6].lower() or movie_name_projection in element[6].upper()) and (hall in element[2].lower() or hall in element[2].upper()) and starting_time <= element[3] and ending_time >= element[4] and projection_date in element[1]:
                search_projection_list.append(element)
        print(f"{'Movie name' : ^30}{'Hall' : ^30}{'Starting time' : ^30}{'Ending time' : ^30}{'Date' : ^15}")
        for element in search_projection_list:
            print(f"{element[6] : ^30}{element[2] : ^30}{element[3] : ^30}{element[4] : ^30}{element[1] : ^15}")

def projection_date_validation():
    global projection_date
    print("Enter date (for example 12.12.2012.):")
    projection_date = input()
    if not valid_date_format(projection_date):
        print("Invalid date format! \nTry again:")
        projection_date_validation()

def projection_starting_time_validation():
    global starting_time
    print("Enter starting time (for example 12:00):")
    starting_time = input()
    if not valid_time_format(starting_time):
        print("\nInvalid time format! \nTry again:")
        projection_starting_time_validation()

def projection_ending_time_validation():
    global ending_time
    print("Enter ending time (for example 12:00):")
    ending_time = input()
    if not valid_time_format(ending_time):
        print("\nInvalid time format! \nTry again:")
        projection_ending_time_validation()

def go_back():
    print("We will return you back to the main menu. \n")
    user_n = "none"
    beginning()

def registered_yet():
    print("Are you registered on our website? \n[y] yes \n[n] no")
    reg_of_user = input()
    if reg_of_user == "y": 
        print("Do you want to log in to our website? \n[y] yes \n[n] no") # Loging in to already existing account
        want_log_in = input()
        log_in(want_log_in)
    elif reg_of_user == "n":
        print("Do you want to sign up to our website? \n[y] yes \n[n] no") # Signing up to website
        want_sign_up = input()
        sign_up(want_sign_up)
    else:   
        responde()
        registered_yet()

def beginning():
    while True:
        print(f"{'Welcome to the official website of the cinema Movieland!' : ^152}") # main menu
        print("\nDo you want to see the list of movies that we have prepared for you or do you want to register to our website? \n[1] list of movies \n[2] register \n[3] exit")
        option = input()
        if option == "1": # Review the list of movies
            review_movie_list()
        elif option == "2": # Register to website
            registered_yet()
        elif option == "3": #Exiting the site
            exiting()
        else: 
            responde1()

def exiting():
    print("Are you sure you want to exit? \n[y] yes \n[n] no")
    want_to_exit = input()
    if want_to_exit == "y":
        print("We hope to see you soon...")
        for element in projections_list:
            today_date = datetime.today().strftime("%d.%m.%Y.")
            day_number = date_checking(today_date)
            price_special_days = float(element[6])
            if day_number == 1:
                price_special_days += 50
                element[6] = str(price_special_days)
            if day_number == 5 or day_number == 6:
                price_special_days -= 50
                element[6] = str(price_special_days)
        with open(file_path, "w", encoding="utf-8") as file:
            for element in main_list:
                file.write(f"{element[0]}|{element[1]}|{element[2]}|{element[3]}|{element[4]}\n")
        with open(file_path_description, "w", encoding="utf-8") as file:
            for element in movie_description_list:
                file.write(f"{element[0]}|{element[1]}\n")
        with open(file_path_movies, "w", encoding="utf-8") as file:
            for element in movie_list:
                file.write(f"{element[0]}|{element[1]}|{element[2]}|{element[3]}|{element[4]}|{element[5]}|{element[6]}|{element[7]}\n")
        with open(projection_path, "w", encoding="utf-8") as file:
            for element in projections_list:
                file.write(f"{element[0]}|{element[1]}|{element[2]}|{element[3]}|{element[4]}|{element[5]}|{element[6]}\n")
        with open(appointment_path, "w", encoding="utf-8") as file:
            for element in appointment_list:
                file.write(f"{element[0]}|{element[1]}\n")
        with open(ticket_path, "w", encoding="utf-8") as file:
            for element in ticket_list:
                file.write(f"{element[0]}|{element[1]}|{element[2]}|{element[3]}|{element[4]}\n")
        with open(hall_path, "w", encoding="utf-8") as file:
            for element in hall_list:
                file.write(f"{element[0]}|{element[1]}|{element[2]}|{element[3]}\n")
        with open(ticket_seller_path, "w", encoding="utf-8") as file:
            for element in ticket_seller_list:
                file.write(f"{element[0]}|{element[1]}|{element[2]}|{element[3]}|{element[4]}\n")
        if report_a_valid is True:
            with open(report_a_path, "w", encoding="utf-8") as file:
                for element in report_a_list:
                    file.write(f"{element[0]}|{element[1]}|{element[2]}|{element[3]}|{element[4]}\n")
        if report_b_valid is True:
            with open(report_b_path, "w", encoding="utf-8") as file:
                for element in report_b_list:
                    file.write(f"{element[0]}|{element[1]}|{element[2]}|{element[3]}|{element[4]}\n")
        if report_c_valid is True:
            with open(report_c_path, "w", encoding="utf-8") as file:
                for element in report_c_list:
                    file.write(f"{element[0]}|{element[1]}|{element[2]}|{element[3]}|{element[4]}\n")
        if report_d_valid is True:
            with open(report_d_path, "w", encoding="utf-8") as file:
                for element in report_d_list:
                    file.write(f"{element[0]}|{element[1]}\n")
        if report_e_valid is True:
            with open(report_e_path, "w", encoding="utf-8") as file:
                for element in report_e_list:
                    file.write(f"{element[0]}|{element[1]}\n")
        if report_f_valid is True:
            with open(report_f_path, "w", encoding="utf-8") as file:
                for element in report_f_list:
                    file.write(f"{element[0]}\n")
        if report_g_valid is True:
            with open(report_g_path, "w", encoding="utf-8") as file:
                for element in report_g_list:
                    file.write(f"{element[0]}|{element[1]}\n")
        if report_h_valid is True:
            with open(report_h_path, "w", encoding="utf-8") as file:
                for element in report_h_list:
                    file.write(f"{element[0]}|{element[1]}\n")
        exit()
    elif want_to_exit == "n":
        go_back()
    else:
        responde()
        exiting()
        
if __name__=='__main__':
    import string
    import re
    from datetime import datetime, timedelta, date
    
    global user_n 
    user_n = "none"
    global main_list
    main_list = []  
    global file_path
    file_path = "Users.txt"
    with open(file_path, "r", encoding="utf_8") as file:
        for line in file.readlines():
            values = line.strip().split("|")
            main_list.append(values)
    global movie_list
    movie_list = []
    global file_path_movies
    file_path_movies = "Movies.txt"
    with open(file_path_movies, "r", encoding = "utf-8") as file:
        for line in file.readlines():
            values = line.strip().split("|")
            movie_list.append(values)
    global movie_description_list
    movie_description_list = []
    global file_path_description
    file_path_description = "Movies description.txt" #Description is added on the list in beginning so it can be used later
    with open(file_path_description, "r", encoding = "utf-8") as file:
        for line in file.readlines():
            values = line.strip().split("|")
            movie_description_list.append(values)
    global projections_list
    projections_list = []  
    global projection_path
    projection_path = "Movie projections.txt"
    with open(projection_path, "r", encoding="utf_8") as file:
        for line in file.readlines():
            values = line.strip().split("|")
            projections_list.append(values)
    global appointment_list
    appointment_list = []  
    global appointment_path
    appointment_path = "Movie projection appointments.txt"
    with open(appointment_path, "r", encoding="utf_8") as file:
        for line in file.readlines():
            values = line.strip().split("|")
            appointment_list.append(values)
    ticket_list = []  
    global ticket_path
    ticket_path = "Ticket.txt"
    with open(ticket_path, "r", encoding="utf_8") as file:
        for line in file.readlines():
            values = line.strip().split("|")
            ticket_list.append(values)
    hall_list = []  
    global hall_path
    hall_path = "Movie hall.txt"
    with open(hall_path, "r", encoding="utf_8") as file:
        for line in file.readlines():
            values = line.strip().split("|")
            hall_list.append(values)
    global combined_list
    combined_list = []
    for elem2 in projections_list:
            for elem1 in appointment_list:
                if elem2[0] in elem1[0]:
                    combined_list.append(elem1 + elem2[1:])
    global report_a_list
    report_a_list = []  
    global report_a_path
    report_a_path = "Report a.txt"
    with open(report_a_path, "r", encoding="utf_8") as file:
        for line in file.readlines():
            values = line.strip().split("|")
            report_a_list.append(values)
    global report_b_list
    report_b_list = []  
    global report_b_path
    report_b_path = "Report b.txt"
    with open(report_b_path, "r", encoding="utf_8") as file:
        for line in file.readlines():
            values = line.strip().split("|")
            report_b_list.append(values)
    global report_c_list
    report_c_list = []  
    global report_c_path
    report_c_path = "Report c.txt"
    with open(report_c_path, "r", encoding="utf_8") as file:
        for line in file.readlines():
            values = line.strip().split("|")
            report_c_list.append(values)
    global report_d_list
    report_d_list = []  
    global report_d_path
    report_d_path = "Report d.txt"
    with open(report_d_path, "r", encoding="utf_8") as file:
        for line in file.readlines():
            values = line.strip().split("|")
            report_d_list.append(values)
    global report_e_list
    report_e_list = []  
    global report_e_path
    report_e_path = "Report e.txt"
    with open(report_e_path, "r", encoding="utf_8") as file:
        for line in file.readlines():
            values = line.strip().split("|")
            report_e_list.append(values)
    global report_f_list
    report_f_list = []  
    global report_f_path
    report_f_path = "Report f.txt"
    with open(report_f_path, "r", encoding="utf_8") as file:
        for line in file.readlines():
            values = line.strip().split("|")
            report_f_list.append(values)
    global report_g_list
    report_g_list = []  
    global report_g_path
    report_g_path = "Report g.txt"
    with open(report_g_path, "r", encoding="utf_8") as file:
        for line in file.readlines():
            values = line.strip().split("|")
            report_g_list.append(values)
    global report_h_list
    report_h_list = []  
    global report_h_path
    report_h_path = "Report h.txt"
    with open(report_h_path, "r", encoding="utf_8") as file:
        for line in file.readlines():
            values = line.strip().split("|")
            report_h_list.append(values)
    global ticket_seller_list
    ticket_seller_list = []
    global ticket_seller_path
    ticket_seller_path = "Ticket seller list.txt"
    with open(ticket_seller_path, "r", encoding="utf_8") as file:
        for line in file.readlines():
            values = line.strip().split("|")
            ticket_seller_list.append(values)
    for element in projections_list:
        today_date = datetime.today().strftime("%d.%m.%Y.")
        day_number = date_checking(today_date)
        price_special_days = float(element[6])
        if day_number == 1:
            price_special_days -= 50
            element[6] = str(price_special_days)
        if day_number == 5 or day_number == 6:
            price_special_days += 50
            element[6] = str(price_special_days)
    global report_a_valid
    report_a_valid = False
    global report_b_valid
    report_b_valid = False
    global report_c_valid
    report_c_valid = False
    global report_d_valid
    report_d_valid = False
    global report_e_valid
    report_e_valid = False
    global report_f_valid
    report_f_valid = False
    global report_g_valid
    report_g_valid = False
    global report_h_valid
    report_h_valid = False
    beginning()