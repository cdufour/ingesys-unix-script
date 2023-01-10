public class App
{
    public static void main(String[] args) {
 
        String lower_chars = "abcdefghijklmnopqrstuvwxyz";
        String upper_chars = lower_chars.toUpperCase();
        int[] digits = {0,1,2,3,4,5,6,7,8,9};
        String pass = "";
        int pass_len = 10; // longueur de mot de passe par défaut
        Helper helper = new Helper();

        // check les args de ligne de commande
        if (args.length == 2 && args[0].equals("-l")) {
            pass_len = Integer.parseInt(args[1]);  
        }

        for (int i=0; i<pass_len; i++) {
     
            if (i % 3 == 0) {
                pass += upper_chars.charAt(helper.getRandInt(0, upper_chars.length() - 1));
            } else if (i % 3 == 1) {
                pass += lower_chars.charAt(helper.getRandInt(0, lower_chars.length() - 1));
            } else {
                pass += digits[helper.getRandInt(0, digits.length - 1)];
            }
        }

        // affichage du mot de passe
        System.out.print(pass);
    }
}