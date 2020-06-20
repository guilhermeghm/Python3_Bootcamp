from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special.</li>
    <li>This list item is not special.</li>
    <li class="special">This list item is also special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
#data = soup.find(class_="super-special").parent.parent
#data = soup.find(class_="super-special").find_next_sibling(class_="special")
#data = soup.find(id="first").find_next_sibling() #This skip the blank lines.
data = soup.find("h3").find_parent("html")

#data1 = soup.body.contents
#data2 = soup.body.contents[1]
#data3 = soup.body.contents[1].next_sibling
#print(data1)
#print(data2)
#print(data3)
#help(data)
print(data)
