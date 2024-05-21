
use sakila;

select database();

show tables;

describe actor;

desc actor;

-- desc sakila.actor;
/**/

-- select statement ( DQL)
select * from actor;

SELECT actor_id, first_name,
actor_id*10 
From
ACTOR;


select * from actor;

-- where clause  
-- selection
-- projection 
select * from actor where actor_id<>2;

select * from actor where actor_id!=2;

select first_name
 from actor where actor_id<=2;
 
 select actor_id
 from actor where first_name="NICK";
 
 
 select * from actor
 where actor_id between 2 and 5;
 
 select * from actor
 where actor_id between 5 and 2;
 
 -- in operator
  select * from actor
 where actor_id not in ( 5,2,12);


select * from actor
 where  first_name="ED";

-- pattern find karo  ( like operator)
-- where like "E"  => where col="E"   
select * from actor
 where  first_name like "__%";

