# YouTube Subscription Exporter

A Python tool to export your complete YouTube subscription list using the official YouTube Data API v3.

## Features
- It fetches all your subscriptions and save their url to text files.
- Handles pagination automatically.

### Using uv

```bash
# Clone the repository
git clone https://github.com/Anand-0037/yt-subscribed-channels-exporter.git
cd yt-subscribed-channels-exporter

uv init # to initialise the directory

uv venv # to create uv venv

source .venv/bin/activate # to activate venv

# Install dependencies using uv
uv sync

# or using uv plus pip
uv pip install -r requirements.txt
```

## Setup

### Google Cloud Console Setup

1. **Navigate to Google Cloud Console**
   - Go to [console.cloud.google.com](https://console.cloud.google.com/)
   - **Create a New Project** --> name it

2. **Enable YouTube Data API v3**
   - Search for "YouTube Data API v3" in the search bar
   - click "ENABLE"

3. **Create OAuth 2.0 Credentials**
   - Navigate to "APIs & Services" > "Credentials"
   - Click "+ CREATE CREDENTIALS" > "OAuth client ID"
   
   **If prompted to configure consent screen:**
   - Click "CONFIGURE CONSENT SCREEN"
   - Select "External" and click "CREATE"
   - Fill in the required fields:
     - App name: `YouTube Exporter`
     - User support email: (Your email-id)
     - Developer contact information: (Your email-id)
   - Click "SAVE AND CONTINUE"
   
   **Create OAuth Client ID:**
   - Go back to "Credentials" > "+ CREATE CREDENTIALS" > "OAuth client ID"
   - Application type: "Desktop app"
   - Name: `YouTube Exporter Desktop Client`
   - Click "CREATE"

4. **Download Credentials**
   - Click "DOWNLOAD JSON" from the popup
   - Rename the file to `user_secret.json`
   - Place it in the project root directory

### Step 2: Add Test Users (Important!)

Since your app is in testing mode, you must add your email as a test user:

1. Go to "APIs & Services" > "OAuth consent screen"
2. Find the "Test users" section
3. Click "+ ADD USERS"
4. Add your Google account email

## Project Structure

```
yt-subscribed-channels-exporter/
├── .gitignore               
├── README.md                
├── pyproject.toml            
├── requirements.txt         
├── uv.lock                  
├── user_secret.json         # you add this --> in root directory
├── token.json               # auto-generated
├── subscriptions.txt        # output file 
└── src/
    ├── auth.py              
    └── main.py              
```

## Usage

### Running the Application

```bash
# for running the repo --> please do setup before this
# caustion: src.main not src/main
uv run -m src.main

```

## Contributing

you can contribute to this repo,
We can do automate the process of subcribing using **Selenium** instead of doing manually.

**Built by [Anand-0037](https://github.com/Anand-0037)**
