# Comandos de la prática 02
## Nombre del equipo
### Integrante 1: Jennifer Erzsebet Olvera Martínez 
### Integrante 2:
### Integrante 3:
### Integrante 4:

# Parte I. 

**Respuesta 1:**

Plataforma/compañía | Longitud de reads (pb) | # reads x run | Tiempo | Costo x 10^6 bases | Error (%) | Química |
--- | --- | --- | --- | --- | --- | --- |
Primera generación | | | | | | |
Sanger/Life Technologies | 800 | 1 | 2 hrs | 2400 | 0.3 | Dideoxy terminator | 
Segunda generación | | | | | | |
Pirosecuenciación (SBS)/454 Life Sciences-Roche | 700 | 1×10^6 | 24-48 hrs | 10 | 1 | Pirosecuenciación |
HiSeq/Illumina | 2x150 | 5x10^9 | 27/240 hrs | 0.1 | 0.8 | Secuenciación por síntesis |
SOLiD/Life Technologies | 50 | 1x10^9 | 14 días | 0.3 | 0.01 | Secuenciación por ligadura de oligonucleótidos |
Ion PGM/Life Technologies | 200 | 5x10^6 | 2-5 hrs | 1 | 1.7 | Secuenciación por la detección de protones liberados por el proceso de polimerización del ADN | 
Tercera generación | | | | | | |
Nanoporos (MinION)/Oxford Nanopores Technologies | >5000 | 6x10^4 | 48/72 hrs | <1 | 34 | Secuenciación de moléculas individuales en tiempo real |


Referencias:
[1] Kulski, J. (2016). Next-Generation Sequencing — An Overview of the History, Tools, and “Omic” Applications. Next Generation Sequencing–Advances, Applications and Challenges, 3-60. https://www.intechopen.com/books/next-generation-sequencing-advances-applications-and-challenges/next-generation-sequencing-an-overview-of-the-history-tools-and-omic-applications

# Parte II.

**Respuesta 1:**

Las secuencias están en la sección Associated Data >> Data Availability Statement >>  http://www.ebi.ac.uk/ena/data/view/PRJEB5172

Descomprimir:

unzip ERR486828.fastq.zp 

gunzip ERR486828_1.fastq.gz

gunzip ERR486828_2.fastq.gz

Convertir archivo...


zcat ERR486828_1.fastq | echo $((`wc -l`/4))

410959

zcat ERR486828_2.fastq | echo $((`wc -l`/4))

410959


# Parte III.

# Parte IV. 
