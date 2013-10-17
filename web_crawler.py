#takes a url and outputs the webpage's content as a string
import urllib2
def get_page(url):
    try:
        f = urllib2.urlopen(url)
        response = f.read()
        response = str(response) #converts the output to a string, it was not working without this line
        f.close()
        return response
    except:
        return ""
    return ""

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

#isolates all the links on the page and inserts it into an array
def get_all_links(page):   
    links = [] 
    while True:
        url, last_quote = get_next_target(page)
        if url:
            links.append(url)
            page = page[last_quote:]
        else:
            break
    return links

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)
            
def crawl_web (seed_page, max_pages):
    tocrawl = get_all_links(get_page(seed_page)) 
    crawled = []
    
    while tocrawl:
        page_url = tocrawl.pop()
        if page_url not in crawled:
            union(tocrawl, get_all_links(get_page(page_url)))
            crawled.append(page_url)
        if len(crawled) >= max_pages:
            break
    return crawled    
     
        
seed_page = 'http://www.udacity.com/cs101x/index.html'        
print crawl_web(seed_page, 3)       
        
        
        
        
        
        