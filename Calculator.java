import java.awt.Color; 
import java.awt.Font;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class Taschenrechner {

	public static JButton komma,plusbtn, minbtn, malbtn, getbtn, gleichbtn, clearbtn, hoch2btn, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn0, prozbtn, backbtn, wurzelbtn;
	public static JTextField Eingabe;
	public static JFrame gui;
	public static JPanel mp;
	public static Font font = new Font("Arial", Font.PLAIN, 30);
	public static Font EingabeFont = new Font("Arial", Font.LAYOUT_RIGHT_TO_LEFT, 30);
	public static Image backbtnimg;
	public static JButton[]btn123 = new JButton[3];
	public static JButton[]btn456 = new JButton[3];
	public static JButton[]btn789 = new JButton[3];
	public static JLabel Eingegebenes;
	public static int i, gesEingInt;
	public static double gesEing2DoubleI;
	public static long gesEingD;
	public static double gesEing2Double, gesEing2IntD;
	public static double  gesEingI;
	public static int gesEing2Int;
	public static String operator, gesEing2, gesEing, s;
	
	
	public static void main(String [] args) {
		
		gui = new JFrame("Rechner");
		gui.setLocationRelativeTo(null);
		gui.setSize(305+2, 525+2);
		gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		gui.setVisible(true);
		gui.setLayout(null);
		gui.setResizable(false);
		
		mp = new JPanel();
		mp.setBounds(0,0,305,525);
		mp.setBackground(new Color(220,220,220));
		mp.setVisible(true);
		mp.setLayout(null);
		gui.add(mp);
		
		Eingegebenes = new JLabel();
		Eingegebenes.setBounds(7,7,278,33);
		Eingegebenes.setBackground(new Color(220,220,220));
		Eingegebenes.setFont(EingabeFont);
		Eingegebenes.setVisible(true);
		mp.add(Eingegebenes);
		
		Eingabe = new JTextField();
		Eingabe.setBounds(7, 47, 278, 75);
		Eingabe.setFont(EingabeFont);
		Eingabe.setBackground(new Color(220,220,220));
		Eingabe.setVisible(true);
		/* Eingabe.getDocument().addDocumentListener(new DocumentListener(){
			
			@Override
			public void insertUpdate(DocumentEvent arg0) {
				if(Eingabe.getText().length() > 15) {
					String l2 = Eingabe.getText();
					Eingabe.setText(l2.substring(0,Eingabe.getText().length()-1));
				}
			}

			@Override
			public void changedUpdate(DocumentEvent arg0) {
				if(Eingabe.getText().length() > 15) {
					String l2 = Eingabe.getText();
					Eingabe.setText(l2.substring(0,15));
				}				
			}

			@Override
			public void removeUpdate(DocumentEvent arg0) {
				if(Eingabe.getText().length() > 15) {
					String l2 = Eingabe.getText();
					Eingabe.setText(l2.substring(0,15));
				}				
			}
		});		*/
		mp.add(Eingabe);
		
		
		clearbtn = new JButton("C");
		clearbtn.setBounds(7, 129, 139, 53);
		clearbtn.setFont(font);
		clearbtn.setBackground(new Color(195,195,195));
		clearbtn.setVisible(true);
		clearbtn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Eingabe.setText(null);
				operator = null;
				Eingegebenes.setText(null);
				gesEingInt = 0;
				gesEing2Int = 0;
				gesEing = null;
				gesEing2 = null;
				
				
			}
		});
		mp.add(clearbtn);
		
		
		
		komma = new JButton(",");
		komma.setBounds(7,429,67,53);
		komma.setFont(font);
		komma.setVisible(true);
		komma.setBackground(new Color(220,220,220));
		komma.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				try {
					if((Eingabe.getText().indexOf(".")<0)) {
						if(!Eingabe.getText().equals("")&&!Eingabe.getText().equals("-")) {
				String ei = Eingabe.getText();
				String ne = ei + ".";
				Eingabe.setText(ne);
					}}
}catch(NumberFormatException e1) {
					
				}
				
			}
		});
		mp.add(komma);
		
		backbtn = new JButton("<--");
	  	backbtn.setBounds(150, 129, 135,53);
		backbtn.setFont(font);
		backbtn.setVisible(true);
		backbtn.setBackground(new Color(195,195,195));
		backbtn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				try{String b = Eingabe.getText();
				int l = Eingabe.getText().length();
				Eingabe.setText(b.substring(0,l-1));
}catch(NumberFormatException e1){
					
				}catch(StringIndexOutOfBoundsException e2) {
					
				}
			}
		});
		mp.add(backbtn);
		
		hoch2btn = new JButton("x^");
		hoch2btn.setBounds(7,189, 67, 53);
		hoch2btn.setFont(font);
		hoch2btn.setVisible(true);
		hoch2btn.setBackground(new Color(205,205,205));
		hoch2btn.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
				try {
				gesEing = Eingabe.getText();
				if(Eingabe.getText().indexOf(".") >= 0 ) {
					gesEingI = Double.parseDouble(gesEing);}
					else if(Eingabe.getText().indexOf(".") < 0)  {
						gesEingD = Long.parseLong(gesEing);
					}
				Eingabe.setText("");
				Eingegebenes.setText(gesEing);
				operator = "**";
}catch(NumberFormatException e1) {
					
				}
				
			}
		});
		mp.add(hoch2btn);
		
		prozbtn = new JButton("R");
		prozbtn.setBounds(78, 189, 67, 53);
		prozbtn.setFont(font);
		prozbtn.setBackground(new Color(205,205,205));
		prozbtn.setVisible(true);
		prozbtn.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
try {
				gesEing = Eingabe.getText();
				if(Eingabe.getText().indexOf(".") >= 0 ) {
					gesEingI = Double.parseDouble(gesEing);}
					else if(Eingabe.getText().indexOf(".") < 0)  {
						gesEingD = Long.parseLong(gesEing);
					}
				Eingabe.setText("");
				Eingegebenes.setText(gesEing);
				operator = "%";
}catch(NumberFormatException e1) {
	
}
				
			}
		});
		mp.add(prozbtn);
		
		getbtn = new JButton("/");
		getbtn.setBounds(219,189,67,53);
		getbtn.setBackground(new Color(215,215,215));
		getbtn.setVisible(true);
		getbtn.setFont(font);
		getbtn.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
				try {
				gesEing = Eingabe.getText();
				if(Eingabe.getText().indexOf(".") >= 0 ) {
					gesEingI = Double.parseDouble(gesEing);}
					else if(Eingabe.getText().indexOf(".") < 0)  {
						gesEingD = Long.parseLong(gesEing);
					}
				Eingabe.setText("");
				Eingegebenes.setText(gesEing);
				operator = "/";
}catch(NumberFormatException e1) {
					
				}
				
			}
		});
		mp.add(getbtn);
		
		wurzelbtn = new JButton("W");
		wurzelbtn.setBounds(149,189,66,53);
		wurzelbtn.setBackground(new Color(205,205,205));
		wurzelbtn.setVisible(true);
		wurzelbtn.setFont(font);
		wurzelbtn.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
				try {
				gesEing = Eingabe.getText();
				if(Eingabe.getText().indexOf(".") >= 0 ) {
					gesEingI = Double.parseDouble(gesEing);
					s = (String.valueOf(Math.sqrt(gesEingI)));
					Eingegebenes.setText(String.valueOf(gesEingI));}
					else if(Eingabe.getText().indexOf(".") < 0) {
						gesEingD = Long.parseLong(gesEing);
						s = (String.valueOf(Math.sqrt(gesEingD)));
						Eingegebenes.setText(String.valueOf(gesEingD));
					}				
				
				Eingabe.setText(s.substring(0,s.length()-2));
				}catch(NumberFormatException e1) {
					
				}
				
				
				
			}
		});
		mp.add(wurzelbtn);
		
		for(i = 0; i<btn789.length;i++) {
			btn789[i]= new JButton();
			
				btn789[i].setBounds(7+(4*i)+(i*67), 249,67,53);
				String btnname = String.valueOf(i+7);
				btn789[i].setText(btnname);
				
			
			btn789[i].setFont(font);
			btn789[i].setBackground(new Color(232,232,232));
			btn789[i].setVisible(true);
			
			
			
			
			
			mp.add(btn789[i]);
		}
		
		btn789[0].addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				String EingabeText = Eingabe.getText() + "7";
				Eingabe.setText(EingabeText);
				
				
			}
		});
		btn789[1].addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				String EingabeText = Eingabe.getText() + "8";
				Eingabe.setText(EingabeText);
				
				
			}
		});
		btn789[2].addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				String EingabeText = Eingabe.getText() + "9";
				Eingabe.setText(EingabeText);
				
				
			}
		});
		
		
		
		for(int i = 0; i<btn456.length;i++) {
			btn456[i]= new JButton();
			
				btn456[i].setBounds(7+(4*i)+(i*67), 309,67,53);
				String btnname = String.valueOf(i+4);
				btn456[i].setText(btnname);
				
			
			btn456[i].setFont(font);
			btn456[i].setBackground(new Color(232,232,232));
			btn456[i].setVisible(true);
			
			mp.add(btn456[i]);
		}
		btn456[2].addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				String EingabeText = Eingabe.getText() + "6";
				Eingabe.setText(EingabeText);
				
				
			}
		});
		btn456[1].addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				String EingabeText = Eingabe.getText() + "5";
				Eingabe.setText(EingabeText);
				
				
			}
		});
		btn456[0].addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				String EingabeText = Eingabe.getText() + "4";
				Eingabe.setText(EingabeText);
				
				
				
				
				
			}
		});


		for(int i=0; i<btn123.length; i++) {
			btn123[i] = new JButton();
			btn123[i].setBounds(7+(4*i)+(i*67),369,67, 53 );
			btn123[i].setFont(font);
			btn123[i].setBackground(new Color( 232,232,232));
			btn123[i].setVisible(true);
			String btnname = String.valueOf(i+1);
			btn123[i].setText(btnname);
			mp.add(btn123[i]);
		}
		btn123[0].addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				String EingabeText = Eingabe.getText() + "1";
				Eingabe.setText(EingabeText);
				
			}
		});
		btn123[1].addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				String EingabeText = Eingabe.getText() + "2";
				Eingabe.setText(EingabeText);
				
				
			}
		});
		btn123[2].addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				String EingabeText = Eingabe.getText() + "3";
				Eingabe.setText(EingabeText);
				
				
			}
		});

		
		
		malbtn = new JButton("x");
		malbtn.setBounds(219, 249, 66,53);
		malbtn.setFont(font);
		malbtn.setBackground(new Color(215,215,215));
		malbtn.setVisible(true);
		malbtn.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
				try {
				gesEing = Eingabe.getText();
				if(Eingabe.getText().indexOf(".") >= 0 ) {
					gesEingI = Double.parseDouble(gesEing);}
					else if(Eingabe.getText().indexOf(".") < 0)  {
						gesEingD = Long.parseLong(gesEing);
					}
				Eingabe.setText("");
				Eingegebenes.setText(gesEing);
				operator = "*";
				
}catch(NumberFormatException e1) {
					
				}
			}
		});
		mp.add(malbtn);
		
		plusbtn = new JButton("+");
		plusbtn.setBounds(219, 309, 66, 53);
		plusbtn.setFont(font);
		plusbtn.setBackground(new Color(215,215,215));
		plusbtn.setVisible(true);
		plusbtn.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
				try {
				gesEing = Eingabe.getText();
				if(Eingabe.getText().indexOf(".") >= 0 ) {
					gesEingI = Double.parseDouble(gesEing);}
					else if(Eingabe.getText().indexOf(".") < 0)  {
						gesEingD = Long.parseLong(gesEing);
					}
				Eingabe.setText("");
				Eingegebenes.setText(gesEing);
				operator = "+";
}catch(NumberFormatException e1) {
					
				}
				
			}
		});
		mp.add(plusbtn);
		
		minbtn = new JButton("-");
		minbtn.setBounds(219,369,66,53);
		minbtn.setBackground(new Color(215,215,215));
		minbtn.setFont(font);
		minbtn.setVisible(true);
		minbtn.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
				try {
				if(Eingabe.getText().equals("")) {
					Eingabe.setText("-");
				}
				else {
				gesEing = Eingabe.getText();
				if(Eingabe.getText().indexOf(".") >= 0 ) {
					gesEingI = Double.parseDouble(gesEing);}
					else if(Eingabe.getText().indexOf(".") < 0)  {
						gesEingD = Long.parseLong(gesEing);
					}
				Eingabe.setText("");
				Eingegebenes.setText(gesEing);
				operator = "-";
}}catch(NumberFormatException e1) {
					
				}
				}
			}
		);
		mp.add(minbtn);
		
		gleichbtn = new JButton("=");
		gleichbtn.setBounds(148,429,137,53);
		gleichbtn.setFont(font);
		gleichbtn.setBackground(new Color(210,210,210));
		gleichbtn.setVisible(true);
		gleichbtn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				try{gesEing2 = Eingabe.getText();
				if(Eingabe.getText().indexOf(".") < 0 ) {
				
				if(gesEing.indexOf(".")>=0) {
					gesEing2IntD = Double.parseDouble(gesEing2);
				if(operator.equals("+")) {
					Eingabe.setText(String.valueOf(gesEingI + gesEing2IntD));
				}
				else if(operator.equals("*")) {
					Eingabe.setText(String.valueOf(gesEingI * gesEing2IntD));
				}
				else if(operator.equals("/")) {
					s = String.valueOf(((double)gesEingI / (double)gesEing2IntD));
					if(s.length()>15) {
					Eingabe.setText(s.substring(0,s.length()-3));}
					else {Eingabe.setText(String.valueOf((double)gesEingI/(double)gesEing2IntD));}
				}
				else if(operator.equals("-")) {
					Eingabe.setText(String.valueOf(gesEingI - gesEing2IntD));
				}
				else if(operator.equals("%")) {
					Eingabe.setText(String.valueOf(gesEingI % gesEing2IntD));
				}
				else if(operator.equals("**")) {
					s = (String.valueOf(Math.pow(gesEingI, gesEing2IntD)));
					Eingegebenes.setText(String.valueOf(gesEingD));
					Eingabe.setText(s.substring(0,s.length()-2));
				}}
				else if(gesEing.indexOf(".")<0) {
					gesEing2Int = Integer.parseInt(gesEing2);
					if(operator.equals("+")) {
						Eingabe.setText(String.valueOf(gesEingD + gesEing2Int));
					}
					else if(operator.equals("*")) {
						Eingabe.setText(String.valueOf(gesEingD * gesEing2Int));
					}
					else if(operator.equals("/")) {
						s = String.valueOf(((double)gesEingD / (double)gesEing2Int));
						if(s.length()>15) {
						Eingabe.setText(s.substring(0,s.length()-3));}
						else {Eingabe.setText(String.valueOf((double)gesEingD/(double)gesEing2Int));}
					}
					else if(operator.equals("-")) {
						Eingabe.setText(String.valueOf(gesEingD - gesEing2Int));
					}
					else if(operator.equals("%")) {
						Eingabe.setText(String.valueOf(gesEingD % gesEing2Int));
					}
					else if(operator.equals("**")) {
						s = (String.valueOf(Math.pow(gesEingD, gesEing2Int)));
						Eingegebenes.setText(String.valueOf(gesEingD));
						Eingabe.setText(s.substring(0,s.length()-2));
					}
				}}
				
				else if(Eingabe.getText().indexOf(".") >= 0)  {
					
					if(gesEing.indexOf(".")>=0) {
						gesEing2Double = Double.parseDouble(gesEing2);
					if(operator.equals("+")) {
						Eingabe.setText(String.valueOf(gesEingI + gesEing2Double));
					}
					else if(operator.equals("*")) {
						Eingabe.setText(String.valueOf(gesEingI * gesEing2Double));
					}
					else if(operator.equals("/")) {
						s = String.valueOf(((double)gesEingI / (double)gesEing2Double));
						if(s.length()>15) {
						Eingabe.setText(s.substring(0,s.length()-3));}
						else {Eingabe.setText(String.valueOf((double)gesEingI/(double)gesEing2Double));}
					}
					else if(operator.equals("-")) {
						Eingabe.setText(String.valueOf(gesEingI - gesEing2Double));
					}
					else if(operator.equals("%")) {
						Eingabe.setText(String.valueOf(gesEingI % gesEing2Double));
					}
					else if(operator.equals("**")) {
						s = (String.valueOf(Math.pow(gesEingI, gesEing2Double)));
						Eingegebenes.setText(String.valueOf(gesEingD));
						Eingabe.setText(s.substring(0,s.length()-2));
					}
				}
					else if(gesEing.indexOf(".")<0) {
						gesEing2DoubleI = Double.parseDouble(gesEing2);
						if(operator.equals("+")) {
							Eingabe.setText(String.valueOf((double)gesEingD + gesEing2DoubleI));
						}
						else if(operator.equals("*")) {
							Eingabe.setText(String.valueOf((double)gesEingD * gesEing2DoubleI));
						}
						else if(operator.equals("/")) {
							s = String.valueOf(((double)gesEingD / (double)gesEing2DoubleI));
							if(s.length()>15) {
							Eingabe.setText(s.substring(0,s.length()-3));}
							else {Eingabe.setText(String.valueOf((double)gesEingD/(double)gesEing2DoubleI));}
						}
						else if(operator.equals("-")) {
							Eingabe.setText(String.valueOf((double)gesEingD - gesEing2DoubleI));
						}
						else if(operator.equals("%")) {
							Eingabe.setText(String.valueOf((double)gesEingD % gesEing2DoubleI));
						}
						else if(operator.equals("**")) {
							s = (String.valueOf(Math.pow((double)gesEingD, gesEing2DoubleI)));
							Eingegebenes.setText(String.valueOf((double)gesEingD));
							Eingabe.setText(s.substring(0,s.length()-2));
						}
						}
					}
				
				
				Eingegebenes.setText("");
				}catch(NumberFormatException e1) {
					
				}
			}
		});
		mp.add(gleichbtn);
		
		btn0 = new JButton("0");
		btn0.setBounds(78,429,67,53);
		btn0.setBackground(new Color(232,232,232));
		btn0.setFont(font);
		btn0.setVisible(true);
		btn0.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				
				String EingabeText = Eingabe.getText() + "0";
				Eingabe.setText(EingabeText);
			}
		});
		mp.add(btn0);
		
		mp.repaint();
		gui.repaint();
	}
}
