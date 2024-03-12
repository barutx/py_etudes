import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    s.strip() 
    if match := re.search(r'^<iframe.+src="https?://(?:www\.)?youtube.com/embed/(.+?)".+</iframe>$', s):
       url = match.group(1)
       return f'https://youtu.be/{url}'
if __name__ == '__main__':
    main()