create type Strutturato as enum ('Ricercatore', 'Professore Associato', 'Professore Ordinato');
create type LavoroProgetto as enum('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro');
create type LavoroNonProgettuale as enum ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro');
create type CausaAssenza as enum ('Chiusura Universitaria', 'Maternita', 'Malattia');
create domain PosInteger as int check(value>=0);
create domain StringaM as varchar(100);
create domain NumeroOre as int check(value>0 and value <8);
create domain Denaro as real check(value>=0);

create table Persona(
    id PosInteger primary key,
    nome StringaM not null,
    cognome StringaM not null,
    posizione Strutturato not null,
    stipendio Denaro not null
);

create table Progetto(
    id PosInteger primary key,
    nome StringaM not null unique,
    inizio data not null,
    fine data not null,
    budget Denaro not null,

    check(inizio<fine),
);

create table WP(
    progetto PosInteger,
    id PosInteger,
    primary key(progetto, id),
    inizio data not null,
    fine data not null,

    check(inizio<fine),
    foreign key progetto references Progetto(id)
);

create table AttivitaProgetto(
    id PosInteger primary key,
    persona PosInteger not null,
    progetto PosInteger not null,
    wp PosInteger not null,
    giorno data not null,
    tipo LavoroProgetto not null,
    oreDurata NumeroOre not null,

    foreign key persona references Persona(id),
    foreign key (progetto,wp) references WP(progetto,id)
);

create table AttivitaNonProgettuale(
    id PosInteger primary key,
    persona PosInteger not null,
    tipo LavoroNonProgettuale not null,
    giorno data not null,
    oreDurata NumeroOre not null,

    foreign key persona references Persona(id)
);

create table Assenza(
    id PosInteger primary key,
    persona PosInteger not null ,
    tipo CausaAssenza not null,
    giorno data not null ,

    unique (persona,giorno),
    foreign key persona references Persona(id)
);
