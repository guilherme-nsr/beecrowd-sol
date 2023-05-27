# Python 3.4.3

def main():
  f1, f2 = map(float, input().split())

  t1 = 100 + f1
  t2 = t1 + ((f2/100)*t1)
  
  print("%.6f" %(t2-100))

if __name__ == '__main__':
	main()