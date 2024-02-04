#include <signal.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <sys/time.h> 
#include <limits.h>

typedef enum process_status {
    RUNNING = 0,
    READY = 1, // Add the READY state
    STOPPED = 2, // Add the STOPPED state
    TERMINATED = 3,
	UNUSED = 4 // Add the UNUSED state
} process_status;

typedef struct process_record {
    pid_t pid;
    process_status status;
    int total_runtime;     // Total expected runtime of the process
    int remaining_runtime; // Remaining runtime of the process
    struct timeval start_time; // Start time of the process
    struct timeval last_update_time; // Last time the runtime was updated
} process_record;

enum {
    MAX_PROCESSES = 64
};

process_record process_records[MAX_PROCESSES];

void update_process_times(void) {
    struct timeval current_time;
    gettimeofday(&current_time, NULL);

    for (int i = 0; i < MAX_PROCESSES; ++i) {
        process_record *p = &process_records[i];
        if (p->status == RUNNING || p->status == STOPPED) {
            long seconds = current_time.tv_sec - p->last_update_time.tv_sec;
            long useconds = current_time.tv_usec - p->last_update_time.tv_usec;
            long elapsed = seconds * 1000 + useconds / 1000; // Convert to milliseconds

            p->remaining_runtime -= elapsed; // Update remaining runtime
            p->last_update_time = current_time; // Update last update time

            // Check if process has completed its runtime
            if (p->remaining_runtime <= 0) {
                p->status = TERMINATED;
                printf("Process %d has completed and is now TERMINATED.\n", p->pid);
            }
        }
    }
}

void scheduler(void) {
    // Set any currently RUNNING process to READY
    for (int i = 0; i < MAX_PROCESSES; ++i) {
        if (process_records[i].status == RUNNING) {
            process_records[i].status = READY;
        }
    }

    int index_of_shortest_job = -1;
    int shortest_runtime = INT_MAX;

    // Find the READY process with the least remaining runtime
    for (int i = 0; i < MAX_PROCESSES; ++i) {
        if (process_records[i].status == READY && process_records[i].remaining_runtime < shortest_runtime) {
            shortest_runtime = process_records[i].remaining_runtime;
            index_of_shortest_job = i;
        }
    }

    // If a READY process is found, set its state to RUNNING
    if (index_of_shortest_job != -1) {
        process_records[index_of_shortest_job].status = RUNNING;
        gettimeofday(&process_records[index_of_shortest_job].last_update_time, NULL); // Update start time
    } else {
        printf("No READY processes available for scheduling.\n");
    }
}

void perform_stop(char *args[]) {
    pid_t pid = atoi(args[0]);
    if (pid <= 0) {
        printf("The process ID must be a positive integer.\n");
        return;
    }

    bool process_found = false;
    for (int i = 0; i < MAX_PROCESSES; ++i) {
        if (process_records[i].pid == pid) {
            if (process_records[i].status == RUNNING) {
                // Change the process status to STOPPED
                process_records[i].status = STOPPED;

                // Update the process's runtime before stopping
                struct timeval current_time;
                gettimeofday(&current_time, NULL);

                long seconds = current_time.tv_sec - process_records[i].last_update_time.tv_sec;
                long useconds = current_time.tv_usec - process_records[i].last_update_time.tv_usec;
                long elapsed = seconds * 1000 + useconds / 1000; // Convert to milliseconds

                process_records[i].remaining_runtime -= elapsed; // Update remaining runtime
                process_records[i].last_update_time = current_time; // Update last update time

                process_found = true;
                break;
            } else {
                printf("Process %d is not RUNNING.\n", pid);
                process_found = true;
                break;
            }
        }
    }

    if (!process_found) {
        printf("Process %d not found.\n", pid);
    }

    // Call the scheduler function every time a process is stopped
    scheduler();
}

void perform_resume(char* args[]) {
    pid_t pid = atoi(args[0]);
    if (pid <= 0) {
        printf("The process ID must be a positive integer.\n");
        return;
    }

    bool process_found = false;
    for (int i = 0; i < MAX_PROCESSES; ++i) {
        if (process_records[i].pid == pid) {
            if (process_records[i].status == STOPPED) {
                process_records[i].status = READY;
                printf("Process %d resumed and set to READY.\n", pid);
                process_found = true;
                break;
            } else {
                printf("Process %d is not in a stopped state.\n", pid);
                process_found = true;
                break;
            }
        }
    }

    if (!process_found) {
        printf("Process %d not found.\n", pid);
    }

    // Call the scheduler function
    scheduler();
}

void perform_run(char* args[]) {
	int index = -1;
	for (int i = 0; i < MAX_PROCESSES; ++i) {
		if (process_records[i].status == UNUSED) {
			index = i;
			break;
		}
	}
	if (index < 0) {
		printf("no unused process slots available; searching for an entry of a killed process.\n");
		for (int i = 0; i < MAX_PROCESSES; ++i) {
			if (process_records[i].status == TERMINATED) {
				index = i;
				break;
			}
		}
	}

	// Convert the third argument to an integer for total runtime
    int runtime = atoi(args[2]); // Assuming args[2] is the total runtime in seconds
    if (runtime <= 0) {
        printf("Invalid runtime. It must be a positive integer.\n");
        return;
    }

	pid_t pid = fork();
	if (pid < 0) {
		fprintf(stderr, "fork failed\n");
		return;
	}
	if (pid == 0) {
		const int len = strlen(args[0]);
		char exec[len + 3];
		strcpy(exec, "./");
		strcat(exec, args[0]);
		execvp(exec, args);
		// Unreachable code unless execution failed.
		exit(EXIT_FAILURE);
	}
	
	process_record * const p = &process_records[index];
	p->pid = pid;
	p->status = READY;
	gettimeofday(&p->start_time, NULL); // Record start time
    p->last_update_time = p->start_time; // Initialize last update time
    p->total_runtime = runtime * 1000; // Set total runtime for the process
    p->remaining_runtime = p->total_runtime;
	scheduler();
}

void perform_kill(char *args[]) {
    const pid_t pid = atoi(args[0]);
    if (pid <= 0) {
        printf("The process ID must be a positive integer.\n");
        return;
    }
    for (int i = 0; i < MAX_PROCESSES; ++i) {
        process_record *const p = &process_records[i];
        if ((p->pid == pid) && (p->status == RUNNING)) {
            kill(p->pid, SIGTERM);
            printf("[%d] %d killed\n", i, p->pid);
            p->status = TERMINATED;
            return;
        }
    }
    printf("Process %d not found.\n", pid);
}

int compare_process_records(const void *a, const void *b) {
    process_record *const *pa = (process_record *const *)a;
    process_record *const *pb = (process_record *const *)b;
    return (*pa)->pid - (*pb)->pid;
}

void perform_list(void) {
    process_record *sorted_records[MAX_PROCESSES];
    int count = 0;

    // Create an array of pointers to process_records
    for (int i = 0; i < MAX_PROCESSES; ++i) {
        if (process_records[i].status != UNUSED) {
            sorted_records[count++] = &process_records[i];
        }
    }

    // Sort the array of pointers
    qsort(sorted_records, count, sizeof(process_record *), compare_process_records);

    // Display the sorted processes
    if (count == 0) {
        printf("No processes to list.\n");
        return;
    }

    for (int i = 0; i < count; ++i) {
        process_record *p = sorted_records[i];
        printf("%d, %d\n", p->pid, p->status);
    }
}

void perform_exit(void) {
    printf("bye!\n");
}

char *get_input(char *buffer, char *args[], int args_count_max) {
    // capture a command
    printf("\x1B[34m"
           "cs205"
           "\x1B[0m"
           "$ ");
    fgets(buffer, 79, stdin);
    for (char *c = buffer; *c != '\0'; ++c) {
        if ((*c == '\r') || (*c == '\n')) {
            *c = '\0';
            break;
        }
    }
    strcat(buffer, " ");
    // tokenize command's arguments
    char *p = strtok(buffer, " ");
    int arg_cnt = 0;
    while (p != NULL) {
        args[arg_cnt++] = p;
        if (arg_cnt == args_count_max - 1) {
            break;
        }
        p = strtok(NULL, " ");
    }
    args[arg_cnt] = NULL;
    return args[0];
}

int main(void) {
    char buffer[80];
    // NULL-terminated array
    char *args[10];
    const int args_count = sizeof(args) / sizeof(*args);
	for (size_t i = 0; i < MAX_PROCESSES; ++i) {
        process_records[i].status = 4;
    }
    while (true) {
		update_process_times();
        char *const cmd = get_input(buffer, args, args_count);
        if (strcmp(cmd, "kill") == 0) {
            perform_kill(&args[1]);
        } else if (strcmp(cmd, "run") == 0) {
            perform_run(&args[1]);
        } else if (strcmp(cmd, "list") == 0) {
            perform_list();
        } else if (strcmp(cmd, "exit") == 0) {
            perform_exit();
            break;
        } else if (strcmp(cmd, "resume") == 0) {
            perform_resume(&args[1]);
        } else if (strcmp(cmd, "stop") == 0) {
            perform_stop(&args[1]);
        }else {
            printf("invalid command\n");
        }
    }
    return EXIT_SUCCESS;
}
