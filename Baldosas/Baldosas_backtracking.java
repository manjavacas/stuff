
import java.util.Arrays;
import Utilidades.*;

public class Baldosas_backtracking {

	/* Variables de clase */
	static int[][] mejorSolucion = null;
	static int mejorNumBaldosas = Integer.MAX_VALUE;

	public static void main(String[] args) {

		/* Variables */
		int[][] solar;
		int[] baldosas;

		/* Obtener datos */
		solar = generarSolar();
		baldosas = generarBaldosas();

		/* Ordenar las baldosas a utilizar */
		ordenarBaldosas(baldosas);

		System.out.println("Solar de dimensiones " + solar.length + " x " + solar.length + ":\n"
				+ MatricesOperaciones.mostrar(solar) + "\n");
		System.out.println(
				"Solar cubierto utilizando baldosas de lado:\n" + MatricesOperaciones.mostrar(baldosas) + "\n");

		/* Aplicar algoritmo backtracking para la distribucion de baldosas */
		mejorSolucion = new int[solar.length][solar.length];

		long inicio = System.nanoTime();
		colocarBaldosas(solar, baldosas);
		long fin = System.nanoTime();
		System.out.println("Ejecutado en " + (fin - inicio) + " ns.");

		/* Mostrar la distribucion obtenida */
		mostrarResultado();
	}

	/* Crear matriz bidimensional que represente el solar */
	static int[][] generarSolar() {

		int lado;
		int[][] solar;

		lado = leer.entero("Introducir metros de lado del solar: ");
		solar = new int[lado][lado];

		return solar;
	}

	/* Generar vector con los diferentes tipos de baldosas */
	static int[] generarBaldosas() {

		int n_tipos;
		int[] baldosas;

		n_tipos = leer.entero("Introducir número de tipos de baldosa: ");
		baldosas = new int[n_tipos];

		/* Lectura de dimensiones */
		for (int i = 0; i < n_tipos; i++) {
			baldosas[i] = leer.entero("Introducir lado de la baldosa " + (i + 1));
		}

		return baldosas;
	}

	/* Aplicar algoritmo de ordenacion sobre matriz */
	static void ordenarBaldosas(int[] baldosas) {
		Arrays.sort(baldosas);
	}

	/* Copiar matriz origen en matriz destino */
	private static void copiarMejorSolucion(int[][] solar) {
		for (int i = 0; i < solar.length; i++)
			for (int j = 0; j < solar[i].length; j++)
				mejorSolucion[i][j] = solar[i][j];
	}

	/* Mostrar solar con la distribucion de baldosas final */
	static void mostrarResultado() {
		System.out.println("Resultado:\n" + MatricesOperaciones.mostrar(mejorSolucion) + "\nSe han colocado "
				+ mejorNumBaldosas + " baldosas.");
	}

	/* Invocar al algoritmo de colocacion de baldosas */
	static void colocarBaldosas(int[][] solar, int[] baldosas) {
		colocarBaldosas(solar, baldosas, 0, 0);
	}

	/* Aplicar algoritmo de backtracking para cubrir el solar */
	private static void colocarBaldosas(int[][] solar, int[] baldosas, int n_baldosa, int colocadas) {

		int[] posicion;
		int fila, columna;

		/* Se obtiene la primera posicion libre */
		posicion = encontrarLibre(solar);
		fila = posicion[0];
		columna = posicion[1];

		/* Se comprueba si el solar se ha cubierto completamente */
		if (fila == -1 || columna == -1) {
			if (colocadas < mejorNumBaldosas) {
				/* Obtener mejor solucion */
				copiarMejorSolucion(solar);
				mejorNumBaldosas = colocadas;
				System.out.println(MatricesOperaciones.mostrar(mejorSolucion));
			}
		} else {
			for (int i = 0; i < baldosas.length; i++) {
				/* Se recorre el solar evaluando los huecos disponibles */
				if (comprobarHuecos(baldosas[i], solar, fila, columna)) {
					/* Rellenar huecos */
					actualizarHuecos(baldosas[i], solar, fila, columna, n_baldosa % 9);
					colocarBaldosas(solar, baldosas, (n_baldosa + 1) % 9, colocadas + 1);
					/* Deshacer cambios */
					actualizarHuecos(baldosas[i], solar, fila, columna, 0);
				}
			}
		}

	}

	/* Comprobar si una baldosa puede introducirse en una posicion dada */
	private static boolean comprobarHuecos(int lado, int[][] solar, int fila, int columna) {

		boolean disponible = true;

		if (fila + lado > solar.length || columna + lado > solar.length) {
			disponible = false;
		} else {
			for (int i = fila; i < fila + lado && disponible; i++) {
				for (int j = columna; j < columna + lado && disponible; j++) {
					/* Comprobar si se exceden los limites del solar o si el hueco esta ocupado */
					if (solar[i][j] != 0) {
						disponible = false;
					}
				}
			}
		}

		return disponible;
	}

	/* Actualizar baldosas en el solar */
	private static void actualizarHuecos(int lado, int[][] solar, int fila, int columna, int n_baldosa) {
		for (int i = 0; i < lado; i++) {
			for (int j = 0; j < lado; j++) {
				solar[fila + i][columna + j] = n_baldosa;
			}
		}
	}


	/* Encontrar la primera posicion libre disponible en el solar */
	private static int[] encontrarLibre(int[][] solar) {

		int[] posicion = new int[2];
		boolean seguir = true;

		posicion[0] = -1;
		posicion[1] = -1;

		for (int i = 0; i < solar.length && seguir; i++) {
			for (int j = 0; j < solar[i].length && seguir; j++) {
				if (solar[i][j] == 0) {
					posicion[0] = i;
					posicion[1] = j;
					seguir = false;
				}
			}
		}

		return posicion;
	}
}
