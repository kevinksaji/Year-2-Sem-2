#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

enum {
	ARG_COUNT = 1,
	ARGS_COUNT = ARG_COUNT + 1
};

int main(int argc, char *argv[]) {
	if (argc != ARGS_COUNT) {
		printf("The program must be run with one argument.\n");
		return EXIT_FAILURE;
	}
	const int count = atoi(argv[ARG_COUNT]);
	if (count <= 0) {
		printf("The argument must be a positive integer.\n");
		return EXIT_FAILURE;
	}
	
	for (int i = 0; i < count; ++i) {
		const pid_t pid = fork();
		if (pid < 0) {
			fprintf(stderr, "fork failed\n");
			return EXIT_FAILURE;
		}
		if (pid == 0) {
			const pid_t mypid = getpid();
			printf("child> My PID is %d. I am child num %d\n", mypid, i);
			return EXIT_SUCCESS;
		}
		printf("parent> I just created child %d\n", pid);
	}
	return EXIT_SUCCESS;
}
