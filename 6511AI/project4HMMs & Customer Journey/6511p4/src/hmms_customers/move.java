package hmms_customers;



import java.util.ArrayList;
import java.util.List;

public class move {
	public static String DEMO = "DEMO";
	public static String VIDEO = "VIDEO";
	public static String TESTIMONIAL = "TESTIMONIAL";
	public static String PRICING = "PRICING";
	public static String BLOG = "BLOG";
	public static String PAYMENT = "PAYMENT";
	public static List<String> moves = new ArrayList<>();

	public move() {
		moves.add(DEMO);
		moves.add(VIDEO);
		moves.add(TESTIMONIAL);
		moves.add(PRICING);
		moves.add(BLOG);
		moves.add(PAYMENT);

		addemis(stage.ZERO, DEMO, 0.1);
		addemis(stage.ZERO, VIDEO, 0.01);
		addemis(stage.ZERO, TESTIMONIAL, 0.05);
		addemis(stage.ZERO, PRICING, 0.3);
		addemis(stage.ZERO, BLOG, 0.5);

		addemis(stage.AWARE, DEMO, 0.1);
		addemis(stage.AWARE, VIDEO, 0.01);
		addemis(stage.AWARE, TESTIMONIAL, 0.15);
		addemis(stage.AWARE, PRICING, 0.3);
		addemis(stage.AWARE, BLOG, 0.4);

		addemis(stage.CONSIDERING, DEMO, 0.2);
		addemis(stage.CONSIDERING, VIDEO, 0.3);
		addemis(stage.CONSIDERING, TESTIMONIAL, 0.05);
		addemis(stage.CONSIDERING, PRICING, 0.4);
		addemis(stage.CONSIDERING, BLOG, 0.4);

		addemis(stage.EXPERIENCING, DEMO, 0.4);
		addemis(stage.EXPERIENCING, VIDEO, 0.6);
		addemis(stage.EXPERIENCING, TESTIMONIAL, 0.05);
		addemis(stage.EXPERIENCING, PRICING, 0.3);
		addemis(stage.EXPERIENCING, BLOG, 0.4);

		addemis(stage.READY, DEMO, 0.05);
		addemis(stage.READY, VIDEO, 0.75);
		addemis(stage.READY, TESTIMONIAL, 0.35);
		addemis(stage.READY, PRICING, 0.2);
		addemis(stage.READY, BLOG, 0.4);

		addemis(stage.LOST, DEMO, 0.01);
		addemis(stage.LOST, VIDEO, 0.01);
		addemis(stage.LOST, TESTIMONIAL, 0.03);
		addemis(stage.LOST, PRICING, 0.05);
		addemis(stage.LOST, BLOG, 0.2);

		addemis(stage.SATISFIED, DEMO, 0.4);
		addemis(stage.SATISFIED, VIDEO, 0.4);
		addemis(stage.SATISFIED, TESTIMONIAL, 0.01);
		addemis(stage.SATISFIED, PRICING, 0.05);
		addemis(stage.SATISFIED, BLOG, 0.5);
		addemis(stage.SATISFIED, PAYMENT, 1);

	}

	public void addemis(String at, String next, double prob) {
		customer.emis[stage.stages.indexOf(at)][moves.indexOf(next)] = prob;
	}


}
