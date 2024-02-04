#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

enum {
	ARG_DELAY = 1,
	ARGS_COUNT = ARG_DELAY + 1
};

enum {
	SECONDS = 1
};

int main(int argc, char *argv[]) {
	if (argc != ARGS_COUNT) {
		printf("The program must be run with one argument.\n");
		return EXIT_FAILURE;
	}
	const int delay = atoi(argv[ARG_DELAY]);
	if (delay <= 0) {
		printf("The argument must be a positive integer.\n");
		return EXIT_FAILURE;
	}
	int i = 0;
	const pid_t pid = getpid();
	while (1) {
		FILE *file = fopen("status.txt", "a");
		if (!file) {
			printf("Unable to open the file.\n");
			return EXIT_FAILURE;
		}
		fprintf(file, "%d running for %d seconds\n", pid, delay * i++);
		fclose(file);
		sleep(delay * SECONDS);
	}
	// No exit intended.
}
