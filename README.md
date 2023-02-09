# 0x00. AirBnB clone - The console

https://user-images.githubusercontent.com/99409347/183261652-1bdb8fd9-f792-440c-8954-f5c576f8dc88.png

This is a first step in building our first full web application **the AirBnB clone**. This forms the basis with which  all other projects will be based on. 
A basic console is created using the Cmd Python module, to manage the objects of the whole project, being able to implement the methods create, show, update, all, and destroy to the existing classes and subclasses.

## Execution
The console can work in both interactive and non-onteractive mode

### Interactive Mode:
'$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$'
### Non-Interactive Mode:
'$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$'
## Authors
[Emmanuel Appiah](https://github.com/eldray)
[Adewale Liadi](https://github.com/jesusenerio)