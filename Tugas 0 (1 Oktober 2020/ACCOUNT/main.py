FROM ACCOUNT IMPORT ACCOUNT


def main():
	humans = [Account(20000), Account(100000)]
	print(humans[0].initial_balance)


if __name__ == "__main__":
	main()