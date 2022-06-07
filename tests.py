import os
import sys

def test_all():
    tests=['1','2','3','4','5','6','7','8a','8b','9a','9b','10a','10b']
    for t in tests:
        stream = os.popen('python slonie.py < test_files\\slo'+t+'.in')
        f = open("test_files\\slo"+t+".out", "r")
        n = int(f.readline())
        output=int(stream.read())
        assert output == n, "Test "+t+" not passed"
        print("Test "+t+" passed")

if __name__ == "__main__":
    test_all()
    print("Everything passed")