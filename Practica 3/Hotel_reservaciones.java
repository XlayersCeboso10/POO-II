import java.util.Scanner;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;

enum Tipo_de_habitacion { INDIVIDUAL, DOBLE, SUITE }

public class Hotel_reservaciones {
    
    private int Numero_habitacion;
    private Tipo_de_habitacion Tipo_habitacion;
    private LocalDate Fecha_ingreso, Fecha_salida;
    private String cliente;

    public Hotel_reservaciones() {
        System.out.print("\033[H\033[2J");
        Scanner Sebas = new Scanner(System.in);
        DateTimeFormatter formato = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        System.out.print("Número de habitación: "); Numero_habitacion = Sebas.nextInt();
        System.out.print("Tipo de habitación (INDIVIDUAL, DOBLE, SUITE): ");
        Tipo_habitacion = Tipo_de_habitacion.valueOf(Sebas.next().toUpperCase());
        Sebas.nextLine(); System.out.print("Fecha de ingreso (YYYY-MM-DD): ");
        Fecha_ingreso = LocalDate.parse(Sebas.nextLine(), formato);
        System.out.print("Fecha de salida (YYYY-MM-DD): "); Fecha_salida = LocalDate.parse(Sebas.nextLine(), formato);
        System.out.print("Nombre del cliente: "); cliente = Sebas.nextLine();
        Sebas.close();
    }

    public long Calcular_dias() {
        return ChronoUnit.DAYS.between(Fecha_ingreso, Fecha_salida);
    }

    public void Mostrar_Info() {
        System.out.println("\n------------- Este es el ticket de la venta -------------");
        System.out.println("Nombre del cliente: " + cliente);
        System.out.println("Número de habitación: " + Numero_habitacion);
        System.out.println("Tipo de habitación: " + Tipo_habitacion);
        System.out.println("Fecha de ingreso: " + Fecha_ingreso);
        System.out.println("Fecha de salida: " + Fecha_salida);
        System.out.println("Total de días en el hotel: " + Calcular_dias());
    }

    public static void main(String[] args) {
        Hotel_reservaciones reserva = new Hotel_reservaciones();
        reserva.Mostrar_Info();
    }
}
