package hmms_customers;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class stage {
	public static String ZERO = "ZERO";
	public static String AWARE = "AWARE";
	public static String CONSIDERING = "CONSIDERING";
	public static String EXPERIENCING = "EXPERIENCING";
	public static String READY = "READY";
	public static String SATISFIED = "SATISFIED";
	public static String LOST = "LOST";
	public static List<String> stages = new ArrayList<>();
	public static Map<String, Map<String, Double>> edges = new HashMap<>();
	public String current;
	
	public stage() {
		stages.add(ZERO);
		stages.add(AWARE);
		stages.add(CONSIDERING);
		stages.add(EXPERIENCING);
		stages.add(READY);
		stages.add(SATISFIED);
		stages.add(LOST);
		
		edges.put(ZERO, new HashMap<>());
		edges.put(AWARE, new HashMap<>());
		edges.put(CONSIDERING, new HashMap<>());
		edges.put(EXPERIENCING, new HashMap<>());
		edges.put(READY, new HashMap<>());
		edges.put(SATISFIED, new HashMap<>());
		edges.put(LOST, new HashMap<>());
		
		current = ZERO;
		
		addtrans(ZERO, AWARE, 0.4);
		addtrans(AWARE, CONSIDERING, 0.3);
		addtrans(AWARE, READY, 0.01);
		addtrans(AWARE, LOST, 0.2);
		addtrans(CONSIDERING, EXPERIENCING, 0.2);
		addtrans(CONSIDERING, READY, 0.02);
		addtrans(CONSIDERING, LOST, 0.3);
		addtrans(EXPERIENCING, READY, 0.3);
		addtrans(EXPERIENCING, LOST, 0.3);
		addtrans(READY, LOST, 0.2);
		
	}
	public  void addtrans(String now, String next, double prob) {
		customer.trans[stages.indexOf(now)][stages.indexOf(next)] = prob;
		edges.get(now).put(next, prob);
		
	}
	

	
	
}
