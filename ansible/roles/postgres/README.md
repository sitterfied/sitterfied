PostgreSQL
==========

An open-source relational database.

Procedures for Testing with Vagrant
-----------------------------------

Testing on a single VM for now:

    $ vagrant up node1
    $ ansible-playbook playbooks/postgresql.yml --limit=node1

(Note: you may use any node -- node1, node 2 and node3. If you are using those
nodes for other testing, we can add others.)

Caveats
-------

PostgreSQL is installed along with psycopg2 (a dependency for the Ansible
PostgreSQL modules to function). Also, to ensure databases are created
using UTF-8, the locale (LC\_ALL) has been set to "en\_US.utf8".

This is a base install, so standard tutorials about using the postgres
user will work. So logging in via command line should work like this...

    $ vagrant ssh node1
    $ sudo -u postgres psql
    psql (9.1.11)
    Type "help" for help.

    vagrant=# \list
                                     List of databases
       Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges
    -----------+----------+----------+------------+------------+-----------------------
     postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
     template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
               |          |          |            |            | postgres=CTc/postgres
     template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
               |          |          |            |            | postgres=CTc/postgres
    (3 rows)

    postgres=# \q


References
----------

* [Upstream Documentation](http://www.postgresql.org/docs/)
