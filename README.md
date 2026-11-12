# REST API Public Fetch — Reflection

This assignment helped me understand how an application can retrieve and process information from an external API instead of relying on data stored locally. I used Python's urllib library to request vehicle information from the NHTSA API, while asyncio allowed the request to run in a separate thread without blocking the application's event loop.

One unexpected challenge was Windows Security apparently blocking the installation of aiohttp. Instead of spending time troubleshooting the installation, I modified the code to use Python's built-in libraries. That showed me there can be multiple ways to accomplish the same task.

After retrieving the JSON response, I filtered the results using the GroupName field to display only records categorized as "Active Safety System." The program successfully returned 11 matching records, including ABS, traction control, and electronic stability control.

I now better understand asynchronous execution, JSON filtering, and how third-party APIs support interoperability. I'd like to explore how these results could be displayed in a graphical interface instead of the terminal.