class ConflictError(Exception):
    pass

class Transaction(object):
    """docstring for Transaction."""

    def __init__(self, ts):
        self.ts = ts
        flag = False
    def time(self):
        return self.ts
    def read(self, x):
        try:
            if self.time() < x.write_ts():
                raise ConflictError('Transaction with timestamp ' + str(self.time()) + ' aborts.')
                flag = True
            else:
                if x.read_ts() < self.time():
                    x.set_read_ts(self.time())
                print("Reading Transaction with ts " + str(self.ts) + "...")
                return True
        except ConflictError as e:
            print(str(e))
            print("Performing rollback...")

    def write(self, x):
        try:
            if self.time() < x.read_ts() or self.time() < x.write_ts():
                raise ConflictError('Transaction with timestamp ' + str(self.time()) + ' aborts.')
                flag = True
            else:
                x.set_write_ts(self.time())
                print("Writing Transaction with ts " + str(self.ts) + "...")
                return True
        except ConflictError as e:
            print(str(e))
            print("Performing rollback...")

class X(object):
    """docstring for X."""
    def __init__(self, ts=0):
        self.ts_read = ts
        self.ts_write = ts
        # self.dictionary{0:(ts, ts)}

    def read_ts(self):
        return self.ts_read

    def write_ts(self):
        return self.ts_write

    def set_read_ts(self, ts):
        self.ts_read = ts

    def set_write_ts(self, ts):
        self.ts_write = ts


if __name__ == '__main__':
    T_1 = Transaction(1)
    T_2 = Transaction(2)
    T_3 = Transaction(3)
    # T_4 = Transaction(4)
    X_1 = X()


    T_1.read(X_1)
    T_2.write(X_1)
    T_1.read(X_1)
    T_2.read(X_1)
    T_3.write(X_1)
    print(X_1.read_ts(), X_1.write_ts())
