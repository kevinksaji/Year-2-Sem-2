#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

enum {
	SECONDS = 1
};

void run_parent(int writing_pipe) {
	char buffer[100];
	while (1) {
		printf("parent> ");
		// In a terminal issue CTRL+D to interrupt.
		if (scanf("%99s", buffer) != 1) {
			fprintf(stderr, "no input captured\n");
			break;
		}
		buffer[99] = '\0';
		if (write(writing_pipe, buffer, 100) <= 0) {
			fprintf(stderr, "unable to write\n");
			break;
		}
		sleep(1 * SECONDS);
	}
}

void run_child(int reading_pipe) {
	char buffer[100];
	while (read(reading_pipe, buffer, 100) > 0) {
		buffer[99] = '\0';
		printf("child > %s command received\n", buffer);
	}
	fprintf(stderr, "child > unable to read\n");
}

int main(void) {
	int p[2];
	if (pipe(p)){
		return EXIT_FAILURE;
	}
	const pid_t pid = fork();
	if (pid < 0) {
		fprintf(stderr, "fork failed\n");
		return EXIT_FAILURE;
	}
	if (pid == 0) {
		// child
		close(p[1]);
		run_child(p[0]);
		close(p[0]);
		return EXIT_SUCCESS;
	} else {
		// parent
		close(p[0]);
		run_parent(p[1]);
		close(p[1]);
		return EXIT_SUCCESS;
	}
}
