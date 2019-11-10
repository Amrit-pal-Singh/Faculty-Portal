

create function changeHod(department VARCHAR(25), faculty VARCHAR(50))
returns void as $$
declare
begin
    update hod 
            set facultyId = faculty, startTime = now()
            where DepartName = department
end;
$$
language plpgsql;


create or replace changedHodTrigger()
returns TRIGGER as $$
declare

begin
    insert into historyOfHod(departmentName, facultyId, startTime, endTime) values (old.DepartName, old.facultyId, old.startTime, now())
    return new;
end;
$$
language plpgsql;


create TRIGGER HodChangeLog
before update
on HOD
for each row
execute procedure changedHodTrigger()




create function changeCross(position VARCHAR(25), faculty VARCHAR(50))
returns void as $$
declare
begin
    update hod 
            set postion = position, startTime = now()
            where facultyId = faculty
end;
$$
language plpgsql;



create or replace changedCrossTrigger()
returns TRIGGER as $$
declare

begin
    insert into historyOfCrossCut(facultyId, position, startTime, endTime) values (old.facultyId, old.position, old.startTime, now())
    return new;
end;
$$
language plpgsql;


create TRIGGER CrossChangeLog
before update
on crossFaculty
for each row
execute procedure changedCrossTrigger()
