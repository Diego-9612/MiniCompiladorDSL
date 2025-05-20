
            load "datos.csv";
            filter column "precio_noche" > 300;
            filter column "tipo_habitacion" == "suite";
            aggregate COUNT column "id_reserva";
            print;
        