// Write a C program stores the information (id, name, age and pay) of an employee and
// displays it on the screen using structures
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	int id;
	char name[50];
	int age;
	int pay;
} Employee;

typedef struct {
	int id;
	char* name;
	int age;
	int pay;
} EmployeePtr;

int main() {
	Employee emp1;
	printf("Enter employee id: ");
	scanf("%d", &emp1.id);
	printf("Enter employee name: ");
	scanf("%s", emp1.name);
	printf("Enter employee age: ");
	scanf("%d", &emp1.age);
	printf("Enter employee pay: ");
	scanf("%d", &emp1.pay);

	printf("\nEmployee Details:\n");
	printf("ID: %d\nName: %s\nAge: %d\nPay: %d\n", emp1.id, emp1.name, emp1.age, emp1.pay);

	// ====================================================================================================

	Employee emp2 = emp1;  // Copying emp to emp2
	printf("\nCopied Employee Details:\n");
	printf("ID: %d\nName: %s\nAge: %d\nPay: %d\n", emp2.id, emp2.name, emp2.age, emp2.pay);

	// ====================================================================================================

	Employee emp3 = {9, "Shar", 30, 50000};
	printf("\nInitialized Employee Details:\n");
	printf("ID: %d\nName: %s\nAge: %d\nPay: %d\n", emp3.id, emp3.name, emp3.age, emp3.pay);

	// ====================================================================================================

	Employee* emp4 = (Employee*)malloc(sizeof(Employee));
	if (emp4 == NULL) {
		printf("Memory allocation failed\n");
		return 1;
	}
	emp4->id = 10;
	// strcpy(emp4->name, "John");
	memcpy(emp4->name, "John", sizeof("John"));
	emp4->age = 28;
	emp4->pay = 60000;
	printf("\nDynamically Allocated Employee Details:\n");
	printf("ID: %d\nName: %s\nAge: %d\nPay: %d\n", emp4->id, emp4->name, emp4->age, emp4->pay);
	free(emp4);

	// ====================================================================================================

	// Using pointer to struct

	EmployeePtr emp5;
	emp5.id = 11;
	emp5.age = 35;
	emp5.pay = 70000;
	emp5.name = NULL;

	printf("Enter employee name: ");
	char temp_name[100];
	scanf("%s", temp_name);
	emp5.name = (char*)malloc(strlen(temp_name) + 1);
	if (emp5.name == NULL) {
		printf("Memory allocation failed\n");
		return 1;
	}
	strcpy(emp5.name, temp_name);

	printf("\nEmployee Details (Using ptr for name):\n");
	printf("ID: %d\nName: %s\nAge: %d\nPay: %d\n", emp5.id, emp5.name, emp5.age, emp5.pay);
	free(emp5.name);

	// ====================================================================================================

	EmployeePtr* emp6 = (EmployeePtr*)malloc(sizeof(EmployeePtr));
	if (emp6 == NULL) {
		printf("Memory allocation failed\n");
		return 1;
	}

	emp6->id = 12;
	emp6->age = 30;
	emp6->pay = 70000;

	printf("Enter employee 6 name: ");
	scanf("%99s", temp_name);  // Reuse temp buffer

	emp6->name = (char*)malloc(strlen(temp_name) + 1);
	if (emp6->name == NULL) {
		printf("Memory allocation failed\n");
		free(emp6);
		return 1;
	}
	strcpy(emp6->name, temp_name);

	printf("\nEmployee 6 Details (Using ptr for name and obj allocation):\n");
	printf("ID: %d\nName: %s\nAge: %d\nPay: %d\n", emp6->id, emp6->name, emp6->age, emp6->pay);
	free(emp6->name);
	free(emp6);

	return 0;
}