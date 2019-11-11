create or replace function changeHod(department VARCHAR(50), faculty VARCHAR(50))
returns void as $$
declare
check_ integer;
begin
    select count(DepartName) into check_
    from hod
    where DepartName = department;
    if(check_ > 1) then
        update hod 
            set facultyId = faculty, startTime = now()
            where DepartName = department;
    else
        insert into hod(facultyId, DepartName, startTime) values (faculty, department, now());
    end if;
    
end;
$$
language plpgsql;


create or replace function changedHodTrigger()
returns TRIGGER as $$
declare
begin
    insert into historyOfHod(departmentName, facultyId, startTime, endTime) values (old.DepartName, old.facultyId, old.startTime, now());
    return new;
end;
$$
language plpgsql;

drop trigger HodChangeLog on HOD;

create TRIGGER HodChangeLog
before update
on HOD
for each row
execute procedure changedHodTrigger();



create or replace function changeCross(position_ VARCHAR(50), faculty VARCHAR(50))
returns void as $$
declare
check_ integer;

begin
    select count(position) into check_
    from crossFaculty
    where position = position_;
    if(check_ > 1) then
        update crossFaculty 
            set postion = position_, startTime = now()
            where facultyId = faculty;
    else
        insert into crossFaculty(facultyId, position, startTime) values (faculty, position_, now());
    end if;
    
    
end;
$$
language plpgsql;



create or replace function changedCrossTrigger()
returns TRIGGER as $$
declare

begin
    insert into historyOfCrossCut(facultyId, position, startTime, endTime) values (old.facultyId, old.position, old.startTime, now());
    return new;
end;
$$
language plpgsql;

drop trigger CrossChangeLog on crossFaculty;

create TRIGGER CrossChangeLog
before update
on crossFaculty
for each row
execute procedure changedCrossTrigger();