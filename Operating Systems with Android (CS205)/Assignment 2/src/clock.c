#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

enum {
	ARG_DELAY = 1,
	ARGS_COUNT = ARG_DELAY + 1
};

enum {
	COUNT = 5,
	SECONDS = 1
};

int main(int argc, char *argv[]) {
	if (argc != ARGS_COUNT) {
		printf("The program must be run with one argument.\n");
		return EXIT_FAILURE;
	}
	const int delay = atoi(argv[ARG_DELAY]);
	if (delay <= 0) {
		printf("The first argument must be a positive integer.\n");
		return EXIT_FAILURE;
	}	
	int i = 0;
	const pid_t pid = getpid();
	while (i < COUNT) {
		printf("[%4d]\t%d/%d: sleep for %d seconds\n", pid, i++, COUNT, delay);
		sleep(delay * SECONDS);
	}
	printf("[%4d]\t%d/%d: done\n", pid, i, COUNT);
	return EXIT_SUCCESS;
}
