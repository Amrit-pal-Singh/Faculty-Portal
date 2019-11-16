create or replace function changeHod(department VARCHAR(50), faculty VARCHAR(50))
returns void as $$
declare
check_ integer;
begin
    select count(DepartName) into check_
    from hod
    where DepartName = department;
    if(check_ >= 1) then
        update hod 
            set facultyId = faculty, startTime = now()
            where DepartName = department;
    else
        insert into hod(facultyId, DepartName, startTime) values (faculty, department, now());
    end if;
    return;
end;
$$
language plpgsql;


create or replace function changedHodTriggerUpdate()
returns TRIGGER as $$
declare
begin
    insert into historyOfHod(departmentName, facultyId, startTime, endTime) values (old.DepartName, old.facultyId, old.startTime, now());
    return new;
end;
$$
language plpgsql;


-- return old
create or replace function changedHodTriggerDelete()
returns TRIGGER as $$
declare
begin
    insert into historyOfHod(departmentName, facultyId, startTime, endTime) values (old.DepartName, old.facultyId, old.startTime, now());
    return old;
end;
$$
language plpgsql;



drop trigger HodChangeLog1 on HOD;

create TRIGGER HodChangeLog1
before update
on HOD
for each row
execute procedure changedHodTriggerUpdate();

drop trigger HodChangeLog2 on HOD;


create TRIGGER HodChangeLog2
before delete
on HOD
for each row
execute procedure changedHodTriggerDelete();



-- # DIR
-- # DEANAA
-- # DEANRA
-- # DEANSA
-- # ADEANFA
-- # ADEANAA
-- # ADEANRA
-- # ADEANSA

create or replace function changeCross(position_ VARCHAR(50), faculty VARCHAR(50))
returns void as $$
declare
check_ integer;

begin
    select count(position) into check_
    from crossFaculty
    where position = position_;
    if(check_ >= 1) then
        update crossFaculty 
            set facultyId = faculty, startTime = now()
            where position = position_;
    else
        insert into crossFaculty(facultyId, position, startTime) values (faculty, position_, now());
    end if;
    
    
end;
$$
language plpgsql;



create or replace function changedCrossTriggerUpdate()
returns TRIGGER as $$
declare

begin
    insert into historyOfCrossCut(facultyId, position, startTime, endTime) values (old.facultyId, old.position, old.startTime, now());
    return new;
end;
$$
language plpgsql;


create or replace function changedCrossTriggerDelete()
returns TRIGGER as $$
declare

begin
    insert into historyOfCrossCut(facultyId, position, startTime, endTime) values (old.facultyId, old.position, old.startTime, now());
    return old;
end;
$$
language plpgsql;




drop trigger CrossChangeLog1 on crossFaculty;

create TRIGGER CrossChangeLog1
before update
on crossFaculty
for each row
execute procedure changedCrossTriggerUpdate();

drop trigger CrossChangeLog2 on crossFaculty; 

create TRIGGER CrossChangeLog2
before delete
on crossFaculty
for each row
execute procedure changedCrossTriggerDelete();