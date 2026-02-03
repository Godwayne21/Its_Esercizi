create domain Stringa as varchar(100);
create domain RealGez as real check(value>=0);

create table Nazione(
    nome Stringa primary key
);

create table Regione(
    nome Stringa not null,
    nazione Stringa not null,

    primary key (nome,nazione),
    foreign key (nazione) references Nazione(nome)
);

create table Citta(
    nome Stringa not null,
    nazione Stringa not null,
    regione Stringa not null,
    id Integer primary key,

    unique (nazione,regione,nome),
    foreign key (regione,nazione) references Regione(nome,nazione)
);

create table Artista(
    id Integer primary key,
    nome_arte Stringa not null,
    data_nascita date not null,
    data_morte date
);

create table Tecnica(
    nome Stringa primary key
);

create table Categoria(
    nome Stringa primary key
);

create table CorrenteArtistica(
    nome Stringa primary key
);

create table Opera(
    id Integer primary key,
    nome Stringa not null,
    anno_realizzazione Integer not null,
    tecnica Stringa,
    categoria Stringa not null,
    artista Integer not null,

    foreign key (tecnica) references Tecnica(nome),
    foreign key (categoria) references Categoria(nome),
    foreign key (artista) references Artista(id)
);

create table Op_Cor(
    correnteArtistica Stringa not null,
    opera Integer not null,

    primary key (correnteArtistica, opera),
    foreign key (correnteArtistica) references CorrenteArtistica(nome),
    foreign key (opera) references Opera(id)
);

create table Esposizione(
    id Integer primary key,
    inizio date not null,
    nome Stringa not null
);

create table Espone(
    opera Integer not null,
    esposizione Integer not null,
    inizio date not null,
    fine date,

    primary key(opera,esposizione),
    foreign key (opera) references Opera(id),
    foreign key (esposizione) references Esposizione(id)
);

create table Temporanea(
    esposizione Integer primary key,
    fine date not null,
    tema Stringa not null,
    prezzo_accesso RealGez not null,

    foreign key (esposizione) references Esposizione(id)
);

create table Permanente(
    esposizione Integer primary key,

    foreign key (esposizione) references Esposizione(id)
);

create table Tariffa(
    nome Stringa primary key,
    prezzo_base RealGez not null
);

create table Biglietto(
    id Integer primary key,
    istante_vendita timestamp not null,
    validita date not null,
    tariffa Stringa not null,

    foreign key (tariffa) references Tariffa(nome)
);

create table Bigl_Esp(
    biglietto Integer not null,
    esposizione Integer not null,

    primary key(biglietto, esposizione),
    foreign key (biglietto) references Biglietto(id),
    foreign key (esposizione) references Esposizione(id)
);

create table Standard(
    biglietto Integer primary key,

    foreign key (biglietto) references Biglietto(id)
);

create table Extended(
    biglietto Integer primary key,

    foreign key (biglietto) references Biglietto(id)
);

create table Ext_Temp(
    extended Integer not null,
    temporanea Integer not null,

    primary key(extended,temporanea),
    foreign key (extended) references Extended(biglietto),
    foreign key (temporanea) references Temporanea(esposizione)
);