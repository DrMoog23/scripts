import psutil
import argparse

def smartKill(name):
	pids = psutil.pids()

	for p in pids:
		process = psutil.Process(p)
		if (name in process.name()):
			process.terminate()
			print(process.name())
			print(p)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("name", type=str, help="Name of the processes to kill")
	args = parser.parse_args()

	smartKill(args.name)
