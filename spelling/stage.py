import re
a = "fa;sdlkjf ajdslkfj ajsdlkfj fjasd sdf34asdf"
c = re.sub(r'[^a-zA-Z\' ]+', '', a)
print(c)