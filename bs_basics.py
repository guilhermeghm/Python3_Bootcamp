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
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
d = soup.select("[data-example]")
#d = soup.find_all(class_="special")
#d = soup.find_all(attrs={"data-example": "yes"})
print(d)
#print(soup.body.div)
#print(soup.find("div"))
#print(soup.find_all("div"))

#For CSS
#d = soup.select("#first")
#d = soup.select("#first")[0]
#print(d)


##Find an element with an id of foo
#soup.find(id="foo")
#soup.select("#foo")[0]

##Find all elements with a class of bar
## Careful! "class" is a reserved word in Python
#soup.find_all(class_="bar")
#soup.select(".bar")

##Find all elements with a data
##Attribute of "baz"
##Using the general attrs kwarg
#soup.find_all(attrs={"data-baz": True})
#soup.select("[data-baz]")
