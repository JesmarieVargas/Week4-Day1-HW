def mood_response(mood):
    mood = mood.lower()
    if mood == 'happy':
        return "That's great to hear!"
    elif mood == 'sad':
        return "I'm sorry to hear that. I hope your day gets better!"
    elif mood == "excited":
        return "I'm excited for you."
    else:
        return "I hope you have a great rest of your day!"
    

