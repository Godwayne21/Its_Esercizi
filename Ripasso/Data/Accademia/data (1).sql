insert into categoria(nome, super)
values
('Elettronica', NULL),
('Informatica', 'Elettronica'),
('Laptop', 'Informatica'),
('Casa e giardino', NULL),
('Arredamento', 'Casa e giardino'),
('Giardino', 'Casa e giardino');


insert into metodopagamento(nome)
values
('Carta di credito'),
('Bonifico'),
('PayPal'),
('Carta regalo');

insert into postoggetto(id, ...)
values
(1, ...)
(2, ...)

insert into met_post(postoggetto, metodo)
values
(1, 'Carta di cretito'),
(1, 'Bonifico'),
(2, 'Bonifico');


