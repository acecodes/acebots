from importio_login import GUID, API_key, Amaz_BestSeller_GUID, Amaz_BestSeller_URL
import logging, json, importio, latch


# You do not need to do this, but setting the logging level will reveal logs about
# what the import.io client is doing and will surface more information on errors
logging.basicConfig(level=logging.INFO)

# If you wish, you may configure HTTP proxies that Python can use to connect
# to import.io. If you need to do this, uncomment the following line and fill in the
# correct details to specify an HTTP proxy:

#proxies = { "http": "127.0.0.1:3128" }

client = importio.importio(user_id=GUID, api_key=API_key)
client.connect()

queryLatch = latch.latch(1)

dataRows = []

def callback(query, message):
    global dataRows
    
    # Disconnect messages happen if we disconnect the client library while a query is in progress
    if message["type"] == "DISCONNECT":
        print "Query in progress when library disconnected"
        print json.dumps(message["data"], indent = 4)

    # Check the message we receive actually has some data in it
    if message["type"] == "MESSAGE":
        if "errorType" in message["data"]:
            # In this case, we received a message, but it was an error from the external service
            print "Got an error!" 
            print json.dumps(message["data"], indent = 4)
        else:
            # We got a message and it was not an error, so we can process the data
            print "Got data!"
            print json.dumps(message["data"], indent = 4)
            # Save the data we got in our dataRows variable for later
            dataRows.extend(message["data"]["results"])
    
    # When the query is finished, countdown the latch so the program can continue when everything is done
    if query.finished(): queryLatch.countdown()

# Connect to Amazon NY Best Seller List API
client.query({
  "connectorGuids": [
    Amaz_BestSeller_GUID
  ],
  "input": {
    "webpage/url": Amaz_BestSeller_URL
  }
}, callback)


print "Queries dispatched, now waiting for results"

# Now we have issued all of the queries, we can "await" on the latch so that we know when it is all done
queryLatch.await()

print "Latch has completed, all results returned"

# It is best practice to disconnect when you are finished sending queries and getting data - it allows us to
# clean up resources on the client and the server
client.disconnect()

# Now we can print out the data we got
print "All data received:"

def author_dic():

    authors = {}

    for row in dataRows:
        if 'author/_text' in row:
            author_name = row['author/_text']

        if 'author' in row:
            author_link = row['author']

        authors[author_name] = author_link

    return authors

def book_dic():

    titles = {}

    for row in dataRows:
        if 'title/_text' in row:
            title_name = row['title/_text']

        if 'title' in row:
            title_link = row['title']

        titles[title_name] = title_link

    return titles

def covers_dic():

    covers = {}

    for row in dataRows:
        if 'title/_text' in row:
            title_name = row['title/_text']

        if 'cover' in row:
            cover_html = row['cover']

        covers[title_name] = cover_html

    return covers