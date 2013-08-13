#finds the position of a " (left quote) after a 'href=' which needs to be after an '<a' tag
#then collect the text after the found quote until the closing quote
def get_next_target ( html_content ):
    anchor_string = '<a'
    href_String = 'href='
    
    start_link_quote = html_content.find('"', html_content.find(href_String, html_content.find(anchor_string))) 
    end_link_quote = html_content.find('"', start_link_quote + 1)
    url = html_content[start_link_quote + 1 : end_link_quote]
    
    return url, end_link_quote


page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href= "http://udacity.com"><a href= "http://jacob.com">')


url, last_quote = get_next_target(page)
page = page[last_quote:]

print (url)

url, last_quote = get_next_target(page)
page = page[last_quote:]

print (url)