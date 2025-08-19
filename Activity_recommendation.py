def get_activity_suggestion():
    mood = input("How are you feeling today (energetic, relaxed, or adventurous)? ").lower()
    preference = input("Do you prefer indoor or outdoor activities? ").lower()

    if mood == "energetic":
        if preference == "outdoor":
            print("Go for a hike or a bike ride!")
        else:
            print("Try a music class or hit the gym!")
    elif mood == "relaxed":
        if preference == "outdoor":
            print("Consider a leisurely walk in the park or fishing.")
        else:
            print("How about reading a book or practicing meditation?")
    elif mood == "adventurous":
        if preference == "outdoor":
            print("Go rock climbing or try surfing!")
        else:
            print("Escape rooms or indoor skydiving might be fun!")
    else:
        print("Invalid mood or preference.")

if __name__ == "__main__":
    get_activity_suggestion()

