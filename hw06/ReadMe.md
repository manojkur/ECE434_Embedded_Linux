1. Where does Julia Cartwright work?
National Insturments

2. What is PREEMT_RT? Hint: Google it.
It is a patch on top of the linux kernel which makes it have real time scheduling.

3. What is mixed criticality?
The ability to run both time based and non time based tasks at the same time.

4. How can drivers misbehave?
If a driver is used at the same time for multiple tasks, they can misbehave.

5. What is delta in Figure 1?
It is the elapsed time from when an event is scheduled to happen to when it actually does happen.

6. What is Cyclictest[2]?
It takes two timestamps and sleeps for a specified amount of time between the timestamps. Then it takes the elapsed time from the the two timestamps and subtracts the sleep time, the result is delta.

7. What is plotted in Figure 2?
The cyclic test for the real-time kernel.

8. What is dispatch latency? Scheduling latency?
Dispatch latency: The time from an interrupt occuring to when the specified event runs.
Scheduling latency: The time it takes from the scheduler being aware of a task to when it acually runs it.

9. What is mainline?
It has a list of interrupts in the main execution line.

10. What is keeping the External event in Figure 3 from starting?
It is the low priority interrupts.

11. Why can the External event in Figure 4 start sooner?
The low priority interrupt is interrupted. That allows the External event to start sooner.

========================
Professor Yoder's Comments

Looks good

Late

Score: 9/10
