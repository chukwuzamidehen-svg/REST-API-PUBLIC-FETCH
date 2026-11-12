# REST API Public Fetch — Reflection

This assignment helped me better understand how REST APIs can communicate with each other rather than just exchanging information with a user interface. I created a Flask application that retrieves vehicle information from the NHTSA public API, filters the JSON response, and makes the results available through a local REST endpoint.

Originally, my application displayed the filtered results directly in the terminal. After reviewing the reference document, I modified it to return JSON through Flask instead. That helped me understand the difference between retrieving data for a script and building an API that other applications can consume.

One unexpected challenge was Windows Security apparently blocking an additional Python package installation. I worked around this by using Python's built-in libraries and reusing an existing Flask environment.

The application successfully returned 11 records categorized as "Active Safety System." Seeing the HTTP 200 response in my terminal helped connect the concepts of GET requests, JSON filtering, and API responses.

I'd like to explore how a JavaScript frontend could asynchronously retrieve and display these results.
