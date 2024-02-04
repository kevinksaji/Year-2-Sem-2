#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>
#include <sys/wait.h>

int main(void) {
	const char * const secs[] = {"3", "1", "2"};
	const int count = sizeof(secs) / sizeof(*secs);
	pid_t pids[count];
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
		pids[i] = pid;
	}

	bool repeat;
	do {
		repeat = false;
		for (int i = 0; i < count; ++i) {
			const pid_t pid = pids[i];
			if (pid > 0) {
				int status;
				if (waitpid(pid, &status, WNOHANG) == pid) {
					printf("parent> child %d exited with code %d\n", pid, status);
					pids[i] = 0;
				} else {
					repeat = true;
				}
			}
		}
	} while (repeat);
	printf("parent> exiting\n");
	return EXIT_SUCCESS;
}
