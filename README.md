# THE2Tester
Tester for Take-Home Exam 2 (2018)

##### !!! THIS PROJECT IS COMPLETELY UNOFFICIAL !!!

## Usage:
### Testing with the Examples in the PDF
After you write your THE2, you will probably want to check it with the examples provided in PDF. test_examplesInPDF.py is exactly written for this task.
Put the script in **the same directory as the2.py file**. Then run:
```
python test_examplesInPDF.py 
```
Or you can make it executable and run it directly (for linux):
```
chmod +x test_examplesInPDF.py 
./test_examplesInPDF.py
```
### Using Generated Dest Data - tester.py
tester.py is a script which takes the file name of the test data (either as a command line argument or using direct input) and executes all test cases in dataset, reporting failures and statistics.

Currently approved dataset(s):
* testdata1 - Approved by 13 people. Contains 200000 test cases, which include:
  * Completely seperate blocks
  * Firmus situations
  * Addendum situations
* test_intersects - Approved by 5 people. Contains 100000 test cases which are mainly intersection situations such as:
  * Intersecting in the middle (like a plus sign or T)
  * Intersecting at the corners
  * One of the blocks is completely inside the other one
* test_epsilon - Approved by 4 people. Contains 150000 test cases which test your code's ability to handle epsilon comparison.
* sondata - Approved by 3 people. Contains 120000 test cases. Thanks to [sirkatee](https://github.com/sirkatee) for submitting.

Each dataset has one test case per line. Every test case contains 3 lists, seperated by ";" (seperator is defined as a global in tester.py which can be changed easily.). First two lists are parameters for is_firmus function and the last list is the expected output.

Use this command to test your code with testdata1: (again, **your the2.py file must be in the same directory**) 
```
python tester.py testdata1
```
or
```
./tester.py testdata1 #you first need to chmod +x tester.py 
```
If you tested a dataset and passed all the test cases, inform me and I will increase the number of people who approved that dataset.
Otherwise check your code and if there is a problem with the tester/testdata, open an issue or discuss at COW newsgroup/Whatsapp. 
