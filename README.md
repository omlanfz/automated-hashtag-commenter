# automated-hashtag-commenter
Description:
------------
This Python project automatically posts movement-related hashtags on Facebook posts to support the Quota Movement in Bangladesh, helping raise international awareness.

Features:
---------
- Locates and clicks the comment button on Facebook posts.
- Posts predefined comments with hashtags.
- Adds emojis for enhanced visibility.
- Continuously scrolls and comments until manually stopped.

Prerequisites:
--------------
- Python 3.x
- Required packages: OpenCV (cv2), NumPy, PyAutoGUI, Pyperclip, Keyboard

Installation:
-------------
1. Clone the repository:
   git clone https://github.com/yourusername/automated-hashtag-commenter.git
   cd automated-hashtag-commenter

2. Install the required packages:
   pip install -r requirements.txt

3. Ensure you have a screenshot of the comment button saved as 'comment_button.png' in the project directory.

Usage:
------
1. Run the script:
   python commenter.py

2. To stop the script, press the 'r' key.
