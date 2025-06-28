from googleapiclient.discovery import build
from src.auth import get_credentials
import sys
def get_all_subscriptions(youtube):

    all_subscriptions=[]
    next_page_token = None

    while True:
        request = youtube.subscriptions().list(
            part="snippet",
            mine=True,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        all_subscriptions.extend(response.get("items", []))
        
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return all_subscriptions
def saving_subscriptions(subscriptions, filename="subscriptions.txt"):
    
    print(f"\nTotal subscriptions are: {len(subscriptions)} . Saving to {filename} \n Loading...")
    with open(filename,"w", encoding="utf-8") as f:
        for i, item in enumerate(subscriptions):
            title = item["snippet"]["title"]
            channel_id = item["snippet"]["resourceId"]["channelId"]
            channel_url = f"https://www.youtube.com/channel/{channel_id}"
            f.write(f"{i+1}. {title} - {channel_url}\n")
    print(f"Subscriptions saved to {filename} successfully!")

def main():
    print("attempt to authenticate is done here")
    try:
        credentials = get_credentials()
        youtube = build("youtube", "v3", credentials=credentials)
        print("Authentication successful!")
        print("Getting subscriptions. Loading...")
        subscriptions = get_all_subscriptions(youtube)
        if subscriptions:
            saving_subscriptions(subscriptions)
        else:
            print("Errorrrrrrrr. No subs")
    except FileNotFoundError:
        print("no subs found. Do read README.md again.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
        
if __name__ == "__main__":
    main()
