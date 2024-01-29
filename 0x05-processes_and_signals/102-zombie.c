#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop with a sleep of 1 second.
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - Creates 5 zombie processes and prints their PIDs.
 * Return: Always 0.
 */
int main(void)
{
	pid_t child;
	int i;

	for (i = 0; i < 5; i++)
	{
		child = fork();

		if (child == -1)
		{
			perror("Error creating child process");
			exit(EXIT_FAILURE);
		}
		else if (child == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(EXIT_SUCCESS);
		}
		else
		{
			/* Parent process continues the loop */
		}
	}
	infinite_while();
	return (0);
}
