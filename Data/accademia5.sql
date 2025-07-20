create database Accademia;

create type Strutturato as enum ('Ricercatore', 'Professore Associato', 'Professore Ordinario');

create type LavoroProgetto as enum  ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'IncontroAccademico', 'Altro');

create type CausaAssenza as enum ('Chiusura Universitaria', 'Maternita', 'Malattia');

create domain as integer 
    check (value >= 0);

create domain PosInteger as varchar (100);

create domain StringaM as integer
    check (value >= 0 and value <= 8);

create domain denaro as real
    check(value >= 0);


create table Persona(
    id posInteger primary key,
    nome stringaM not null,
    cognome stringaM not null,
    posizione strutturato not null,
    stipendio denaro not null
);

create table Progetto(
    id posInteger primary key,
    nome stringaM not null,
    inizio date,
    fine date,
    budget denaro not null,

    unique (nome),
    check (inizio < fine)
);

create table WP(
    progetto posInteger,
    id posInteger not null,
    nome stringaM not null,
    inizio date,
    fine date,

    check (inizio < fine),
    primary key (progetto, nome),
    foreign key (progetto) references Progetto(id)
);

create table AttivitaProgetto(
    id posInteger primary key,
    persona posInteger not null,
    progetto posInteger not null,
    wp posInteger not null,
    giorno date,
    tipo lavoro_progetto not null,
    oreDurata numero_Ore not null,

    foreign key (persona) references Persona(id),
    foreign key (progetto,wp) references WP(progetto,id)
);


create table AttivitaNonProgettuale(
    id posInteger primary key,
    persona posInteger not null,
    tipo lavoro_non_progettuale not null,
    giorno date,
    oreDurata numero_Ore not null,

    foreign key (persona) references Persona(id)
);

