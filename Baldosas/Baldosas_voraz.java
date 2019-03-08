package p3;

import java.util.Arrays;
import Utilidades.*;

/* @author Antonio.Manjavacas */

public class Baldosas_voraz {

	public static void main(String[] args) {

		/* Variables */
		int[][] solar;
		int[] baldosas;
		int colocadas;
		
		/* Obtener datos */
		solar = generarSolar();
		baldosas = generarBaldosas();

		/* Ordenar las baldosas a utilizar */
		ordenarBaldosas(baldosas);

		System.out.println("Solar de dimensiones " + solar.length + " x " + solar.length + ":\n"
				+ MatricesOperaciones.mostrar(solar) + "\n");
		System.out.println("Solar cubierto utilizando baldosas de lado:\n" 
				+ MatricesOperaciones.mostrar(baldosas) + "\n");

		/* Aplicar algoritmo voraz para la distribucion de baldosas */
		long inicio = System.nanoTime();
		colocadas = colocarBaldosas(solar, baldosas);
		long fin = System.nanoTime();
		System.out.println("Ejecutado en " + (fin - inicio) + " ns.");
		
		/* Mostrar la distribucion obtenida */
		mostrarResultado(solar, colocadas);
	}

	/* Crear matriz bidimensional que represente el solar */
	static int[][] generarSolar() {

		int lado;
		int[][] solar;

		lado = leer.entero("Introducir metros de lado del solar: ");
		solar = new int[lado][lado];

		/* Inicializar matriz */
		for (int i = 0; i < solar.length; i++) {
			for (int j = 0; j < solar[i].length; j++) {
				solar[i][j] = 0;
			}
		}

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

	/* Mostrar solar con la distribucion de baldosas final */
	static void mostrarResultado(int[][] solar, int colocadas) {
		System.out.println("Resultado:\n" + MatricesOperaciones.mostrar(solar) + "\nSe han colocado " + colocadas + " baldosas.");		
	}

	/* Aplicacion de algoritmo voraz para distribuir las baldosas en el solar */
	static int colocarBaldosas(int[][] solar, int[] baldosas) {

		int lado, colocadas = 0, n_baldosa = 0, huecos = solar.length * solar.length;

		for (int i = baldosas.length - 1; i >= 0; i--) {
			lado = baldosas[i];
			/* Se comprueba si hay huecos disponibles para la baldosa dada */
			if (lado * lado <= huecos) {
				/* Se recorre el solar evaluando los huecos disponibles */
				for (int j = 0; j < solar.length; j++) {
					for (int k = 0; k < solar[j].length; k++) {
						if (comprobarHuecos(baldosas[i], solar, j, k)) {
							/* Ajustar identificador de baldosa entre 1 y 9 */
							n_baldosa = (n_baldosa < 9) ? ++n_baldosa : 1;
							/* Rellenar huecos */
							huecos -= rellenarHuecos(baldosas[i], solar, j, k, n_baldosa);
							colocadas++;
						}
					}
				}
			}
		}
		
		return colocadas;

	}

	/* Comprobar si una baldosa puede introducirse en una posicion dada */
	private static boolean comprobarHuecos(int lado, int[][] solar, int fila, int columna) {

		boolean disponible = true;

		for (int i = 0; i < lado & disponible; i++) {
			for (int j = 0; j < lado & disponible; j++) {
				/* Comprobar si se exceden los limites del solar o si el hueco esta ocupado */
				if (fila + i >= solar.length || columna + j >= solar.length || solar[fila + i][columna + j] != 0) {
					disponible = false;
				}
			}
		}

		return disponible;
	}

	/* Representar baldosas en el solar */
	private static int rellenarHuecos(int lado, int[][] solar, int fila, int columna, int n_baldosa) {

		int huecos = 0;

		for (int i = 0; i < lado; i++) {
			for (int j = 0; j < lado; j++) {
				solar[fila + i][columna + j] = n_baldosa;
				huecos++;
			}
		}

		/* Se devuelven los huecos que han sido ocupados */
		return huecos;
	}

}
