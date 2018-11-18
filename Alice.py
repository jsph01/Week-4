import sqlite3

con = sqlite3.connect('c:\sqlite\pcfb.db')
#con.execute('create table people(contact_id integer primary key, first_name text not null, job_title text not null, phone text not null, office_number text not null)')
#con.execute("insert into people(first_name, job_title, phone, office_number) values('Alice', 'Research Director', '555-123-0001', '4b')")

#con.execute('create table people (id integer primary key, name varchar, position varchar,phone varchar,office varchar);')
#con.execute('create table experiment (id integer primary key, name varchar, researcher integer, description text, foreign key(researcher) references people(id));')

con.execute("insert into people(name, position, phone, office) values ( 'Alice', 'Research Director', '555-123-0001', '4b');")
con.execute("insert into people(name, position, phone, office) values ( 'Bob', 'Research assistant', '555-123-0002', '17');")
con.execute("insert into people(name, position, phone, office) values ( 'Charles', 'Research assistant', '555-123-0001', '24');")
con.execute("insert into people(name, position, phone, office) values ( 'David', 'Research assistant', '555-123-0001', '8');")

con.execute("insert into experiment(name, researcher, description) values ( 'EBV Vaccine trial', '1', 'A vaccine trial');")
con.execute("insert into experiment(name, researcher, description) values ( 'Flu antibody study', '2', 'Study of the morphology of flu antibodies');")

#add new user
con.execute("insert into people(name, position, phone, office) values ( 'John', 'Research Director', '555-123-0003', '5b');")
#delete Alice
con.execute("delete from people where name = 'Alice'")
con.execute("update experiment set researcher = 5 where name = 'EBV Vaccine trial'")
r = con.execute('select p.name, e.name from people as p join experiment as e where e.researcher == p.id')

for i in r:
    print('Name: %s\n\tExperiment: %s' % (i[0],i[1]))

r = con.execute('select * from people')
   
for i in r:
    print(i)