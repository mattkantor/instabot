
from instalooter.looters import HashtagLooter

def links(media, looter):
    if media.get('__typename') == "GraphSidecar":
        media = looter.get_post_info(media['shortcode'])
        nodes = [e['node'] for e in media['edge_sidecar_to_children']['edges']]
        return [n.get('video_url') or n.get('display_url') for n in nodes]
    elif media['is_video']:
        media = looter.get_post_info(media['shortcode'])
        return [media['video_url']]
    else:
        return [media['display_url']]

def scrape(hashtag):

    looter = HashtagLooter(hashtag)
    with open("output/output.txt", "w") as f:
        for pages in looter.pages():
            for p in pages:
                print(pages)
                
                # for media in p.medias():
                #     for link in links(media, looter):
                #         f.write("{},{},{}\n".format(link))

def start():
    try:
        print("starting...")
        with open("hashtags.txt", "r") as f:
            content = f.readlines()
            content = [x.strip() for x in content]  
            for line in content:
                print("scraping {}".format(line))
                scrape(line)
    except Exception as e:
        print(e)
        pass




if __name__ == '__main__':
   start()
