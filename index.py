page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href= "http://udacity.com">')
anchor_string = '<a'
href_String = 'href='
start_link_quote = page.find('"', page.find(href_String, page.find(anchor_string)))
end_link_quote = page.find('"', start_link_quote + 1)
print (page[start_link_quote + 1 : end_link_quote])  