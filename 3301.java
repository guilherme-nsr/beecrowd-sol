import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static String getSobrinhoMeio(int h, int z, int l) {
    if ((h > z && h < l) || (h < z && h > l)) {
      return "huguinho";
    }

    if ((z > h && z < l) || (z < h && z > l)) {
      return "zezinho";
    }

    return "luisinho";
  }

  public static void main(String[] args) throws IOException {
    InputStreamReader ir = new InputStreamReader(System.in);
    BufferedReader in = new BufferedReader(ir);

    String entrada = in.readLine();

    String[] hzl = entrada.split(" ");
    int h = Integer.parseInt(hzl[0]);
    int z = Integer.parseInt(hzl[1]);
    int l = Integer.parseInt(hzl[2]);

    System.out.println(getSobrinhoMeio(h, z, l));
  }
}