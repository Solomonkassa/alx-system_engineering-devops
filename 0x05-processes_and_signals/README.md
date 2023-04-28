# Processes and Signals
---------------------------------------------------------------------------------------------------------------------------------------------------------------
In computing, a process is the instance of a computer program that is being executed by one or many threads. A process has its own memory space, resources, and system state. A signal is a software interrupt that is sent to a process or a thread to notify it of an event or to request its attention.

This document aims to provide a brief overview of processes and signals in Unix-based operating systems.

# Processes

In Unix-based operating systems, a process is an instance of a running program. Each process has a unique process ID (PID) that identifies it. Processes can be created by other processes, and they can communicate with each other by using inter-process communication (IPC) mechanisms, such as pipes, sockets, and shared memory.

# Process States

A process can be in one of the following states:

   * Running: The process is currently executing on a CPU.
   * Blocked: The process is waiting for an event to occur (such as I/O).
   * Sleeping: The process is waiting for a certain amount of time to elapse before resuming execution.
   * Stopped: The process has been stopped (e.g., by a debugger).
   * Zombie: The process has terminated, but its parent has not yet called wait() to retrieve its exit status.

# Process Management

In Unix-based operating systems, processes can be managed using system calls such as fork(), exec(), and wait(). The fork() system call creates a new process by duplicating the calling process. The exec() system call replaces the current process image with a new process image. The wait() system call suspends the calling process until one of its child processes terminates.

# Signals

A signal is a software interrupt that is sent to a process or a thread to notify it of an event or to request its attention. Signals are identified by integer constants, such as SIGINT, SIGTERM, and SIGKILL.

# Signal Handling

In Unix-based operating systems, signals can be handled using signal handlers, which are functions that are executed when a signal is received. Signal handlers can be installed using the signal() or sigaction() system calls.
Common Signals

Some of the most common signals are:

  - SIGINT: Interrupt from keyboard (e.g., Ctrl+C).
  - SIGTERM: Termination request.
  - SIGKILL: Termination signal (cannot be caught or ignored).
  - SIGSTOP: Stop process (cannot be caught or ignored).
  - SIGCONT: Continue process that has been stopped.

# Conclusion

Processes and signals are fundamental concepts in Unix-based operating systems. Processes are instances of running programs, and signals are software interrupts that can be sent to processes to notify them of events or to request their attention. Understanding how processes and signals work is essential for system programming and debugging.
