import sys
from hashtag import newDP as DP

def word_reader(handle):
  while 1:
    line = sys.stdin.readline()
    if line.strip():
		yield line
		line = ""
    else: 
		return
	

def main():
  for word in word_reader(sys.stdin):
	for result in DP.result(word):
		print result[0], "\t", result[1]
  
  print
  sys.stdout.flush()
  

if __name__ == "__main__": 
  main()
