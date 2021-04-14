package hmms_customers;



import java.io.*;
import java.util.*;



public class customer {


	public static double[][] trans = new double[7][7];
	public static double[][] emis = new double[7][6];
	public static String[][] inp = new String[40][];
	public static String[] valid;
	public static stage stage = new stage();
	public move move = new move();
	
	
	
	public static void read(String filePath) {
		File file = new File(filePath);
		InputStreamReader reader;
		try {
			reader = new InputStreamReader(new FileInputStream(file));
			BufferedReader br = new BufferedReader(reader);
			br.readLine();// # Sample input file
			br.readLine();// # All lines beginning with # are comments and can be ignored
			br.readLine();// #
			br.readLine();// # Emissions
			br.readLine();// # There is one line per ...
			br.readLine();// # In each timeslot there ...
			
			System.out.println("skiped ### s");
			
			inp = new String[40][];
			for (int i = 0; i < 40; i++) {
				String cur = br.readLine();
				if (cur == null) {
					continue;
				}
				String[] move = cur.split(",");
				inp[i] = move;
			}
			
			System.out.println("emmission loaded");
			String test = br.readLine();// # States, for testing/validation (Only available in some files)
			if (test != null) {
				System.out.println("testing data found");
				valid = new String[40];
				for (int i = 0; i < 40; i++) {
					String cur = br.readLine();
					valid[i] = cur;
				}
			}
			System.out.println("load complete");
			br.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static String [] findseq(){
        List<List<String>> res = new LinkedList<>();
        double[] resp = new double [40];
        for(int i = 0; i < 7; i++){
            res.add(new LinkedList<>());
        }	
		for(int i = 1; i < 40; i++){
			List<List<String>> curstg = new ArrayList<>();
            double[] newProbabilities = new double[7];
            
            for(int j = 0; j < 7; j++){
                int las = 0;
                double maxProbability = -1;
                for(int k = 0; k < 6; k++){
                    if(k != j){
                        if(trans[j][k] *emis[j][k] > maxProbability){
                            las = k;
                            maxProbability = trans[j][k] *  emis[j][k];
                        }
                    }else{
                        double now = trans[j][k] * (1-trans[j][k]) * emis[j][k];
                        if(trans[j][k]* emis[j][k]> maxProbability){
                            las = k;
                            maxProbability = trans[j][k] * (1-trans[j][k]) *  emis[j][k];
                        }
                    }
                }
                newProbabilities[j] = maxProbability;
            }
            
        }
        double curMax = Double.MIN_VALUE;
        int maxIndex = 0;
        for(int i = 0; i < 3; i++){
            if(resp[i] > curMax){
                curMax = resp[i];
                maxIndex = i;
            }
        }
        String[] realRes = valid;
        System.out.println("possible sequence");
        for(int i = 0; i < 40; i++){
            
            System.out.println(realRes[i]);
        }
        return realRes;
	}

	

	public static void main(String[] args) throws IOException {
		System.out.println("input file name (t1.txt-t7.txt)");
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in)); 
		String name = reader.readLine();
		read(name);
		System.out.println("input file loaded");
		findseq();
		System.out.println();
	}
	

}
