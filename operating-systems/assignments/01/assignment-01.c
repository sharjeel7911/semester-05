/* GLOBAL SCOPE */
#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

#define MAX_STUDENTS 50
#define NAME_LENGTH 50
#define TOTAL_MARKS 250.0
#define INPUT_FILE "students-data.csv"

typedef struct {
	int id;
	char name[NAME_LENGTH];
	double marks;
	double percentage;
	char grade[3];
} Student;

/* ---------- METHODS ---------- */

static void bind_to_cpu(int);
static void write_all(int, const void*, size_t);
static void read_all(int, void*, size_t);
static int compare_by_marks_ascending(const void*, const void*);
static int read_students_from_file(const char*, Student[]);
static void percentage_child(int, int);
static void grade_child(int, int);
void print_results(Student[], int);

/* ---------- Main ---------- */

int main(void) {
	Student students[MAX_STUDENTS];
	int student_count = read_students_from_file(INPUT_FILE, students);
	if (student_count == 0) {
		fprintf(stderr, "No students found in %s\n", INPUT_FILE);
		return 1;
	}

	bind_to_cpu(0);

	int parent_to_child1[2], child1_to_child2[2], child2_to_parent[2];
	if (pipe(parent_to_child1) < 0 || pipe(child1_to_child2) < 0 || pipe(child2_to_parent) < 0) {
		perror("pipe");
		return 1;
	}

	pid_t child1_pid = fork();
	if (child1_pid == 0) {
		close(parent_to_child1[1]);
		close(child1_to_child2[0]);
		close(child2_to_parent[0]);
		close(child2_to_parent[1]);
		percentage_child(parent_to_child1[0], child1_to_child2[1]);
	}

	pid_t child2_pid = fork();
	if (child2_pid == 0) {
		close(parent_to_child1[0]);
		close(parent_to_child1[1]);
		close(child1_to_child2[1]);
		close(child2_to_parent[0]);
		grade_child(child1_to_child2[0], child2_to_parent[1]);
	}

	close(parent_to_child1[0]);
	close(child1_to_child2[0]);
	close(child1_to_child2[1]);
	close(child2_to_parent[1]);

	write_all(parent_to_child1[1], &student_count, sizeof student_count);
	write_all(parent_to_child1[1], students, student_count * sizeof(Student));
	close(parent_to_child1[1]);

	int graded_count;
	Student graded_students[MAX_STUDENTS];
	read_all(child2_to_parent[0], &graded_count, sizeof graded_count);
	read_all(child2_to_parent[0], graded_students, graded_count * sizeof(Student));
	close(child2_to_parent[0]);

	waitpid(child1_pid, NULL, 0);
	waitpid(child2_pid, NULL, 0);

	qsort(graded_students, graded_count, sizeof(Student), compare_by_marks_ascending);
	print_results(graded_students, graded_count);
	return 0;
}

static void bind_to_cpu(int cpu) {
	cpu_set_t cpu_set;
	CPU_ZERO(&cpu_set);
	CPU_SET(cpu, &cpu_set);
	if (sched_setaffinity(0, sizeof cpu_set, &cpu_set) != 0) perror("sched_setaffinity");
}

static void write_all(int fd, const void* data, size_t size) {
	const char* cursor = data;
	while (size > 0) {
		ssize_t sent = write(fd, cursor, size);
		if (sent <= 0) {
			perror("write");
			exit(1);
		}
		cursor += sent;
		size -= (size_t)sent;
	}
}

static void read_all(int fd, void* data, size_t size) {
	char* cursor = data;
	while (size > 0) {
		ssize_t received = read(fd, cursor, size);
		if (received <= 0) {
			perror("read");
			exit(1);
		}
		cursor += received;
		size -= (size_t)received;
	}
}

static int compare_by_marks_ascending(const void* a, const void* b) {
	const Student* first = a;
	const Student* second = b;
	if (first->marks < second->marks) return -1;
	if (first->marks > second->marks) return 1;
	return 0;
}

static int read_students_from_file(const char* file_name, Student students[]) {
	FILE* file = fopen(file_name, "r");
	if (file == NULL) {
		perror("fopen");
		exit(1);
	}

	char line[256];
	int student_count = 0;

	// skip header row
	fgets(line, sizeof line, file);

	while (student_count < MAX_STUDENTS && fgets(line, sizeof line, file) != NULL) {
		Student* current = &students[student_count];
		if (sscanf(line, "%d,%49[^,],%lf", &current->id, current->name, &current->marks) == 3) {
			current->percentage = 0.0;
			current->grade[0] = '\0';
			student_count++;
		}
	}
	fclose(file);
	return student_count;
}

static void percentage_child(int input_fd, int output_fd) {
	bind_to_cpu(1);

	int student_count;
	Student students[MAX_STUDENTS];

	read_all(input_fd, &student_count, sizeof student_count);
	read_all(input_fd, students, student_count * sizeof(Student));
	close(input_fd);

	for (int i = 0; i < student_count; i++) students[i].percentage = students[i].marks * 100.0 / TOTAL_MARKS;

	write_all(output_fd, &student_count, sizeof student_count);
	write_all(output_fd, students, student_count * sizeof(Student));
	close(output_fd);
	exit(0);
}

static void grade_child(int input_fd, int output_fd) {
	bind_to_cpu(2);

	int student_count;
	Student students[MAX_STUDENTS];

	read_all(input_fd, &student_count, sizeof student_count);
	read_all(input_fd, students, student_count * sizeof(Student));
	close(input_fd);

	for (int i = 0; i < student_count; i++) {
		double percentage = students[i].percentage;
		if (percentage >= 90.0)
			strcpy(students[i].grade, "A+");
		else if (percentage >= 80.0)
			strcpy(students[i].grade, "A");
		else if (percentage >= 70.0)
			strcpy(students[i].grade, "B");
		else if (percentage >= 60.0)
			strcpy(students[i].grade, "C");
		else if (percentage >= 50.0)
			strcpy(students[i].grade, "D");
		else
			strcpy(students[i].grade, "F");
	}

	write_all(output_fd, &student_count, sizeof student_count);
	write_all(output_fd, students, student_count * sizeof(Student));
	close(output_fd);
	exit(0);
}

void print_results(Student graded_students[], int graded_count) {
	printf("%-6s | %-22s | %-10s | %-12s | %-8s\n", "ID", "Name", "Marks", "Percentage", "Grade");
	printf("----------------------------------------------------------------------\n");
	for (int i = 0; i < graded_count; i++) {
		char percentage_text[16];
		snprintf(percentage_text, sizeof percentage_text, "%.2f%%", graded_students[i].percentage);

		printf("%-6d | %-22s | %-10.2f | %-12s | %-8s\n", graded_students[i].id, graded_students[i].name, graded_students[i].marks, percentage_text, graded_students[i].grade);
	}
}