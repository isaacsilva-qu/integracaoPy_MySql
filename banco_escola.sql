Create Database escola;
Use escola;
Drop Table alunos;
Create Table alunos (
	matricula int not null unique,
    nome varchar(150) not null,
    idade int not null,
    curso varchar(100) not null,
    nota float default 0 
);



select * from alunos;