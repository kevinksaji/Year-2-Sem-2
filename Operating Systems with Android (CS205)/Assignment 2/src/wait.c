#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void) {
	const char * const secs[] = {"3", "1", "2"};
	const int count = sizeof(secs) / sizeof(*secs);
	for (int i = 0; i < count; ++i) {
		const pid_t pid = fork();
		if (pid < 0) {
			fprintf(stderr, "fork failed\n");
			continue;
		}
		if (pid == 0) {
			char * const exec = strdup("./clock");
			char * const arg1 = strdup(secs[i]);
			char * const arg_list[] = {exec, arg1, NULL};
			execvp(arg_list[0], arg_list);
			// Unreachable code unless execution failed.
			free(arg1);
			free(exec);
			return EXIT_FAILURE;
		}
		printf("parent> created a child %d\n", pid);
	}

	printf("parent> now waiting for the first child to return...\n");
	int status;
	const pid_t child_pid = wait(&status);
	printf("parent> child process %d exited with code %d\n", child_pid, status);
	printf("parent> exiting\n");
	return EXIT_SUCCESS;
}
