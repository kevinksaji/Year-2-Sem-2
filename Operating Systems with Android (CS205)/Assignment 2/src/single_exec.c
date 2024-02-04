#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(void) {
	pid_t pid = fork();
	if (pid < 0) {
		fprintf(stderr, "fork failed\n");
		return EXIT_FAILURE;
	}
	if (pid == 0) {
		char * const exec = strdup("./clock");
		char * const arg1 = strdup("3");
		char * const arg_list[] = {exec, arg1, NULL};
		execvp(arg_list[0], arg_list);
		// Unreachable code unless execution failed.
		free(arg1);
		free(exec);
		return EXIT_FAILURE;
	}
	printf("parent> created a child %d\n", pid);
	return EXIT_SUCCESS;
}
