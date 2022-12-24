
## The project flow, blockers, results, basically the course of project thoughts.



The project was not one of the regular web scraping tasks. The given website "https://v-tylu.work/uk/?transaction_type=offering-with-online-payment" has its JavaScript DOM active, that is why it is not straightforward to fetch data from there. As needed when I inspected the website elements and tried to scrape some tags as well as classes they returned no value to me.

The reason for that was this DOM object. 

To give an overall understanding for the topic, the underlying code does not hold all the classes and tags and respective data for them. There is a JavaScript file/code/event regardless of the reference, it does some stuff on the browser and only after that fetches the correct data. 

So, I found a way which took my entire day to complete this task because it was the first time I was facing something like this and I literally needed to research and learn new topics.

Coming to implementation, I found XHR files of the website being "listings" and "categories" within its network field. There I sent a request for every page (load more listings. For the sake of representation, I took sample page numbers to be 10 given by total_pages variable in the code) and stored its response. Within those responses I used Regex to find the patterns like "/uk/listings/{id_numbers}" to find every specific listing's id numbers. 

Later, having stored and fetched those id numbers to a list (after storing them in a set because sets do not allow duplicate values which in our case obviously id numbers should not be duplicated), I sent a POST request to "https://listing-service.v-tylu.com/work/listings" endpoint which actually returns us the needed data for every listing. 

Having stored the responses of those requests to a pandas dataframe, I wrote the dataframe to both an Excel and a CSV file. CSV file in unreadable due to multiple characters not being either Unicode Decode or Encode compatible for readibility. However, Excel file is well structured and readable ready for further usage and analysis.

Thank you for reading through this README.md file to understand the project flow and project related specifics.