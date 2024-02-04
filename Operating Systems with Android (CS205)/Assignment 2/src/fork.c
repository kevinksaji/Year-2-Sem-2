#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void) {
	const pid_t pid = fork();
	if (pid < 0) {
		fprintf(stderr, "fork failed\n");
		return EXIT_FAILURE;
	}
	int n = 0;
	if (pid == 0) {
		pid_t mypid = getpid();
		n = 1;
		printf("child> My PID is %d\n", mypid);
		printf("child> n = %d\n", n);
		return EXIT_SUCCESS;
	}
	n = 100;
	printf("parent> I just created child %d\n", pid);
	printf("parent> n = %d\n", n);
	return EXIT_SUCCESS;
}
