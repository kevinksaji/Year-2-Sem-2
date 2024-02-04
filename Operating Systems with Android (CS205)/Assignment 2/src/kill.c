#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>

enum {
	SECONDS = 1
};

int main(void) {
	const char * const secs[] = {"1", "2"};
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
	sleep(3 * SECONDS);
	
	const pid_t kill_pid = pids[0];
	if (kill_pid > 0) {
		kill(kill_pid, SIGTERM);
		printf("parent> child %d killed\n", kill_pid);
	}
	
	const pid_t resume_pid = pids[1];
	if (resume_pid > 0) {
		kill(resume_pid, SIGSTOP);
		printf("parent> child %d stopped\n", resume_pid);
		printf("parent> wait for 2s\n");
		sleep(2 * SECONDS);
		printf("parent> resuming child %d\n", resume_pid);
		kill(resume_pid, SIGCONT);
	}
	printf("parent> exiting\n");
	return EXIT_SUCCESS;
}
