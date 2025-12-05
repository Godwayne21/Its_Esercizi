select *
from progetto
where fine > '2023-12-31';

select posizione, count(*) as totale
from persona
group by posizione;

select id,nome
from persona
where id in (
select id
from assenza
where tipo = 'Malattia');

elect tipo, count(*) as malati
from assenza
group by tipo;
