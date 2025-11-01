# FJOX.WIN
# Simple Python bot to repost a rss feed to mastodon compatible software
# code for git.fjox.win/fjox/rss-to-mastodon / fjox/rss-to-mastodon

import feedparser
import json
import hashlib
import os
import requests
import time

def build_toot(entry):
    ''' Take the entry dict and build a toot
    '''
    # Initialise
    skip_tags = SKIP_TAGS + ["blog", "documentation", CW_TAG]   
    toot_str = ''

    if "blog" in entry['tags']:
        toot_str += "New #Blog: "
    elif "documentation" in entry['tags']:
        toot_str += "New #Documentation: "

    toot_str += f"{entry['title']}\n"

    if entry['author']:
        toot_str += f"Author: {entry['author']}\n"

    toot_str += f"\n\n{entry['link']}\n\n"

    # Tags to hashtags
    if len(entry['tags']) > 0:
        for tag in entry['tags']:
            if tag in skip_tags:
                # Skip the tag
                continue
            toot_str += f'#{tag.replace(" ", "")} '

    return toot_str


def send_toot(en):
    ''' Turn the dict into toot text

    and send the toot
    '''
    toot_txt = build_toot(en)

    headers = {
        "Authorization" : f"Bearer {MASTODON_TOKEN}"
        }

    data = {
        'status': toot_txt,
        'visibility': MASTODON_VISIBILITY
        }

    if en['cw']:
        data['spoiler_text'] = en['title']

    if DRY_RUN == "Y":
        print("------")
        print(data['status'])
        print(data)
        print("------")
        return True

    try:
        resp = SESSION.post(
            f"{MASTODON_URL.strip('/')}/api/v1/statuses",
            data=data,
            headers=headers
        )

        if resp.status_code == 200:
            return True
        else:
            print(f"Failed to post {en['link']}")
            print(resp.status_code)
            return False
    except:
        print(f"Urg, exception {en['link']}")
        return False


def process_feed(feed):
    ''' Process the RSS feed and generate a toot for any entry we haven't yet seen
    '''
    if os.path.exists(feed['HASH_FILE']):
        hashtracker = open(feed['HASH_FILE'],'r+')
        storedhash = hashtracker.read()
    else:
        hashtracker = open(feed['HASH_FILE'],'w')
        storedhash = ''

    # This will be overridden as we iterate through
    firsthash = False

    # Load the feed
    d = feedparser.parse(feed['FEED_URL'])

    # Iterate over entries
    for entry in d.entries:

        # compare a checksum of the URL to the stored one
        # this is used to prevent us re-sending old items
        linkhash = hashlib.sha1(entry.link.encode('utf-8')).hexdigest()

        if storedhash == linkhash:
            print("Reached last seen entry")
            break

        en = {}
        en['title'] = entry.title
        en['link'] = entry.link
        en['author'] = False       
        en['tags'] = []

        if hasattr(entry, "tags"):
            # Iterate over tags and add them
            [en['tags'].append(x['term']) for x in entry.tags]

        en['cw'] = CW_TAG in en['tags']

        if INCLUDE_AUTHOR == "True" and hasattr(entry, "author"):
            en['author'] = entry.author

        # Keep a record of the hash for the first item in the feed
        if not firsthash:
            firsthash = linkhash

        # Send the toot
        if send_toot(en):
            # If that worked, write hash to disk to prevent re-sending
            hashtracker.seek(0)
            hashtracker.truncate()
            hashtracker.write(firsthash)

        time.sleep(1)
    hashtracker.close()

fh = open("feeds.json", "r")
FEEDS = json.load(fh)
fh.close()

HASH_DIR = os.getenv('HASH_DIR', '')
INCLUDE_AUTHOR = os.getenv('INCLUDE_AUTHOR', "True")

# Posts with this tag will toot with a content warning
CW_TAG = os.getenv('CW_TAG', "content-warning")

MASTODON_URL = os.getenv('MASTODON_URL', "https://mastodon.social")
MASTODON_TOKEN = os.getenv('MASTODON_TOKEN', "")
MASTODON_VISIBILITY = os.getenv('MASTODON_VISIBILITY', 'public')
DRY_RUN = os.getenv('DRY_RUN', "N").upper()
SKIP_TAGS = os.getenv('SKIP_TAGS', "").lower().split(',')

# We want to be able to use keep-alive if we're posting multiple things
SESSION = requests.session()

for feed in FEEDS:
    feed['HASH_FILE'] = HASH_DIR + hashlib.sha1(feed['FEED_URL'].encode('utf-8')).hexdigest()
    process_feed(feed)