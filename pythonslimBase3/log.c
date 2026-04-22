#define _GNU_SOURCE
#include <stdio.h>
#include <dlfcn.h>
#include <unistd.h>

typedef int (*execve_t)(const char *filename, char *const argv[], char *const envp[]);

// custom execve function that logs the executed command to a file before calling the original execve
int execve(const char *filename, char *const argv[], char *const envp[]) {
    static execve_t original_execve = NULL;
    if (!original_execve) {
        original_execve = (execve_t)dlsym(RTLD_NEXT, "execve");
    }

    // opens log file in 'append' mode
    FILE *log = fopen("/tmp/exec.log", "a");
    if (log) {
        // records the specific path of the binary being executed
        fprintf(log, "Executed: %s\n", filename);
        fclose(log);
    }

    // the original execve function is called 
    return original_execve(filename, argv, envp);
}