package ed2.projeto.algoritmosordenacao;

import java.util.Arrays;
import java.util.Scanner;

public class main {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        int[] vetorOriginal = { 9, 4, 6, 2, 7, 1, 8, 3, 5 };

        System.out.println("===== ALGORITMOS DE ORDENACAO =====");
        System.out.println("1 - Bubble Sort");
        System.out.println("2 - Selection Sort");
        System.out.println("3 - Insertion Sort");
        System.out.println("4 - Quick Sort");
        System.out.print("Escolha uma opcao: ");

        int opcao = entrada.nextInt();

        IAlgoritmoOrdenacao algoritmo = null;

        switch(opcao) {
            case 1:
                algoritmo = new BubbleSort();
                break;
            case 2:
                algoritmo = new SelectionSort();
                break;
            case 3:
                algoritmo = new InsertionSort();
                break;
            case 4:
                algoritmo = new QuickSort();
                break;
            default:
                System.out.println("Opcao invalida!");
                System.exit(0);
        }

        int[] vetorParaOrdenar = Arrays.copyOf(vetorOriginal, vetorOriginal.length);

        System.out.println("\nAlgoritmo escolhido: " + algoritmo.toString());
        System.out.println("Vetor original: " + Arrays.toString(vetorOriginal));

        algoritmo.ordenarVetor(vetorParaOrdenar);

        System.out.println("Vetor ordenado: " + Arrays.toString(vetorParaOrdenar));

        entrada.close();
    }

}