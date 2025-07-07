import google.generativeai as genai

# Replace with your actual Gemini API key
genai.configure(api_key="AIzaSyDcc1s1OF-U7Dr6n4s5MVzHJbzyzfZxVrY")

# Select model (latest available that supports content generation)
model = genai.GenerativeModel('models/gemini-1.5-flash')

# Prompt user for script type
print("Select script type:")
print("1. YouTube Video (up to 10 mins)")
print("2. Shorts/Reels (under 60 seconds)")
choice = input("Enter 1 or 2: ")

# Ask for topic and tone/style
topic = input("Enter the topic: ")
style = input("Enter the tone or style (e.g., friendly, funny, informative): ")

if choice == '1':
    audience = input("Enter your target audience (e.g., common audience, professionals): ")
    prompt = f"""
    You are a professional content writer for YouTube creators. Write a detailed, original script for a YouTube video 
    that is up to 10 minutes long. Include an attention-grabbing hook, valuable information, and a natural ending. 
    Keep the script engaging and narration-friendly.

    Topic: {topic}
    Audience: {audience}
    Style: {style}
    """
elif choice == '2':
    prompt = f"""
    Create a short, punchy script suitable for Instagram Reels or YouTube Shorts. Keep it under 60 seconds of spoken content.
    Start with a hook, deliver one strong message or tip, and end with a call-to-action or punchline.

    Topic: {topic}
    Tone: {style}
    """
else:
    print("Invalid selection. Please choose 1 or 2.")
    exit()

# Generate content
response = model.generate_content(prompt)

# Output result
print("\nGenerated Script:\n")
print(response.text)
