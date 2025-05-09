load "datos.csv";
filter column "precio_noche" BETWEEN 100 AND 200;
aggregate SUM column "precio_noche" where "estado_reserva" == "confirmada";
print;