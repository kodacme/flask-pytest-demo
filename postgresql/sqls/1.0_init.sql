
drop table if exists fruits cascade;

create table fruits (
  id varchar(64),
  name varchar(255),
  fruit_type varchar(64),
  is_deleted boolean default false,
  primary key(id)
);

insert into
  fruits
values
  ('537827e5-03fe-4381-026b-d84e4e460723', 'Yubari Melon', 'MELON', false);
