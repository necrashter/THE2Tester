# THE2Tester
Tester for Take-Home Exam 2 (2018)

##### !!! THIS PROJECT IS COMPLETELY UNOFFICIAL !!!

## Usage:
### Testing with the Examples in the PDF
After you write your THE2, you will probably want to check it with the examples provided in PDF.
Put the script in **the same directory as the2.py file**. Then run:
```
python test_examplesInPDF.py 
```
Or you can make it executable and run it directly (for linux):
```
chmod +x test_examplesInPDF.py 
./test_examplesInPDF.py
```
### Unconfirmed Directory
Under "unconfirmed" directory, you will find two files:
1. tester.py - A script which takes the file name of the test data (either as a command line argument or using direct input)
2. testdata1 - Relatively large file (about 40 MB) containing 200000 test cases with my expected outputs (To those in Whatsapp group: This does NOT include the test cases shared there)

Since these files are not provided to us by CENG, they need testing. If your code has passed all the test cases in the first part, test your code with this: (again, **your the2.py file must be in the same directory**) 
```
python tester.py testdata1
```
or
```
./tester.py testdata1 #you first need to chmod +x tester.py 
```
If your code passed all the tests, inform me and I will keep track of how many people has approved this dataset.
Otherwise check your code and if there is a problem with the tester/testdata, open an issue or email me. 
