# This_Week_In_Student_Life
**Why:**
Weekly the Dean of Students at Florida Tech writes an email including every event happening on campus that week. Some weeks this took 4 hours to write and most of the time I was the one writing it. So I made this program to do it for me.

## How It's Made
I tried multiple different ways to pull the information from the campus labs website (ical file, html parser, ...). In the end, I had to resort to an automated web browser. Yes, it is slow and there is probably a better option, but I didn't want to write another email and I found it to work.

**What it uses:**
- Selenium -interacts with webpage, scrapes data
- Tkinter -small UI to ease data input
- Python-docx -write all events, add hyperlinks

## Possible Features
- Option to save the password for quicker sign-in
- Window to choose what clubs to exclude
- Pull photos and choose some at random to add

## Demos
*Both demos are only were only given a minute for fairness.*

**Written by hand**

![by_hand_twisl](https://github.com/user-attachments/assets/a8afa891-3f94-4081-b44b-2b84a74b79be)

**Using the program**

![program_twisl](https://github.com/user-attachments/assets/bf4ed2d8-cb8e-4848-bad5-42b9d657253c)

**Example Email**

![twisl](https://github.com/user-attachments/assets/71bf1fb7-6bc3-4af9-996c-862cb5a20aaf)
