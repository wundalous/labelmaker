# labelmaker
This repository contains code for generating herbarium voucher specimen labels from a specially-formatted CSV file. Especially useful if you need to write a bunch of labels for your plant collections, but don't have access to an existing herbarium database, or to the tools your local herbarium uses to generate labels. This solution is simple and easy to use, but is a work in progress, so bug reports are appreciated. 

## TO USE:
1. Download the whole repository, ensuring you save all of its contents into one folder.
2. Create a CSV (comma-separated value) file (use any spreadsheet software, such as MS Excel or Google Sheets to do this) containing your label data. *Ensure that all field names (column headings) are the same as in the sample CSV file provided.* 
3. Save this CSV file in the same folder as the repository files. (Let's say you name it 'MyLabels.csv'.)
4. Once you've written the content of your labels, run the program by opening a terminal window, navigating to the folder in which you've saved the repository files and your CSV file, and typing the following: 
//python v3labelmaker.py -i MyLabels
*Make sure to type in just the name of the CSV file, without the '.csv' file extension.* (Otherwise the program will look for a file called 'MyLabels.csv.csv'.) Hit 'Enter' to run the program. 
5. The program, if run successfully, will give you no feedback. To verify that the program worked, check the contents of the folder you've been working in. There should now be a MyLabels.json and a MyLabels.html. 
6. Open MyLabels.html in a browser. Each label will appear to be the whole width of the page on your screen. When you try to print the page, however, the labels will be resized so that six of them will fit on one page. 
7. Print the page. 
