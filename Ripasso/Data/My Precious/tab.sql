create domain Stringa as varchar(100)
create domain RealGez as real (check value>=0)

create table Nazione(
    nome Stringa primary key,
);

create table Regione(
    nome Stringa not null,
    nazione Stringa not null,

    primary key (nome, Nazione),
    foreign key (nazione) references Nazione(nome)
);

create table Citta(
    id Stringa primary key,
    nome Stringa not null,
    regione Stringa not null,
    nazione Stringa not null,

    unique (nome,regione,nazione),
    foreign key(regione,nazione) references regione(nome,nazione)
);

create table Artista(
    id Stringa primary key,
    nome_arte Stringa not null,
    data_nascita date not null,
    data_morte date,
    citta Stringa not null,

    foreign key (citta) references citta(id)
);

create table Opera(
    id Stringa primary key,
    nome: Stringa not null,
    anno_realizzazione Integer not null,
    artista Stringa,
    tecnica Stringa,
    categoria Stringa not null,
    correnteArtistica Stringa not null,

    foreign key (correnteArtistica) references correnteArtistica(id),
    foreign key (categoria) references categoria (id),
    foreign key (tecnica) references tecnica(id),
    foreign key (artista) references artista(id)
);

create table Tecnica(
    id Stringa primary key,
    nome Stringa not null,
);

create table Categoria(
    id Stringa primary key,
    nome Stringa not null,
);

create table CorrenteArtistica(
    id Stringa primary key,
    nome Stringa not null,
);

create table Op_Corr(
    opera Stringa not null,
    correnteArtistica Stringa not null,

    primary key(opera, correnteArtistica),
    foreign key(opera) references opera(id)
    foreign key (correnteArtistica) references correnteArtistica(id)
);

create table Esposizione(
    id Integer primary key,
    nome Stringa not null,
    inizio date not null,
);

create table Espone(
    inizio date not null,
    fine date,
    opera Stringa not null,
    esposizione Integer not null,

    primary key (opera, esposizione),
    foreign key(opera) references opera(id),
    foreign key (esposizione) references esposizione(id)
);

create table Temporanea(
    fine date not null,
    tema Stringa not null,
    prezzo_accesi RealGez not null,
    esposizione Integer primary key,

    foreign key(esposizione) references esposizione(id)
);

create table Permanente(
    esposizione Integer primary key,

    foreign key (esposizione) references esposizione(id)
);

create table Biglietto(
    id Stringa primary key,
    istante_vendita Timestamp not null,
    validita date not null,
    tariffa Stringa not null,

    foreign key (tariffa) references tariffa(nome)
);

create table Tariffa(
    nome Stringa primary key,
    prezzo_base RealGez not null
);

create table Standard(
    biglietto Stringa primary key,

    foreign key(biglietto) references biglietto(id)
);

create table Extended(
    biglietto Stringa primary key,

    foreign key(biglietto) references biglietto(id)
);

create table Ext_Temp(
    extended Stringa not null,
    temporanea Integer not null,

    primary key(extended, temporanea),
    foreign key(extended) references extended(biglietto),
    foreign key (temporanea) references temporanea (esposizione)
);