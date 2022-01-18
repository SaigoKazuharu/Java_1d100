import java.util.Scanner;
class Main{
	public static void main(String[] args) throws Exception{

		while(true){
			System.out.println("1d100のダイスロール");
			int val = (int) (Math.random() * 100)+ 1;

			if(val >= 95){
				System.out.println(val+"　致命的失敗\n");
			}
			
			else if(val <= 5){
				System.out.println(val+"　決定的成功\n");
			}
			
			else{
				System.out.println(val+"\n");
			}

			Scanner scanner = new Scanner(System.in);
			System.out.println("やめるときはnを入力してください。");
			String key = scanner.next();
			
			if(key.equals("n"))
			break;
		}
	}
}