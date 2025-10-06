--1. Quanti sono gli strutturati di ogni fascia?
select posizione, count(*) as num from persona group by posizione;

--2. Quanti sono gli strutturati con stipendio ≥ 40000?
select count(*) as num from persona where stipendio >= 40000;

--3. Quanti sono i progetti già finiti che superano il budget di 50000?
select count(*) from progetto where budget >= 50000 and fine <= current_date;

--4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto ‘Pegasus’?
select