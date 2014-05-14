"""
Import.io Scaffold

This is a barebones setup that can be used to start a project that utilizes 
the import.io web scraping API. You will need to create a file called importio_login.py
and create the variables GUID and API_key which, predictably, hold your official
import.io GUID and API key. I've kept mine out of this repository for obvious reasons.

"""

from importio_login import GUID, API_key
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

# Issue three queries to the same data source with different inputs
# You can modify the inputs and connectorGuids so as to query your own sources
# To find out more, visit the integrate page at http://import.io/data/integrate/#python
client.query({"input":{ "query": "server" },"connectorGuids": [ "39df3fe4-c716-478b-9b80-bdbee43bfbde" ]}, callback)
client.query({"input":{ "query": "ubuntu" },"connectorGuids": [ "39df3fe4-c716-478b-9b80-bdbee43bfbde" ]}, callback)
client.query({"input":{ "query": "clocks" },"connectorGuids": [ "39df3fe4-c716-478b-9b80-bdbee43bfbde" ]}, callback)

print "Queries dispatched, now waiting for results"

# Now we have issued all of the queries, we can "await" on the latch so that we know when it is all done
queryLatch.await()

print "Latch has completed, all results returned"

# It is best practice to disconnect when you are finished sending queries and getting data - it allows us to
# clean up resources on the client and the server
client.disconnect()

# Now we can print out the data we got
print "All data received:"
print json.dumps(dataRows, indent = 4)