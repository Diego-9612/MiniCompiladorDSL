load "datos.csv";
aggregate COUNT column "id_reserva" where "metodo_pago" == "tarjeta";
aggregate AVERAGE column "precio_noche" where "tipo_habitacion" == "suite";
print;