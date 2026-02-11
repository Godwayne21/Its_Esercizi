create domain Stringa as varchar;

create type Condizione as enum
	('Ottimo', 'Buono', 'Discreto', 'Da sistemare');


create domain URL as varchar;
--	check (value ~ '...');

create domain Voto as integer
	check (value between 0 and 5);

create domain IntGEZ as integer
	check (value >= 0);

create domain IntGZ as integer
	check (value > 0);

create domain IntGE2 as integer
	check (value >= 2);

create domain RealGEZ as real
	check (value >= 0);

create domain RealGZ as real
	check (value > 0);


