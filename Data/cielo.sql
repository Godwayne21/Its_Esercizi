create database Cielo

create domain postinteger as integer
    check (value >= 0);

create domain stringam as varchar (100);

create domain codIATA as char(3);

create table compagnia(
    nome stringam primary key,
    annodfondaz postinteger not null
);

create table volo (
    codice postinteger not null,
    comp stringam not null,
    primary key (codice, comp),
    durataMinuti postinteger not null,
    foreign key (comp)
        references compagnia(nome)

    --Posticipo la definizione della foreign 
    --key (codice, comp) verso ArrPart per 
    --evitare errori

);

create table aereoporto(
    codice codIATA primary key,
    nome stringam not null,
    --Posticipo 
);

create table luogoaereoporto (
    aereoporto codIATA primary key,
    citta stringam not null,
    nazione stringam not null,

)

create table arrpart (
    codice postinteger not null,
    comp stringam not null,
    primary key (codice, comp),
    foreign key (codice, comp)
        references volo(codice, comp),
    partenza codIATA not null,
    arrivo codIATA not null,
    fk...
);

alter table volo
    add constraint volo arrpart_fk
    foreign key (codice,comp)
        references arrpart(codice,comp)