from urllib.request import urlopen

# with block manages resource returned by url, because under the hood,
# fetching a resource from the web requires operating system sockets and other resources.
# using a with statement with objects that use external resources is good practice to avoid resource leaks.
# with statement calls urlopen function and binds response to a variable named story.
# with statement is terminated by a colon, introducing a new block.
with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        # divide line into words based on whitespace boundaries
        # http request transfers raw bytes over the network.
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

print(story_words)
