create domain RealGEZ as real
    check(value>= 0);

create domain Stringa as varchar;

create domain Cap as char (5)
    check(value ~ '[0-9] {5}');

create type Indirizzo as (
    via Stringa ,
    civico Stringa,
);

