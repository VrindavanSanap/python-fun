def html_tag(tag):
    def wrap(text):
        return f'<{tag}> {text} </{tag}>'
    return wrap


h1_tag = html_tag('h1')
p_tag = html_tag('p')
b_tag = html_tag('b')


print(h1_tag('Local Man Proclaims His Love for Broccoli; Swears Off Bacon Forever'))
print(p_tag(f'In a shocking twist of dietary fate, local man {b_tag("John Smith")} has announced that he will no longer be consuming {b_tag("bacon")}, his once beloved breakfast food, and instead will be dedicating his taste buds to the humble green vegetable {b_tag("brocoli")}.'))