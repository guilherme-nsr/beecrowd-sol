import math

def main():
	voltas, placas = map(int, input().split())

	total_placas = placas*voltas

	placas_contadas = [math.ceil(total_placas * (i/10)) for i in range(1, 10)]

	print(' '.join(map(str, placas_contadas)))


if __name__ == "__main__":
	main()