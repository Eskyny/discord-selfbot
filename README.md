# discord-selfbot
A simple Python code to connect a real Discord account.

## ⚠️ Warning
Using selfbots is against Discord's Terms of Service. Your account may be permanently banned if detected. Use at your own risk.

## Features
- Connects to Discord using a user token
- Automatically sets status to "Do Not Disturb" (DND)
- Minimal and lightweight

## Requirements
- Python 3.9 or higher
- discord.py-self library

## Installation

### Windows
```bash
git clone https://github.com/Eskyny/discord-selfbot.git
cd discord-selfbot
pip install discord.py-self
```

### Linux (Debian/Ubuntu)
```bash
git clone https://github.com/Eskyny/discord-selfbot.git
cd discord-selfbot
python3 -m venv venv
source venv/bin/activate
pip install discord.py-self
```

## Configuration
1. Open `selfbot.py`
2. Replace `'TOKEN_HERE'` with your Discord user token

### How to get your Discord token

1. Open Discord in your web browser (discord.com/app)
2. Press F12 to open Developer Tools
3. Go to the "Application" tab (Chrome) or "Storage" tab (Firefox)
4. On the left sidebar, expand "Local Storage"
5. Click on "https://discord.com"
6. In the search box, type "tokens"
7. Copy the value (remove the quotes around it)

## Usage

### Run normally
```bash
python selfbot.py
```

**Important Notes:**
- Never share your token with anyone
- If your token is compromised, change your Discord password immediately to invalidate it

## Disclaimer
This project is for educational purposes only. The author is not responsible for any misuse or consequences of using this code. Discord selfbots violate Discord's Terms of Service and may result in account termination.

## License
MIT License
