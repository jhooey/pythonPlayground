page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href= "http://udacity.com">')

import urllib.request

def get_page(url):
    try:
        f = urllib.request.urlopen(url)
        response = f.read()
        f.close()
        return response
    except:
        return ""
    return ""

page = get_page('http://www.google.com')
print (page)

#finds the position of a " (left quote) after a 'href=' which needs to be after an '<a' tag
#then collect the text after the found quote until the closing quote
def get_next_target ( html_content ):
    anchor_string = '<a'
    href_String = 'href='
    
    start_link_quote = html_content.find('"', html_content.find(href_String, html_content.find(anchor_string))) 
    
    #Error catch if a link is not found
    if start_link_quote == -1:
        return None, 0
    
    end_link_quote = html_content.find('"', start_link_quote + 1)
    url = html_content[start_link_quote + 1 : end_link_quote]
    
    return url, end_link_quote


def get_all_links(page):   
    links = [] 
    while True:
        url, last_quote = get_next_target(page)
        if url:
            links.append(url)
            page = page[last_quote:]
        else:
            break      