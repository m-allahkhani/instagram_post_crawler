import instaloader
import json
import time
import os
def save_instagram_links_to_json(session_username, target_profile, output_file):
    try:
        # L = instaloader.Instaloader(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
        # L.load_session_from_file(session_username)
        # profile = instaloader.Profile.from_username(L.context, target_profile)
        L = instaloader.Instaloader()

        L.load_session("m.a.t.dreamer", {
            "csrftoken": "WHERFB0gmSUDGuAWUQ6QXf",
            "sessionid": "75146617751%3AODevA4xfsmqoMA%3A28%3AAYdNy2qMbQzWzGRu4w0ufY-hXr9MtruP1eQB6ev0qg",
            "ds_user_id": "75146617751",
            "mid": "aDmcqQALAAH4chndwfHvDyQ_ctBU",
            "ig_did": "A07A0F52-959B-4B8A-81A6-58062F2B162C"
        })

        profile = instaloader.Profile.from_username(L.context, "alahkhani")

        if os.path.exists(output_file):
            with open(output_file, 'r') as f:
                share_links = json.load(f)
        else:
            share_links = []

        seen_links = set(share_links)

        for post in profile.get_posts():
            share_link = f"https://www.instagram.com/p/{post.shortcode}/"
            if share_link not in seen_links:
                print(f"Saving: {share_link}")
                share_links.append(share_link)
                seen_links.add(share_link)
                # Save after every new link
                with open(output_file, 'w') as json_file:
                    json.dump(share_links, json_file, indent=4)

                time.sleep(10)  # To avoid rate limiting

    except instaloader.exceptions.ConnectionException as e:
        print("Instagram blocked the request temporarily.")
        print("Wait for 15-60 minutes and try again.")
        print("Error details:", e)
        
    #     share_links = []
    #     for post in profile.get_posts():
    #         print("*")
    #         share_link = f"https://www.instagram.com/p/{post.shortcode}/"
    #         share_links.append(share_link)
    #         time.sleep(10)  # Avoid rate limiting

    #     with open(output_file, 'w') as json_file:
    #         json.dump(share_links, json_file, indent=4)
        
    #     print(f"Share links saved to {output_file}")
    
    # except instaloader.exceptions.ConnectionException as e:
    #     print("Instagram blocked the request temporarily.")
    #     print("Wait for 15-60 minutes and try again.")
    #     print("Error details:", e)

# Run it
session_username = 'yourusername'
target_profile = 'yourTargetPofile'
output_file = 'E:/PROJECTS/crwaler/instagram_links.json'

save_instagram_links_to_json(session_username, target_profile, output_file)
############ instaloader --login=sessionusername run in cmd