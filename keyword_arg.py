# keyword ini sama seprti argument_list, tp menggunakan 2 bintang
# artinya argumen keyword ini adalah optional, dan ketika keyword argument ini terisi oleh value
# hasil value ini akan di simpan kedalam dictionary

def create_html(tag, text, **atr):
    html = f"<{tag}"
    print(atr)
# hasil object dictionary ini dijadikan tupple
    for key , val in atr.items(): 

        html = html + f" {key}='{val}'"
        
    html = html + f">{text}</{tag}>"

    return html

html = create_html("p", "gellow lu")
print(html)

html = create_html("a", "kuro lo", href="google.com", style="color:red")
print(html)