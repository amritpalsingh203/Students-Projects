
Project Title: Real Time Threat Detection for Deaf and Blind
----
2025 Batch - CSE
* Alok Kumar Verma - 21103010
* Tanish Sharma - 21103151

gitHub repo : - https://github.com/alokkv2502/Threat-detection-backend

---
REAL-TIME THREAT DETECTION SYSTEM USER GUIDE

What is this system?
This is a system that listens to conversations and alerts you when it detects threatening words. It works by converting speech to text and checking for dangerous words in real-time.

What do you need to use it?
- A computer with Python 3.8 or newer
- A web browser that can use your microphone
- Internet connection
- A working microphone

How to set up the system:

1. Setting up your computer:
   - Open your terminal/command prompt
   - Create a new environment by typing: python -m venv venv
   - Start the environment:
     * On Mac/Linux: source venv/bin/activate
     * On Windows: venv\Scripts\activate
   - Install the required programs: pip install -r requirements.txt
   - Set up the database: python manage.py migrate

2. Starting the system:
   - Type: python manage.py runserver
   - Open your web browser and go to: http://localhost:8000

How to use the system:

1. Opening the system:
   - Open your web browser
   - Go to the website address
   - You'll see three main parts:
     * A button to start/stop listening
     * A box showing what is being said
     * A section showing if any threats are found

2. Starting to listen:
   - Click the "Start Listening" button
   - When your browser asks, allow it to use your microphone
   - A red dot will appear when the system is listening

3. How it works:
   - The system will show what it hears in the text box
   - If it hears dangerous words, it will show a warning
   - It will tell you which dangerous words it found

4. Stopping the system:
   - Click the "Stop Listening" button
   - The system will stop listening
   - The text and warnings will be cleared

What words does it look for?
The system checks for these words:
- bomb
- attack
- shoot
- kill
- threat
- danger
- terrorist
- Tanish

Technical information:
- The system checks audio every second
- It uses a special program to understand speech
- It works on your computer without sending data elsewhere
- It uses a small, fast program to understand speech

If something goes wrong:

1. If the microphone doesn't work:
   - Make sure your browser can use the microphone
   - Check if your microphone is working
   - Try refreshing the page

2. If you can't hear anything:
   - Check if your microphone is plugged in
   - Make sure your volume is on
   - Check if the system has permission to use the microphone

3. If the system is slow:
   - Close other programs
   - Check if your computer is working hard
   - Make sure your internet is working

Getting help:
- Look at the realtimesst.log file for errors
- Contact the person who set up the system
- Tell them about any problems you find

Important things to know:
- The system works on your computer only
- It doesn't save what it hears
- It's safe to use
- Keep the system updated

Tips for using the system:
1. Test it regularly to make sure it works
2. Keep it updated
3. Use it in appropriate places
4. Follow privacy rules

Updates:
- The system will be updated regularly
- Check for new versions
- Follow update instructions
- Save your settings before updating

Need more help?
Contact the person who set up the system or check the technical guide. 