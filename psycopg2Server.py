import psycopg2

conn = psycopg2.connect(database = "project", user = "postgres", password = "123456789", host = "127.0.0.1", port = "5432")
print("Opened database successfully")

cur = conn.cursor()
cur.execute('''SELECT now();''')
print("Table created successfully", cur.fetchone())
# cur.execute('''
#     create table department(
#         name VARCHAR(50) NOT NULL UNIQUE,
#         PRIMARY_KEY name
#         );
# ''')


# cur.execute('''
#     create table faculty(
#         Id VARCHAR(50) NOT NULL PRIMARY KEY,
#         noOfLeaves integer NOT NULL,
#         department VARCHAR(25) NOT NULL,
#         FOREIGN KEY(department) references department(name)
#     );
# ''')

cur.execute('''
    create table HOD(
        facultyId VARCHAR(50) NOT NULL,
        DepartName VARCHAR(50) NOT NULL,
        startTime timestamp,
        PRIMARY KEY(facultyId, DepartName),
        FOREIGN KEY(DepartName) references department(name),
        FOREIGN KEY(facultyId) references faculty(Id)
    );
''')

# cur.execute('''
#     create table historyOfHod(
#         departmentName VARCHAR(25) NOT NULL,
#         facultyId VARCHAR(50) NOT NULL,
#         startTime timestamp,
#         endTime timestamp,
#         PRIMARY KEY(departmentName, facultyId),
#         FOREIGN KEY(departmentName) references department(name),
#         FOREIGN KEY(facultyId) references faculty(Id)
#     );
# ''')

# cur.execute('''
#     create table crossFaculty(
#         facultyId VARCHAR(50) NOT NULL,
#         position VARCHAR(50) NOT NULL PRIMARY KEY,
#         startTime timestamp,
#         FOREIGN KEY(facultyId) references faculty(Id)
#     )
# ''')

# cur.execute('''
#     create table historyOfCrossCut(
#         facultyId VARCHAR(50) NOT NULL,
#         position VARCHAR(50) NOT NULL,
#         startTime timestamp,
#         endTime timestamp,
#         PRIMARY KEY(facultyId, position),
#         FOREIGN KEY(facultyId) references faculty(Id),
#         FOREIGN KEY(position) references crossFaculty(position)
#     )
# ''')


conn.commit()
conn.close()