import random
import string

# List of dialogues with their respective movies
actors_movies = {
    "Leonardo DiCaprio": ["Inception", "Titanic", "The Revenant"],
    "Scarlett Johansson": ["Avengers", "Lost in Translation", "Marriage Story"],
    "Robert Downey Jr.": ["Iron Man", "Sherlock Holmes", "Chaplin"],
    "Meryl Streep": ["The Devil Wears Prada", "Sophie's Choice", "Mamma Mia!"],
    "Denzel Washington": ["Training Day", "Glory", "Fences"],
    "Angelina Jolie": ["Maleficent", "Wanted", "Salt"],
    "Tom Hanks": ["Forrest Gump", "Cast Away", "Saving Private Ryan"],
    "Jennifer Lawrence": ["The Hunger Games", "Silver Linings Playbook", "Red Sparrow"],
    "Will Smith": ["Men in Black", "The Pursuit of Happyness", "Ali"],
    "Natalie Portman": ["Black Swan", "V for Vendetta", "Thor"],
    "Aamir Khan": ["Dangal", "PK", "3 Idiots"],
    "Shah Rukh Khan": ["Dilwale Dulhania Le Jayenge", "My Name Is Khan", "Chennai Express"],
    "Salman Khan": ["Bajrangi Bhaijaan", "Tiger Zinda Hai", "Sultan"],
    "Hrithik Roshan": ["Koi... Mil Gaya", "Zindagi Na Milegi Dobara", "War"],
    "Deepika Padukone": ["Padmaavat", "Chennai Express", "Piku"],
    "Ranbir Kapoor": ["Sanju", "Yeh Jawaani Hai Deewani", "Ajab Prem Ki Ghazab Kahani"],
    "Priyanka Chopra": ["Baywatch", "Bajirao Mastani", "The White Tiger"],
    "Akshay Kumar": ["Housefull", "Padman", "Mission Mangal"],
    "Sonakshi Sinha": ["Dabangg", "Rowdy Rathore", "Akira"],
    "John Wick": ["John Wick", "John Wick: Chapter 2", "John Wick: Chapter 3 – Parabellum"],
    "Chris Hemsworth": ["Thor", "The Avengers", "Extraction"],
    "Gal Gadot": ["Wonder Woman", "Justice League", "Fast & Furious 7"],
    "Chris Evans": ["Captain America", "The Avengers", "Avengers: Endgame"],
    "Emma Watson": ["Harry Potter", "Beauty and the Beast", "Little Women"],
    "Robert Pattinson": ["Twilight", "The Batman", "Tenet"],
    "Brie Larson": ["Captain Marvel", "Room", "Short Term 12"],
    "Tom Holland": ["Spider-Man", "The Avengers", "Uncharted"],
    "Zendaya": ["Euphoria", "Spider-Man", "Dune"],
    "Henry Cavill": ["Superman", "The Witcher", "Mission: Impossible – Fallout"],
    "Margot Robbie": ["The Wolf of Wall Street", "I, Tonya", "Birds of Prey"],
    "Ryan Reynolds": ["Deadpool", "The Hitman's Bodyguard", "Free Guy"],
    "Sandra Bullock": ["The Blind Side", "Gravity", "Speed"],
    "Keanu Reeves": ["John Wick", "The Matrix", "Speed"],
    "Charlize Theron": ["Mad Max: Fury Road", "Monster", "Atomic Blonde"],
    "Viola Davis": ["The Help", "Fences", "Ma Rainey's Black Bottom"],
    "Jennifer Aniston": ["Friends", "Marley & Me", "The Morning Show"],
    "Ben Affleck": ["Batman v Superman", "The Accountant", "Argo"],
    "Emma Stone": ["La La Land", "The Help", "Cruella"],
    "Mark Ruffalo": ["The Avengers", "Shutter Island", "Spotlight"],
    "Reese Witherspoon": ["Legally Blonde", "Walk the Line", "Wild"],
    "Christian Bale": ["Batman", "The Dark Knight", "Vice"],
    "Ranveer Singh": ["Gully Boy", "Bajirao Mastani", "Padmaavat"],
    "Alia Bhatt": ["Raazi", "Highway", "Gully Boy"],
    "Varun Dhawan": ["Student of the Year", "Badlapur", "Street Dancer 3D"],
    "Katrina Kaif": ["Zindagi Na Milegi Dobara", "Jab Tak Hai Jaan", "Tiger Zinda Hai"],
    "Shraddha Kapoor": ["Aashiqui 2", "Street Dancer 3D", "Haider"],
    "Sidharth Malhotra": ["Student of the Year", "Kapoor & Sons", "Shershaah"],
    "Kareena Kapoor Khan": ["Kabhi Khushi Kabhie Gham", "Tanu Weds Manu", "Jab We Met"],
    "Priyanka Chopra Jonas": ["Don", "Bajirao Mastani", "Quantico (TV)"],
    "Jacqueline Fernandez": ["Kick", "Race 2", "Housefull 3"],
    "Hrithik Roshan": ["Jodha Akbar", "War", "Bang Bang!"],
    "Anushka Sharma": ["PK", "Ae Dil Hai Mushkil", "Sultan"],
    "Vicky Kaushal": ["Uri: The Surgical Strike", "Raazi", "Masaan"],
    "Ayushmann Khurrana": ["Vicky Donor", "Andhadhun", "Article 15"],
    "Rajkummar Rao": ["Stree", "Bareilly Ki Barfi", "Newton"],
    "Kartik Aaryan": ["Pyaar Ka Punchnama", "Sonu Ke Titu Ki Sweety", "Bhool Bhulaiyaa 2"],
    "Taapsee Pannu": ["Pink", "Badla", "Thappad"],
    "Deepika Padukone": ["Chennai Express", "Padmaavat", "Cocktail"],
    "Ileana D'Cruz": ["Barfi!", "Rustom", "Main Tera Hero"],
    "Sushant Singh Rajput": ["Kai Po Che!", "Chhichhore", "Dil Bechara"],
    "Nawazuddin Siddiqui": ["Gangs of Wasseypur", "The Lunchbox", "Sacred Games (TV)"],
    "Radhika Apte": ["Lal Kaptaan", "Andhadhun", "Sacred Games (TV)"],
    "Neha Dhupia": ["Qayamat", "Chup Chup Ke", "Tumhari Sulu"],
    "Rishi Kapoor": ["Kapoor & Sons", "Agneepath", "Mulk"],
    "Boman Irani": ["Munna Bhai M.B.B.S.", "3 Idiots", "Khosla Ka Ghosla"],
    "Manoj Bajpayee": ["Satya", "The Family Man (TV)", "Gangs of Wasseypur"],
    "Farhan Akhtar": ["Zindagi Na Milegi Dobara", "Rock On!!", "Bhaag Milkha Bhaag"],
    "Madhuri Dixit": ["Dil To Pagal Hai", "Devdas", "Gulaab Gang"],
    "Sonam Kapoor": ["Neerja", "Raanjhanaa", "Khoobsurat"],
    "Samantha Ruth Prabhu": ["Rangasthalam", "Vijetha", "Mahanati"],
    "Kangana Ranaut": ["Queen", "Tanu Weds Manu", "Manikarnika: The Queen of Jhansi"],
}


# ANSI escape codes for coloring text
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

# Function for Caesar cipher encryption
def caesar_cipher(message, key, direction=1):
    final_message = ''
    for char in message:
        if char.isalpha():
            # Shift within the bounds of the alphabet
            offset = 65 if char.isupper() else 97
            new_char = chr((ord(char) - offset + key * direction) % 26 + offset)
            final_message += new_char
        else:
            final_message += char
    return final_message

def encrypt(message, key):
    return caesar_cipher(message, key)

# Function to display the result with colored text
def display_result(user_progress, quote, encrypted_quote):
    result_display = ""
    for idx, char in enumerate(user_progress):
        if char != '_':
            result_display += GREEN + char + RESET + ' '
        else:
            result_display += '_ '
    print(result_display.strip())
    print(' '.join(encrypted_quote))

# Function to provide a hint
def provide_hint(user_progress, quote, actor_name, movies):
    # Find the first unguessed letter
    for idx, char in enumerate(quote):
        if user_progress[idx] == '_':
            # Provide the hint with the movie
            movie = random.choice(movies)
            return f"Hint: The actor stars in the movie '{movie}'."
    return "All letters guessed correctly so far!"

# Function to update the user's progress
def update_progress(user_guess, user_progress, quote):
    new_progress = list(user_progress)
    for idx, char in enumerate(quote):
        if user_guess[idx].lower() == char.lower():
            new_progress[idx] = char
    return ''.join(new_progress)

# Main game function
def main():
    # Select a random dialogue
    quote, movie = random.choice(list(actors_movies.items()))
    shift_key = random.randint(1, 21000)  # Caesar cipher shift key

    # Encrypt the selected quote
    encrypted_quote = encrypt(quote, shift_key)

    # Initialize user progress with underscores
    user_progress = ''.join(['_' if char.isalpha() else char for char in quote])
    print("WELCOME TO THE GUESSING GAME!!!")
    print("Encrypted quote:")
    print(' '.join(user_progress))
    print(' '.join(encrypted_quote))

    # Main game loop
    while True:
        print("\nOptions:")
        print("1. Guess the actor's name")
        print("2. Ask for a hint")
        print("3. Quit")
        user_option = input("Enter your option (1, 2, or 3): ").strip()

        if user_option == '1':
            user_guess = input("Enter the actor's name: ").strip()
            if len(user_guess) != len(quote):
                print("The length of your input does not match the length of the encrypted dialogue.")
            else:
                user_progress = update_progress(user_guess, user_progress, quote)
                if user_progress.lower() == quote.lower():
                    print("Congratulations! You've successfully decrypted the name of the actor.")
                    display_result(user_progress, quote, encrypted_quote)
                    break
                else:
                    display_result(user_progress, quote, encrypted_quote)
                    print("Incorrect. Try again or choose another option.")
        elif user_option == '2':
            hint = provide_hint(user_progress, quote, quote, actors_movies[quote])
            print(hint)
        elif user_option == '3':
            print("You've decided to quit the game. See you next time!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

# Call the main function to start the game
if __name__ == "__main__":
    main()
