# [Basic Time stamp ordering protocol](https://github.com/abhijeet2096/Assignments/tree/master/CS309/assignment4)
In this assignment we have tried to simulate basic time stamp ordering.

# Requirements
1. Python

# Instruction to Simulate

1. Open the source file into your favorite editor.
2. Move to Main Section and initialize the number of transaction needed to Simulate like this.

```
T_1 = Transaction(1)
T_2 = Transaction(2)
T_3 = Transaction(3)
```

3. write the transaction order you need to Simulate

```
T_1.read(X_1)
T_2.write(X_1)
T_1.read(X_1)
T_2.read(X_1)
T_3.write(X_1)
```
4. Spawn the terminal and execute the script like

```
$python /path/to/protocol.py
```

5. Sample Output

```
Reading Transaction with ts 1...
Writing Transaction with ts 2...
Transaction with timestamp 1 aborts.
Performing rollback...
Reading Transaction with ts 2...
Writing Transaction with ts 3...
2 3
```
# Approach
We have made Two classes

**class Transaction(object):** :- This class is used to simulate transaction with following functions:

1. read : To simulate Read operation of a transaction.

  *Input* Object X , where X is a simulated database object.

  *Output* True if successful otherwise vice versa.
2. write : To simulate Write operation of a transaction.

  *Input* Object X , where X is a simulated database object.

  *Output* True if successful otherwise vice versa.

**class X(object)** :- This class is used to simulate Database Object with following function:

1. read_ts :  Returns the value of last read timestamp.
2. write_ts : Returns the values of last write timestamp.
3. set_read_ts : Sets the value of read timestamp.
4. set_write_ts : Sets the values of write timestamp.

We have used try exception method in python to simulate rollback!

# About
This assignment is for course CS309 under Prof [Sriram Kailasam.](http://faculty.iitmandi.ac.in/~sriramk/)
