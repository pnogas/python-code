from ghost import Ghost
import re
g = Ghost(wait_timeout=20)

page, resources = g.open('http://www.indeed.ca/jobs?q=telecommunications&l=Toronto')
result, resources = g.evaluate("document.getElementsByClassName('company');")

print result
