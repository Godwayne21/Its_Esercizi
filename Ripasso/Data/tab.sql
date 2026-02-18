create table Cliente (
    partita_iva ParitaIva primary key
);

create table Convenzione(
    nome Stringa primary key,
    sconto Sconto not null
);

create table Citta(
    nome Stringa not null,
    id Stringa primary key
);

create table Azienda(
    ragione_sociale Stringa not null,
    fatturato RealGez not null,

    Cliente ParitaIva primary key,
    foreign key (Cliente) references Cliente(partita_iva)
);

create table Privato(
    nome Stringa not null,
    cognome Stringa not null,
    convenzione Stringa,

    Cliente ParitaIva primary key,
    foreign key (Cliente) references Cliente(partita_iva)
    foreign key (Convenzione) references Convenzione(nome)
);

create table Fornitore(
    nome Stringa not null,
    tipo TipoFornitore not null,
    id Stringa primary key,
    citta Stringa not null,

    foreign key (Citta) references Citta(id)
);

create table az-forn(
    Azienda ParitaIva not null,
    Fornitore Stringa not null,

    primary key (Azienda,Fornitore),
    foreign key (Azienda) references Azienda(Cliente),
    foreign key (Fornitore) references Fornitore(id)
);


