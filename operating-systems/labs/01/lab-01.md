- cmd: grep <word> <file>
	- i case insensitive
	- v display those lines that do NOT match
	- n precede each matching line with the line number
	- c print only the total count of matched lines
	

- cmd: chmod

{
	- Type
	rwx Owner
	rwx Group
	rwx Others
}
	
chmod u+w file.txt   		  # Add owner write permission
chmod g-w file.txt   		  # Remove group write permission
chmod o-r file.txt   		  # Remove others' read permission
chmod a+x script.sh  		  # Add execute permission for everyone
chmod u=rwx,g=rx,o= file.txt  # The owner gets rwx, the group gets r-x, and others get no permissions

Each permission has a number:
	r = 4
	w = 2
	x = 1
	rwx	=> 4 + 2 + 1	 = 7

- files versus directories	
Permission | FILE             | DIR
-----------|------------------|-------------------------------
r          | Read contents    | List filenames
w          | Modify contents  | Create, delete, rename entries
x          | Execute program  | Enter/traverse directory
