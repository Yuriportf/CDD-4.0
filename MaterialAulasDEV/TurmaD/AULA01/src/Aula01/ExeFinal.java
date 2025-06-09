package Aula01;
import java.util.Scanner;

public class ExeFinal {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um número: ");
		double resp = entrada.nextDouble();
		System.out.println(resp);
		
		if (resp > 0){
			System.out.println("positivo");
		}else {
			System.out.println("negativo");
			
		}

	}

}
